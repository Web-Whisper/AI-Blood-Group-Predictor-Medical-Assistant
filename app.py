import streamlit as st
from model import predict_blood_group
from utils import process_image
import cv2

st.set_page_config(page_title="AI Blood Group Detector", layout="wide")

# 🎨 Background Styling
def set_bg():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1581093588401-12f7b8c4c1f1");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg()

# 🧾 Title
st.title("🩸 AI Blood Group Detector")
st.markdown("### Smart Medical Assistant (Simulation)")

# 📌 Mode Selection
option = st.radio(
    "Select Detection Method:",
    ["Upload Hand Image", "Live Camera Scan"]
)

# 📷 Upload Image
if option == "Upload Hand Image":
    uploaded_file = st.file_uploader("Upload Hand Image", type=["jpg", "png"])

    if uploaded_file:
        image = process_image(uploaded_file)
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        if st.button("Detect Blood Group"):
            result, confidence = predict_blood_group(image)

            st.success(f"🩸 Predicted Blood Group: {result}")
            st.info(f"📊 Confidence Level: {confidence}%")

# 📸 Camera Mode
elif option == "Live Camera Scan":
    camera = st.camera_input("Take a picture of your hand")

    if camera:
        image = process_image(camera)

        if st.button("Detect Blood Group"):
            result, confidence = predict_blood_group(image)

            st.success(f"🩸 Predicted Blood Group: {result}")
            st.info(f"📊 Confidence Level: {confidence}%")

# 🩺 Info Section
st.markdown("---")
st.header("🩺 Blood Group Information")

info = {
    "A+": "Common blood group. Can donate to A+ and AB+.",
    "O-": "Universal donor.",
    "AB+": "Universal recipient."
}

for key, value in info.items():
    st.write(f"**{key}**: {value}")
