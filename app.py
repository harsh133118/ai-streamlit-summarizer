import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_summarizer():
    st.info("Loading AI summarization model... This may take a moment on the first run.")
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

try:
    summarizer = load_summarizer()
except Exception as e:
    st.error(f"Error loading AI model: {e}")
    summarizer = None

st.title("🧠 AI Text Summarizer")
st.markdown("Paste a long article below and click 'Generate Summary'.")

article_text = st.text_area(
    "Paste your text here (Min. 100 characters recommended):",
    height=250,
    placeholder="e.g., The global financial markets experienced...",
)

max_length = st.slider(
    "Maximum summary length (words)",
    min_value=30,
    max_value=150,
    value=80,
    step=10
)

if st.button("Generate Summary"):
    if summarizer is None:
        st.error("Cannot run summarizer because the AI model failed to load.")
    elif len(article_text) < 100:
        st.warning("Please paste at least 100 characters for a meaningful summary.")
    else:
        with st.spinner("AI is thinking... Generating summary."):
            try:
                summary_result = summarizer(
                    article_text,
                    max_length=max_length,
                    min_length=int(max_length * 0.4),
                    do_sample=False
                )

                summary = summary_result[0]['summary_text']
                st.success("✅ Summary Generated:")
                st.info(summary)

            except Exception as e:
                st.error(f"An unexpected error occurred during summarization: {e}")

st.markdown("---")
st.caption("Built with Hugging Face and Streamlit.")
