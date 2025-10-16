# app.py
import streamlit as st

st.set_page_config(page_title="D.R.A.M.A.", page_icon="🎬", layout="centered")

# --- Custom CSS for logo-like text ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Montserrat:wght@300;600&display=swap');

    .logo-wrap{
        display: flex;
        align-items: center;
        justify-content: center;
        height: 70vh;                 /* center vertically on the page */
        flex-direction: column;
        gap: 10px;
    }

    .logo-main {
        font-family: 'Playfair Display', serif;
        font-weight: 900;
        font-size: 84px;
        letter-spacing: 8px;
        color: #E94F6D;               /* main accent color (warm magenta) */
        text-shadow:
            0 2px 0 rgba(0,0,0,0.12),
            0 10px 25px rgba(233,79,109,0.18);
        margin: 0;
    }

    .logo-sub {
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        font-size: 18px;
        color: #2F4858;               /* dark slate for subtitle */
        opacity: 0.9;
        margin: 0;
        letter-spacing: 1px;
    }

    /* small screen adjustments */
    @media (max-width: 600px) {
        .logo-main { font-size: 44px; letter-spacing: 4px; }
        .logo-sub  { font-size: 14px; }
    }
    </style>

    <div class="logo-wrap">
        <div class="logo-main">D.R.A.M.A.</div>
        <div class="logo-sub">Data-driven Revenue &amp; Audience Metrics Analyst</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Keep page minimal
st.write("")  # leave blank so only logo is visible