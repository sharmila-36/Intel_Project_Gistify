from flask import Flask, render_template, request, send_file, session, render_template_string, redirect, url_for, jsonify
import os, io, re, uuid
import whisper
import yt_dlp
from xhtml2pdf import pisa
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from transformers import AutoTokenizer
from optimum.intel.openvino import OVModelForSeq2SeqLM
from deep_translator import GoogleTranslator
import nltk
from flask_session import Session

nltk.download('punkt')
from nltk.tokenize import sent_tokenize

app = Flask(__name__)
app.secret_key = "supersecretkey"
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.before_request
def redirect_to_welcome():
    if not session.get("seen_welcome") and request.endpoint == "index":
        return redirect(url_for("welcome"))

@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

@app.route("/go-to-main")
def go_to_main():
    session["seen_welcome"] = True
    return redirect(url_for("index"))

# === Load Models ===
whisper_model = whisper.load_model("base")
tokenizer = AutoTokenizer.from_pretrained("t5-small")
summary_model = OVModelForSeq2SeqLM.from_pretrained("t5-small", export=True)

llm = ChatGroq(api_key="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", model="llama3-8b-8192", temperature=0.0)

# === Prompt Templates ===
mcq_prompt = PromptTemplate(input_variables=["context", "num_questions"], template="""
You are an AI assistant generating multiple-choice questions (MCQs) from the following text:

{context}

Generate {num_questions} MCQs with:
- A question
- Three options (A, B, C)
- Correct answer clearly marked at the end

Format:
MCQ
Question: [question]
A) [option A]
B) [option B]
C) [option C]
Correct Answer: [correct option]
""")

notes_prompt = PromptTemplate(input_variables=["context"], template="""
You are an AI note-taker. Convert the following educational content into structured bullet-point study notes:

{context}

Output:
- Clear, concise bullet points covering the main ideas.
""")

glossary_prompt = PromptTemplate(input_variables=["context"], template="""
You are a glossary generator. From the following content, extract 8 important terms and provide a short, simple definition for each.

{context}

Format:
1. Term: Definition
""")

mcq_chain = LLMChain(llm=llm, prompt=mcq_prompt)
notes_chain = LLMChain(llm=llm, prompt=notes_prompt)
glossary_chain = LLMChain(llm=llm, prompt=glossary_prompt)

# === Helpers ===
def parse_mcqs(raw_text):
    pattern = r"Question:\s*(.*?)\nA\)\s*(.*?)\nB\)\s*(.*?)\nC\)\s*(.*?)\nCorrect Answer:\s*([ABC])"
    matches = re.findall(pattern, raw_text, re.DOTALL)
    mcqs = []
    for match in matches:
        question, a, b, c, correct = match
        options = [a.strip(), b.strip(), c.strip()]
        correct_index = ord(correct.strip().upper()) - ord('A')
        if 0 <= correct_index < 3:
            mcqs.append({
                "question": question.strip(),
                "options": options,
                "answer": options[correct_index]
            })
    return mcqs

def clean_summary(text):
    text = re.sub(r'[.,]{2,}', '.', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\.{2,}', '.', text)
    text = re.sub(r'\s*\.\s*', '. ', text)
    text = re.sub(r'\s*,\s*', ', ', text)

    sentences = sent_tokenize(text)
    seen = set()
    filler_phrases = [
        "here's", "let's take", "basically", "actually", "in fact", "so", "you know",
        "i think", "kind of", "sort of", "just", "like", "it's normally", "as you can see"
    ]
    cleaned_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) < 10:
            continue
        for filler in filler_phrases:
            sentence = re.sub(rf'\b{filler}\b', '', sentence, flags=re.IGNORECASE)
        sentence = sentence.strip()
        if sentence and sentence.lower() not in seen:
            seen.add(sentence.lower())
            sentence = sentence[0].upper() + sentence[1:]
            cleaned_sentences.append(sentence)

    return ' '.join(cleaned_sentences)


def translate_text(full_text, target_lang):
    max_chunk_size = 5000
    chunks = [full_text[i:i+max_chunk_size] for i in range(0, len(full_text), max_chunk_size)]
    translated_chunks = []
    for chunk in chunks:
        if not chunk.strip():
            continue
        try:
            translated = GoogleTranslator(source='auto', target=target_lang).translate(chunk)
            translated_chunks.append(translated)
        except:
            translated_chunks.append("[Translation failed]")
    return ' '.join(translated_chunks)

def download_audio(youtube_url):
    uid = uuid.uuid4().hex
    output_template = f"audio_{uid}.%(ext)s"
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_template,
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        base = ydl.prepare_filename(info).rsplit(".", 1)[0]
        mp3_file = f"{base}.mp3"
        if not os.path.exists(mp3_file):
            raise Exception("Failed to convert to MP3")
        return mp3_file

def transcribe_audio(file_path):
    return whisper_model.transcribe(file_path)["text"]

def chunk_text(text, max_tokens=500):
    sentences = sent_tokenize(text)
    chunks, chunk = [], ''
    for sentence in sentences:
        if len(tokenizer.encode(chunk + sentence)) < max_tokens:
            chunk += sentence + " "
        else:
            if chunk.strip():
                chunks.append(chunk.strip())
            chunk = sentence + " "
    if chunk.strip():
        chunks.append(chunk.strip())
    return chunks
def pre_clean_transcript(text):
    # Remove excessive punctuation and whitespace
    text = re.sub(r"[.,]{2,}", ".", text)
    text = re.sub(r",+", ",", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\.{2,}", ".", text)

    # Remove stuttering repeated words: "got got got", "and and and"
    text = re.sub(r'\b(\w+)( \1\b)+', r'\1', text, flags=re.IGNORECASE)

    # Remove repeated lines
    lines = text.splitlines()
    seen = set()
    cleaned_lines = []
    for line in lines:
        line = line.strip()
        if line and line.lower() not in seen:
            seen.add(line.lower())
            cleaned_lines.append(line)
    text = " ".join(cleaned_lines)

    # Remove repeated sentences
    sentences = sent_tokenize(text)
    final_sentences = []
    seen_sentences = set()
    for sent in sentences:
        clean = sent.strip()
        if clean.lower() not in seen_sentences:
            seen_sentences.add(clean.lower())
            final_sentences.append(clean)
    return " ".join(final_sentences)


def summarize_text(text):
    chunks = chunk_text(text)
    final_summary = ""
    seen = set()
    for chunk in chunks:
        if not chunk.strip():
            continue
        try:
            inputs = tokenizer(chunk, return_tensors="pt", truncation=True)
            if inputs["input_ids"].shape[1] == 0:
                final_summary += "[Empty input skipped] "
                continue
            outputs = summary_model.generate(**inputs, max_length=150, min_length=40)
            summary_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
            if summary_text and summary_text not in seen:
                seen.add(summary_text)
                final_summary += summary_text + " "
        except Exception as e:
            final_summary += f"[Summary failed: {str(e)}] "
    return final_summary.strip()
@app.route("/translate", methods=["POST"])
def translate():
    lang_map = {"english": "en", "tamil": "ta", "hindi": "hi", "telugu": "te", "malayalam": "ml"}
    selected_lang = request.form.get("language")

    session["selected_lang"] = selected_lang
    summary = session.get("summary", "")

    if not summary:
        session["translated_summary"] = "⚠️ No summary to translate."
        return redirect(url_for("index"))

    if selected_lang and selected_lang in lang_map and selected_lang != "english":
        session["translated_summary"] = translate_text(summary, lang_map[selected_lang])
    else:
        session["translated_summary"] = None

    return redirect(url_for("index"))


# ... (everything above remains unchanged until index() function)

@app.route("/", methods=["GET", "POST"])
def index():
    lang_map = {"english": "en", "tamil": "ta", "hindi": "hi", "telugu": "te", "malayalam": "ml"}

    if request.method == "POST":
        url = request.form.get("youtube_url")
        session["summary"] = None
        session["translated_summary"] = None
        session["selected_lang"] = None

        if not url:
            session["summary"] = "⚠️ No URL provided."
            return redirect(url_for("index"))

        try:
            audio_path = download_audio(url)
            transcript = transcribe_audio(audio_path)
            os.remove(audio_path)

            if not transcript.strip():
                session["summary"] = "⚠️ No speech detected in the video."
                return redirect(url_for("index"))

# ✅ Pre-clean transcript and clean summary for best quality
            cleaned_transcript = pre_clean_transcript(transcript)
            raw_summary = summarize_text(cleaned_transcript)
            summary = clean_summary(raw_summary)
            session["summary"] = summary


        except Exception as e:
            session["summary"] = f"⚠️ Error: {str(e)}"
            return redirect(url_for("index"))

        session["mcqs"] = None
        session["mcqs_raw"] = None
        session["notes"] = None
        session["glossary"] = None

        return redirect(url_for("index"))

    return render_template("index.html",
                           summary=session.get("summary"),
                           translated_summary=session.get("translated_summary"),
                           mcqs=session.get("mcqs"),
                           mcqs_raw=session.get("mcqs_raw"),
                           notes=session.get("notes"),
                           glossary=session.get("glossary"))

@app.route("/generate-mcq")
def generate_mcq():
    summary = session.get("summary", "")
    if not summary:
        return redirect(url_for("index"))
    try:
        raw_mcqs = mcq_chain.run({"context": summary, "num_questions": 5}).strip()
        session["mcqs"] = parse_mcqs(raw_mcqs)
        session["mcqs_raw"] = raw_mcqs
    except Exception as e:
        session["mcqs"] = []
        session["mcqs_raw"] = f"Error: {str(e)}"
    return redirect(url_for("index"))

@app.route("/generate-notes")
def generate_notes():
    summary = session.get("summary", "")
    if not summary:
        return redirect(url_for("index"))
    try:
        session["notes"] = notes_chain.run({"context": summary}).strip()
    except Exception as e:
        session["notes"] = f"Error generating notes: {str(e)}"
    return redirect(url_for("index"))

@app.route("/generate-glossary")
def generate_glossary():
    summary = session.get("summary", "")
    if not summary:
        return redirect(url_for("index"))
    try:
        session["glossary"] = glossary_chain.run({"context": summary}).strip()
    except Exception as e:
        session["glossary"] = f"Error generating glossary: {str(e)}"
    return redirect(url_for("index"))

@app.route("/download-summary-notes-glossary")
def download_summary_notes_glossary():
    summary = session.get("summary", "No summary available.")
    notes = session.get("notes", "No notes available.")
    glossary = session.get("glossary", "No glossary available.")
    html = render_template_string("""
    <html><body>
        <h2>🧠 Summary</h2><p>{{ summary }}</p>
        <h2>🗒️ Notes</h2><pre>{{ notes }}</pre>
        <h2>📚 Glossary</h2><pre>{{ glossary }}</pre>
    </body></html>""", summary=summary, notes=notes, glossary=glossary)
    stream = io.BytesIO()
    pisa.CreatePDF(io.StringIO(html), dest=stream)
    stream.seek(0)
    return send_file(stream, download_name="summary_notes_glossary.pdf", as_attachment=True)

@app.route("/download-mcq-pdf")
def download_mcq_pdf():
    mcqs_raw = session.get("mcqs_raw", "No MCQs available.")
    html = render_template_string("<html><body><h2>Generated MCQs</h2><pre>{{ mcqs }}</pre></body></html>", mcqs=mcqs_raw)
    stream = io.BytesIO()
    pisa.CreatePDF(io.StringIO(html), dest=stream)
    stream.seek(0)
    return send_file(stream, download_name="mcqs.pdf", as_attachment=True)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    question = data.get("question")
    summary = session.get("summary", "")
    if not summary:
        return jsonify({"answer": "No summary available to answer from."})
    prompt = f"""You are a helpful assistant. Use the following summary to answer the question.\n\nSummary: {summary}\n\nQuestion: {question}\nAnswer:"""
    try:
        reply = llm.invoke(prompt)
        return jsonify({"answer": reply.content.strip()})
    except Exception as e:
        return jsonify({"answer": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
