# Intel Unnati Industrial Training Program 2025

## Gistify – "Summarise Smarter"

## Project Overview

Students increasingly turn to YouTube and similar platforms for learning, but long and dense videos can be overwhelming. Challenges like note-taking, staying focused, language barriers, and lack of quick revision tools often hinder effective learning.

Gistify solves this by turning any YouTube lecture into a simplified, student-friendly format. It uses AI to transcribe, summarize, translate, and generate quizzes, notes, and glossaries — all within a clean web interface.

### Key Modules:  
- 📹 YouTube Video Summarization  
- 📄 PDF Document Summarization  
- 🔊 Text-to-Speech (Voice Summary)  
- ❓ MCQ Generation from Summarized Text  
- 🤖 Chatbot for Doubt Solving  
- 📚 Glossary Term Extraction  
- 🌐 Multilingual Translation  
- 📝 PDF Export of Summaries 


---
## Table of Contents  
- [Project Overview](#project-overview)  
- [Folder Structure](#folder-structure) 
- [Process Flow](#process-flow)
- [Tech Stack Used](#tech-stack-used)  
- [Installation](#installation)
- [Screenshots](#screenshots)
- [Demo Video](#demo-video)
- [Sample Downloads](#sample-downloads)
- [Results](#results)     
- [Authors](#authors)

---
 

---
## Folder Structure

```plaintext
Intel_Project_Gistify/
│
├── templates/             # HTML files (e.g., welcome.html, index.html)
├── static/                # CSS, JS, images
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
```
## Process Flow  

<img width="776" height="433" alt="intel process flow" src="https://github.com/user-attachments/assets/c9426067-97ad-4408-8541-c7ae4b0cb8bd" />

The Gistify application follows a modular pipeline that processes YouTube educational videos into interactive, multilingual learning content. Here’s the complete flow:

1. *🔗 YouTube URL Input*
   - The user enters a YouTube video link into the web interface built with Flask.

2. *🎧 Audio Extraction (yt-dlp)*
   - The backend extracts only the audio stream using yt-dlp, ensuring faster and lightweight downloads.

3. *🗣 Transcription (Whisper)*
   - The audio is transcribed into English text using OpenAI's Whisper model.

4. *🧹 Transcript Cleaning (NLTK + Regex)*
   - The raw transcript is cleaned to remove filler words, repeated phrases, and punctuation issues using pre_clean_transcript() and clean_summary().

5. *🧠 Summarization (T5 + OpenVINO)*
   - The cleaned transcript is passed into a T5 summarization model optimized with OpenVINO for fast CPU inference, producing a concise summary.

6. *🌐 Translation (Deep Translator)*
   - The summary can be manually translated into Tamil, Hindi, Telugu, Malayalam, and Kannada by splitting it into chunks and translating each.

7. *📝 AI Content Generation (LangChain + Groq)*
   - The summary is used as context to generate:
     - Multiple-Choice Questions (MCQs)
     - Important Notes
     - Glossary terms  
   - These are generated using Groq-hosted LLaMA-3 via LangChain.

8. *🤖 Doubt-Solving Chatbot*
   - A chatbot (LLM-based via LangChain) answers student questions in natural language, using the summary as context.

9. *📥 PDF Export (xhtml2pdf)*
   - The summary, notes, glossary, and quiz can be downloaded as a single PDF for offline study.

10. *🖥 User Interface*
    - The Flask-based frontend displays all results: summary, translation, MCQs, chatbot, and download buttons, with text-to-speech support and floating chatbot.
---

## Tech Stack Used

### ⚙ Backend & Core Technologies

| Technology               | Purpose in Project |
|--------------------------|--------------------|
| *Python*               | Main programming language used to develop both backend logic and AI features. |
| *Flask*                | Lightweight web framework used to create the application backend and API routes. |
| *Flask-Session*        | Handles session management to store user data like summary and translations during interaction. |
| *OpenAI Whisper*       | Converts YouTube video audio into accurate transcribed text for further processing. |
| *yt-dlp*               | Downloads audio from YouTube videos, used as input for Whisper transcription. |
| *LangChain*            | Framework for chaining together LLM components — used here for MCQ, notes, and glossary generation. |
| *Transformers (Hugging Face)* | Provides access to pretrained NLP models like T5 for summarization. |
| *Optimum + OpenVINO*   | Optimizes and accelerates inference for the summarization model (T5) using OpenVINO. |
| *Deep Translator*      | Enables summary translation into regional languages like Hindi, Tamil, Telugu, Malayalam, and Kannada. |
| *NLTK*                 | Natural Language Toolkit used for cleaning transcript text (e.g., sentence tokenization, stopword removal). |
| *xhtml2pdf*            | Converts the final summary into a downloadable and printable PDF. |
---

## Installation  
To get started, clone the repository and install the required dependencies:

```plaintext
git clone https://github.com/sharmila-36/Intel_Project_Gistify.git  
cd Intel_Project_Gistify  
pip install -r requirements.txt  
```
Run the app:
```plaintext
python app.py
```
## Screenshots

Below are key UI screens and features of **Gistify**:

---

### 🏠 1. Home / Welcome Page  
_The clean and simple landing page where users begin the summarization journey._

![Home Page](https://github.com/sharmila-36/Intel_Project_Gistify/blob/eb003a6491ad7bc4e95d1d1e79642d41e7293b23/Intel%20Project%20Gistify/final%20intel%20updated%20project/output%20screen%20shots/input_page.png.png)

---

### 🔗 2. YouTube URL Input Page  
_Users paste the link of the YouTube video for summarization._

![YouTube Input](https://github.com/sharmila-36/Intel_Project_Gistify/blob/main/Intel%20Project%20Gistify/final%20intel%20updated%20project/output%20screen%20shots/input_page.png.png)

---

### 📄 3. Summary Output Page  
_AI-generated summary based on the transcribed content._

![Summary Output](https://github.com/sharmila-36/Intel_Project_Gistify/blob/eb003a6491ad7bc4e95d1d1e79642d41e7293b23/Intel%20Project%20Gistify/final%20intel%20updated%20project/output%20screen%20shots/summary_output.png.png)

---

### 🌐 4. Translated Summary Page  
_Summary translated into selected regional language._

![Translated Summary](https://github.com/sharmila-36/Intel_Project_Gistify/blob/eb003a6491ad7bc4e95d1d1e79642d41e7293b23/Intel%20Project%20Gistify/final%20intel%20updated%20project/output%20screen%20shots/translated_summary.png)



---
### 📝 5. MCQ Generation Page  
_Automatically generated multiple-choice questions based on the summarized content._

![MCQ Page](https://github.com/sharmila-36/Intel_Project_Gistify/blob/eb003a6491ad7bc4e95d1d1e79642d41e7293b23/Intel%20Project%20Gistify/final%20intel%20updated%20project/output%20screen%20shots/mcq_page.png)


### 📝 6. Generate Notes Page  
_Notes and multiple-choice questions extracted from the summary._

![Notes Page](https://github.com/sharmila-36/Intel_Project_Gistify/blob/eb003a6491ad7bc4e95d1d1e79642d41e7293b23/Intel%20Project%20Gistify/final%20intel%20updated%20project/output%20screen%20shots/generated_notes.png)

---

### 📚 7. Glossary Terms Page  
_Terms with definitions automatically generated from the summary._

![Glossary Page](https://github.com/sharmila-36/Intel_Project_Gistify/blob/eb003a6491ad7bc4e95d1d1e79642d41e7293b23/Intel%20Project%20Gistify/final%20intel%20updated%20project/output%20screen%20shots/glossary.png)

---

### 💬 8. Chatbot Interface  
_An interactive chatbot that answers questions based on the content._

![Chatbot UI](https://github.com/sharmila-36/Intel_Project_Gistify/blob/eb003a6491ad7bc4e95d1d1e79642d41e7293b23/Intel%20Project%20Gistify/final%20intel%20updated%20project/output%20screen%20shots/chatbot.png)

---

### 📥 9. Downloadable PDF Output  
_All generated content (summary, glossary, notes, MCQs) is compiled into a PDF._

🔗 [Click here to view/download the sample PDF](https://github.com/sharmila-36/Intel_Project_Gistify/blob/eb003a6491ad7bc4e95d1d1e79642d41e7293b23/Intel%20Project%20Gistify/final%20intel%20updated%20project/output%20screen%20shots/sample_notes.pdf)
## Demo Video

Watch the full walkthrough of the Gistify application in action:

▶️ [Click here to view the demo video](https://drive.google.com/file/d/1mQCqzhvOp77Y-tq5elSXKQjldvYns8X2/view?usp=sharing)


## Sample Downloads

Explore real PDF outputs generated by Gistify:

- 🧾 [Sample Output: Summary + Notes + Glossary](https://github.com/sharmila-36/Intel_Project_Gistify/blob/main/Intel%20Project%20Gistify/final%20intel%20updated%20project/sample_outputs/summary_notes_glossary.pdf)

- 📘 [Sample MCQs](https://github.com/sharmila-36/Intel_Project_Gistify/blob/main/Intel%20Project%20Gistify/final%20intel%20updated%20project/sample_outputs/sample_mcq's.pdf)

> These PDFs are downloadable and demonstrate how Gistify converts educational content into structured learning materials.


## Results

- ✅ Summarized and translated content displayed on the web interface.  
- 📥 Option to download voice summaries and PDF reports.  
- 💬 Interactive chatbot to clarify queries.  
- 📝 Generated MCQs and glossary terms based on the summarized content.

---

## Authors

- **Shamsu Nisha N** – Backend Developer (Team Lead)  
  Developed core backend features: MCQ generation, glossary, chatbot.

- **Sharmila D** – AI & System Designer  
  Designed architecture, integrated OpenVINO with LLMs for summarization.

- **Tharani V S** – UI/UX Developer  
  Built intuitive frontend for smooth user experience.

---
