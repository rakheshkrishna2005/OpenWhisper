# 🎙️ OpenWhisper

## 📜 Description

**OpenWhisper** lets you convert spoken audio into written text using the powerful Whisper speech recognition model. Simply upload or record audio, and get a clean transcription in seconds.

## 🚀 Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io)
- **Speech Recognition**: [OpenAI Whisper](https://github.com/openai/whisper)
- **Python Libraries**:`torch`, `openai-whisper`, `numpy`

## 🖼️ Screenshot

![App Screenshot](https://github.com/rakheshkrishna2005/OpenWhisper/blob/main/app.png?raw=true)


## ✨ Features

- 🎤 Upload or record audio directly in the browser
- 🧠 Transcribe speech to text using Whisper
- ⚡ GPU acceleration with CUDA support
- 📁 Custom model download location (`D:/whisper_models`)
- 🧹 Clean and centered wide-layout UI
- ✅ Displays transcription with progress indicators

## 🔧 Installation

1. **Clone the repo:**

```bash
git clone https://github.com/rakheshkrishna2005/OpenWhisper
cd OpenWhisper
```

2. **Set up virtual environment (optional but recommended):**

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

## ▶️ Usage

1. **Run the Streamlit app:**

```bash
streamlit run app.py
```

2. **Open your browser:**
Visit `http://localhost:8501`

3. **Upload or record audio** and view the transcription.

## 📁 File Structure

```
OpenWhisper/
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
├── app.png              # Screenshot
└── README.md            # Project overview and setup
```
