# Intel Unnati Industrial Training Program 2025

## Gistify – "Summarise Smarter"

**Gistify** is a smart web-based application that transcribes, summarizes, and translates spoken content from **YouTube videos** using OpenAI's Whisper model. It provides concise AI-generated summaries, multilingual translation, and PDF export — all through a clean and user-friendly interface.

---
## Table of Contents  
- [Project Overview](#project-overview)  
- [Folder Structure](#folder-structure) 
- [Process Flow](#process-flow)
- [Tech Stack Used](#tech-stack-used)  
- [Installation](#installation)  
- [Results](#results)     
- [Authors](#authors)

---
## Project Overview  
Gistify is a Python-Flask-based tool that automates summarization and translation tasks using AI. It supports input formats like YouTube videos and provides summarized output in text, speech, and downloadable formats. It also includes educational features such as MCQ generation, a glossary extractor, and a chatbot for solving user queries.

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
