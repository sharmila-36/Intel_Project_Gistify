# Gistify - "Summarise Smarter"

**Gistify** is a smart web-based application that transcribes, summarizes, and translates spoken content from **YouTube videos** using OpenAI's Whisper model. It provides concise AI-generated summaries, multilingual translation, and PDF export — all through a clean and user-friendly interface.

---

## 🚀 Features

- 📹 YouTube video summarization  
- 📄 PDF document summarization  
- 🔊 Voice-based summary (Text-to-Speech)  
- ❓ MCQ generation  
- 🤖 Doubt-solving chatbot  
- 📚 Glossary term extraction  
- 🌐 Multilingual translation  
- 📝 PDF export

---

## 🛠️ Technologies Used

- **Python**
- **Flask** & **Flask-Session**
- **OpenAI Whisper**
- **yt-dlp**
- **xhtml2pdf**
- **LangChain**, **Transformers**, **Optimum (OpenVINO)**
- **Deep Translator**
- **NLTK**

---

## 📦 Installation

### 1. Clone the repo
git clone https://github.com/sharmila-36/Intel_Project_Gistify.git

cd Intel_Project_Gistify

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the app
python app.py

Then open your browser and go to:

http://127.0.0.1:5000

## 📁 Project Structure

```plaintext
Intel_Project_Gistify/
│
├── templates/             # HTML files (e.g., welcome.html, index.html)
├── static/                # CSS, JS, images
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
```

## 👩‍💻 Authors

- **Shamsu Nisha N** – Backend Developer (Team Lead)  
  Developed core backend features: MCQ generation, glossary, chatbot.

- **Sharmila D** – AI & System Designer  
  Designed architecture, integrated OpenVINO with LLMs for summarization.

- **Tharani V S** – UI/UX Developer  
  Built intuitive frontend for smooth user experience.
