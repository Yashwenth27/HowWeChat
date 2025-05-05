import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import plotly.graph_objects as go
import re
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize

# ----- SETTING PAGE -----
st.set_page_config(page_title="Chat Sentiment Checker", layout="wide")
st.markdown("""
    <style>
        .block-container { padding-top: 1rem; }
        h1 { margin-bottom: 0.2rem; }
        hr { margin-top: 0.2rem; margin-bottom: 0.6rem; }
    </style>
""", unsafe_allow_html=True)

# ----- MAIN APP -----
class ChatSentimentApp:
    def __init__(self):
        nltk.download('vader_lexicon')
        nltk.download('punkt')  # Needed for word_tokenize
        self.analyzer = SentimentIntensityAnalyzer()

        self.some_chat = [
            "I'm so happy today! 😊",
            "Ugh, this is so annoying 😡",
            "Let's go out for dinner 🍝",
            "That was an amazing performance! 😍",
            "I'm not sure how I feel about this...",
            "Terrible service at the restaurant 👎",
            "Had a great time with friends! 🎉",
            "Why is this always happening to me? 😔",
            "Absolutely love it! ❤️"
        ]
        self.emoji_finder = re.compile("[\U00010000-\U0010ffff]", flags=re.UNICODE)

    def draw_title(self):
        st.markdown("<h1 style='color: black;'>How we chat ?</h1>", unsafe_allow_html=True)
        self.put_line()

    def put_line(self):
        st.markdown("<hr style='border:2px solid #3B82F6; box-shadow: 0px 2px 6px #3B82F6;'>", unsafe_allow_html=True)

    def clean_chat(self, raw_text):
        lines = raw_text.splitlines()
        cleaned_msgs = []
        current_msg = ""

        def is_new_message(line):
            parts = line.split(" - ", 1)
            if len(parts) != 2:
                return False
            timestamp = parts[0]
            return "," in timestamp

        for line in lines:
            line = line.strip()
            if not line:
                continue

            if is_new_message(line):
                if current_msg:
                    cleaned_msgs.append(current_msg.strip())
                try:
                    message_part = line.split(" - ", 1)[1].split(": ", 1)[1]
                except IndexError:
                    message_part = ""
                current_msg = message_part if self._is_valid_message(message_part) else ""
            else:
                if current_msg and self._is_valid_message(line):
                    current_msg += " " + line

        if current_msg:
            cleaned_msgs.append(current_msg.strip())

        return cleaned_msgs

    def _is_valid_message(self, msg):
        msg = msg.strip().lower()
        return msg and "media omitted" not in msg and not msg.startswith("http")

    def get_mood(self, lines):
        the_counts = {'positive': 0, 'neutral': 0, 'negative': 0}
        the_words = []
        the_emojis = []

        for each in lines:
            scores = self.analyzer.polarity_scores(each)
            compound = scores['compound']
            if compound > 0.1:
                the_counts['positive'] += 1
            elif compound < -0.1:
                the_counts['negative'] += 1
            else:
                the_counts['neutral'] += 1

            the_words.extend(word_tokenize(each))
            the_emojis.extend(self.emoji_finder.findall(each))

        return the_counts, the_words, the_emojis

    def draw_words_cloud(self, the_words):
        if not the_words:
            return None
        pic = WordCloud(width=400, height=200, background_color='white').generate(' '.join(the_words))
        fig, ax = plt.subplots()
        ax.imshow(pic, interpolation='bilinear')
        ax.axis("off")
        return fig

    def show_bar_graph(self, mood_counts):
        fig = go.Figure(data=go.Bar(
            x=list(mood_counts.values()),
            y=list(mood_counts.keys()),
            orientation='h',
            marker=dict(color=['#10B981', '#9CA3AF', '#EF4444'])
        ))
        fig.update_layout(title="Sentiment Breakdown", height=300,
                          margin=dict(l=30, r=30, t=40, b=20))
        return fig

    def show(self):
        self.draw_title()
        left, right = st.columns([0.3, 0.7])

        with left:
            with st.container(border=True):
                st.subheader("What It Do?")
                st.write("Upload WhatsApp chat (.txt) or view sample.")
                file = st.file_uploader("Upload chat file", type=["txt"], label_visibility="collapsed")

        real_chat = self.some_chat
        if file:
            raw = file.read().decode("utf-8")

            with open("all_chats.txt", "a", encoding="utf-8") as archive_file:
                archive_file.write("\nQAZWSXEDCRFV\n")
                archive_file.write(raw.strip() + "\n")

            real_chat = self.clean_chat(raw)

            if real_chat:
                filtered_text = "\n".join(real_chat)
                with left:
                    st.download_button(
                        label="Download Filtered Chat (.txt)",
                        data=filtered_text,
                        file_name="filtered_chat.txt",
                        mime="text/plain"
                    )

        mood, the_words, the_emojis = self.get_mood(real_chat)

        with right:
            with st.container(border=True):
                st.markdown("### Mood Check")
                self.put_line()
                st.plotly_chart(self.show_bar_graph(mood), use_container_width=False)

            right1, right2 = st.columns(2)

            with right1:
                with st.container(border=True):
                    st.markdown("### Some Info")
                    self.put_line()
                    st.write(f"**Happy lines:** {mood['positive']}")
                    st.write(f"**Neutral lines:** {mood['neutral']}")
                    st.write(f"**Sad lines:** {mood['negative']}")
                    st.write("**Emojis:** " + (' '.join(set(the_emojis)) if the_emojis else "None found"))

            with right2:
                with st.container(border=True):
                    st.markdown("### Words in Chat")
                    self.put_line()
                    if the_words:
                        st.pyplot(self.draw_words_cloud(the_words))
                    else:
                        st.write("No words found to generate word cloud.")

# Run the app
if __name__ == "__main__":
    myapp = ChatSentimentApp()
    myapp.show()
