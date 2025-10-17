import streamlit as st
from transformers import pipeline
from PIL import Image

st.set_page_config(page_title="🌟 Care & Cheer App", page_icon="🌟")
st.title("🌟 Care & Cheer App (Lightweight Version)")

st.write("Upload your selfie or photo to receive an encouraging message!")

uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    # Auto-fix orientation from phone photos
    try:
        image = Image.open(uploaded_file)
        image = image.transpose(Image.Transpose.EXIF)
    except Exception:
        pass

    st.image(image, caption="Your uploaded image", use_container_width=True)
    st.info("Analyzing image... please wait a few seconds ⏳")

    # Lightweight model suitable for CPU (Streamlit Cloud)
    captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

    result = captioner(image)[0]["generated_text"]

    # Create a positive, caring response
    encouraging_message = f"You're looking amazing! 🌟 Here's what I see: {result}. Keep being awesome!"

    st.success(encouraging_message)
