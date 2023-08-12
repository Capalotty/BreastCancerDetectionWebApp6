import streamlit as st

st.title("Breast Cancer Detector Using Machine Learning")
st.header("Breast Cancer Ultrasound Classification Example")
st.text("Upload a scan for Classification")


uploaded_file = st.file_uploader("Choose a scan result ...", type="png")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Scan.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    