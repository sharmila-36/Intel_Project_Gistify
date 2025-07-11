# Intel_Project_Gistify
Gistify is a web-based app that transcribes and summarizes audio using OpenAI's Whisper, with features like AI Summary, PDF export, and multilingual translation.

# Gistify

Gistify is a smart web application that transcribes, summarizes, and translates spoken content using OpenAI's Whisper model. It supports audio uploads and YouTube links, generating clean, readable summaries with optional PDF export — all from a user-friendly interface.

---

## 🚀 Features

- 🎙️ **Audio Transcription** – Upload or fetch audio from YouTube links.
- 🧠 **AI Summarization** – Summarizes transcribed text for quick understanding.
- 🌐 **Translation** – Translates output to multiple languages using Deep Translator.
- 📝 **PDF Export** – Save your transcripts and summaries as downloadable PDFs.
- 🔐 **Session Support** – Keeps user data consistent across interactions.

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
```bash
git clone https://github.com/sharmila-36/Intel_Project_Gistify.git
cd Intel_Project_Gistify

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the app
python app.py
Then open your browser and go to:
http://127.0.0.1:5000

📁 Project Structure

Gistify/
│
├── templates/             # HTML files (e.g., welcome.html, index.html)
├── static/                # CSS, JS, images
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation

📝 License
This project is open-source for educational and personal use.
Feel free to explore and adapt it with credit.

👩‍💻 Author
Sharmila D
Final Year B.Tech CSE Student
Passionate about AI, Web Development & Smart Solutions 💡
