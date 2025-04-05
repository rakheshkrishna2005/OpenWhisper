import streamlit as st
import whisper

# Set wide layout
st.set_page_config(page_title="Speech-to-Text", layout="wide")

# Load Whisper model
whisper_model = whisper.load_model("base")

# Transcribe audio function
def transcribe_audio(audio_bytes):
    temp_path = "temp.wav"
    with open(temp_path, "wb") as f:
        f.write(audio_bytes)
    result = whisper_model.transcribe(temp_path)
    return result["text"]

# Page title (centered)
st.markdown("<h1 style='text-align: center;'>🎙️ Speech-to-Text with Whisper</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload or record an audio file and get the transcription.</p>", unsafe_allow_html=True)

# Centered layout using columns in wide mode
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    recorded_audio = st.audio_input("🎙️ Record audio")
    uploaded_file = st.file_uploader("📁 Choose an audio file", type=["wav", "mp3", "m4a"])

    audio_bytes = None
    if uploaded_file:
        audio_bytes = uploaded_file.read()
    elif recorded_audio:
        audio_bytes = recorded_audio.getvalue()

    if audio_bytes:
        with st.spinner("Transcribing... Please wait ⏳"):
            transcribed_text = transcribe_audio(audio_bytes)
        st.success("Transcription complete ✅")
        st.text_area("📝 Transcribed Text", value=transcribed_text, height=200)
