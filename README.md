# Intel_Unnati_Industrial_Training_Program_2025

## Gistify – "Summarise Smarter"

**Gistify** is a smart web-based application that transcribes, summarizes, and translates spoken content from **YouTube videos** using OpenAI's Whisper model. It provides concise AI-generated summaries, multilingual translation, and PDF export — all through a clean and user-friendly interface.

---
## Table of Contents  
- [Project Overview](#project-overview)  
- [Folder Structure](#folder-structure) 
- [Project Flow](#project-flow)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Results](#results)  
- [Technologies Used](#technologies-used)    
- [Authors](#authors)

---
## Project Overview  
Gistify is a Python-Flask-based tool that automates summarization and translation tasks using AI. It supports various input formats like YouTube videos and PDF documents, and provides summarized output in text, speech, and downloadable formats. It also includes educational features such as MCQ generation, a glossary extractor, and a chatbot for solving user queries.

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
## Project Flow  
Below is the functional workflow of the Gistify system:
<img width="776" height="433" alt="intel process flow" src="https://github.com/user-attachments/assets/c9426067-97ad-4408-8541-c7ae4b0cb8bd" />


## Technologies Used

- **Python**
- **Flask** & **Flask-Session**
- **OpenAI Whisper**
- **yt-dlp**
- **xhtml2pdf**
- **LangChain**, **Transformers**, **Optimum (OpenVINO)**
- **Deep Translator**
- **NLTK**
---

## Installation

```plaintext
1. Clone the repo:
   git clone https://github.com/sharmila-36/Intel_Project_Gistify.git
   cd Intel_Project_Gistify

2. Install dependencies:
   pip install -r requirements.txt

3. Run the app:
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
