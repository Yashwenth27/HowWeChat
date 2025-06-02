
# 💬 How we chat ?

[![Streamlit](https://img.shields.io/badge/platform-Streamlit-orange?logo=streamlit)](https://streamlit.io/)  
[![Python](https://img.shields.io/badge/language-Python-blue?logo=python)](https://www.python.org/)  

**How we chat ?** is a simple and interactive Streamlit app that analyzes the overall mood of your WhatsApp chats. Upload your exported `.txt` chat file and get an instant sentiment overview of how people really talk and feel in your conversations.

---

## ✨ Features

- 📁 **Upload WhatsApp chat file** (`.txt` format)
- 🧹 **Cleans and filters** the chat — removes media placeholders, empty lines, and irrelevant text
- 😊😢😐 **Sentiment Analysis** on each message: Happy, Sad, or Neutral
- 📊 **Visualizations:**
  - Bar chart of happy / sad / neutral message counts
  - Word cloud showing the most frequent words
  - Emoji usage summary from the chat
- 💾 **Download filtered chat** with cleaned messages only for your records

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Streamlit (`pip install streamlit`)
- Other dependencies listed in `requirements.txt`

### Running the App

1. Clone the repo:

   ```bash
   git clone https://github.com/YOUR_USERNAME/how-we-chat.git
   cd how-we-chat
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Launch the app:

   ```bash
   streamlit run app.py
   ```

4. Open your browser and upload your WhatsApp `.txt` export or try the sample chats provided.

---

## 📚 How It Works

- The app parses WhatsApp chat text line by line.
- Filters out system messages, media, and empty lines.
- Runs a sentiment analyzer on each message.
- Aggregates results and creates visual summaries.
- Displays an interactive UI to explore chat mood and contents.

---

## 📬 Feedback and Contributions

Feel free to open issues or pull requests for improvements or new features!
