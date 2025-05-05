# How we chat ? 💬

This is a Streamlit app for checking the overall mood of a WhatsApp chat. It's called **How we chat ?** because that’s basically what it does — tells you how people in a chat actually talk or feel.

You can upload your own WhatsApp exported `.txt` chat or just try it out using the sample chats we added. The app will scan through the messages and tell you if people are being happy, sad or just neutral.

---

## 🎯 What It Do

- ✅ Upload your WhatsApp chat file (`.txt`).
- ✅ App will clean it up and remove things like media or empty lines.
- ✅ Then it will analyse the sentiment of each line.
- ✅ Shows you:
  - Bar chart of how many happy / sad / neutral messages
  - Word cloud of all the words used
  - Emojis that people use in the chat
- ✅ You can also download the filtered chat only (the clean messages).

---

## 🛠️ How To Use

1. Run the app using Streamlit:

   ```bash
   streamlit run app.py
