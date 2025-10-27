import streamlit as st
#esto es una prueba 
st.set_page_config(page_title="Go to Movie Rating Predictor 🎬", page_icon="🎥", layout="centered")

st.title(" Movie Rating Predictor App")
st.write("Click below to open the deployed version of the app:")

# Create a button-like link
st.markdown(
    """
    <style>
    .link-button {
        background-color: #4CAF50;
        color: white;
        padding: 12px 25px;
        border-radius: 10px;
        text-decoration: none;
        font-weight: bold;
        font-size: 16px;
    }
    .link-button:hover {
        background-color: #45a049;
    }
    </style>
    <a href="https://movie-rating-predictor-njxxxjsvn2uvhy7nkphw9o.streamlit.app" 
       target="_blank" class="link-button"> Open App</a>
    """,
    unsafe_allow_html=True
)