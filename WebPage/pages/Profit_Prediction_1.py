import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
from pathlib import Path

# ---------- MAPPINGS ---------- #

GENRES = [
    "Action", "Adventure", "Animation", "Biography", "Comedy", "Crime", "Drama", "Family", 
    "Fantasy", "Film-Noir", "History", "Horror", "Music", "Musical", "Mystery", "Romance", 
    "Sci-Fi", "Sport", "Thriller", "War", "Western"
]

DIRECTORS = {
    "James Cameron": "director_nm0000116",
    "Francis Lawrence": "director_nm1349376",
    "M. Night Shyamalan": "director_nm0796117",
    "Chris Columbus": "director_nm0001060",
    "Todd Phillips": "director_nm0680846",
    "Joe Russo": "director_nm0751648",
    "Anthony Russo": "director_nm0751577",
    "David Yates": "director_nm0001392",
    "James Wan": "director_nm0004716",
    "Sam Mendes": "director_nm0811583",
    "Jon Favreau": "director_nm0942367",
    "Justin Lin": "director_nm0905154",
    "Sergio Leone": "director_nm0001466",
    "Martin Scorsese": "director_nm0000217",
    "Andrew Stanton": "director_nm0083348",
    "Steven Spielberg": "director_nm0000229",
    "James L. Brooks": "director_nm0000631",
    "Ron Howard": "director_nm0000318",
    "Quentin Tarantino": "director_nm0000233",
    "Christopher Nolan": "director_nm0634240",
    "Francis Ford Coppola": "director_nm0000399",
    "Peter Jackson": "director_nm0000881",
    "Tim Burton": "director_nm0000709",
    "Ridley Scott": "director_nm0001741",
    "Bryan Singer": "director_nm0005363",
    "Michael Mann": "director_nm0000142",
    "Joel Coen": "director_nm0000165",
    "Denis Villeneuve": "director_nm0004056",
    "Gareth Edwards": "director_nm0298807",
    "Michael Bay": "director_nm0005222",
    "David Fincher": "director_nm0327944",
    "Roland Emmerich": "director_nm0269463",
    "Christopher McQuarrie": "director_nm0570912",
    "Ang Lee": "director_nm0510912",
    "Joss Whedon": "director_nm0891216",
    "Woody Allen": "director_nm0000040",
    "Robert Zemeckis": "director_nm0001661",
    "George Lucas": "director_nm0001054",
    "Stanley Kubrick": "director_nm0001053",
    "Gore Verbinski": "director_nm0000965",
    "Zack Snyder": "director_nm0868219",
    "Sam Raimi": "director_nm0893659",
    "J.J. Abrams": "director_nm0003506",
    "Clint Eastwood": "director_nm0009190",
    "Brad Bird": "director_nm0946734",
    "The Wachowskis": "director_nm1490123",
    "Guillermo del Toro": "director_nm0898288",
    "Roman Polanski": "director_nm0000338",
    "Oliver Stone": "director_nm0001716",
    "Peter Berg": "director_nm0881279"
}

ACTORS = {
    "Chris Pratt": "actor_nm0695435",
    "Ian McKellen": "actor_nm0424060",
    "Will Smith": "actor_nm0000226",
    "Jeremy Renner": "actor_nm0000437",
    "Willem Dafoe": "actor_nm0262635",
    "Harrison Ford": "actor_nm0000148",
    "Andy Serkis": "actor_nm0005212",
    "Leonardo DiCaprio": "actor_nm0001570",
    "Emma Watson": "actor_nm0914612",
    "Laurence Fishburne": "actor_nm0736622",
    "Bradley Cooper": "actor_nm0670408",
    "Jonah Hill": "actor_nm0719637",
    "Edward Norton": "actor_nm0177896",
    "Johnny Depp": "actor_nm0000228",
    "Simon Pegg": "actor_nm0688335",
    "Samuel L. Jackson": "actor_nm0000168",
    "Brad Pitt": "actor_nm0000093",
    "Tom Hanks": "actor_nm0000158",
    "Scarlett Johansson": "actor_nm0413168",
    "Tom Cruise": "actor_nm0000129",
    "Robert Downey Jr.": "actor_nm0000375",
    "Matt Damon": "actor_nm0000353",
    "Robert De Niro": "actor_nm0000134",
    "Vin Diesel": "actor_nm0749263",
    "Morgan Freeman": "actor_nm0000151",
    "Ben Stiller": "actor_nm0000354",
    "Bruce Willis": "actor_nm0000246",
    "Dwayne Johnson": "actor_nm0748620",
    "Christian Bale": "actor_nm0000288",
    "Denzel Washington": "actor_nm0000332",
    "Chris Hemsworth": "actor_nm0350453",
    "Mark Ruffalo": "actor_nm0005351",
    "Natalie Portman": "actor_nm0000204",
    "Jennifer Lawrence": "actor_nm2225369",
    "George Clooney": "actor_nm0000120",
    "Daniel Craig": "actor_nm0000179",
    "Tom Hardy": "actor_nm0000401",
    "Clint Eastwood": "actor_nm0000553",
    "Liam Neeson": "actor_nm0000474",
    "Jude Law": "actor_nm0876138",
    "Keanu Reeves": "actor_nm0000206",
    "Chris Evans": "actor_nm0202966",
    "Gary Oldman": "actor_nm0000198",
    "Chris Pine": "actor_nm1706767",
    "Ken Watanabe": "actor_nm0564215",
    "Zoe Saldana": "actor_nm0785227",
    "Jeff Goldblum": "actor_nm0252961",
    "Emma Stone": "actor_nm1297015",
    "Eddie Murphy": "actor_nm0000191",
    "Cate Blanchett": "actor_nm0004874"
}

LANGUAGES = {
    "English": "lang_en",
    "Japanese": "lang_ja",
    "Italian": "lang_it",
    "French": "lang_fr",
    "Korean": "lang_ko",
    "Spanish": "lang_es",
    "German": "lang_de",
    "Portuguese": "lang_pt",
    "Hindi": "lang_hi",
    "Danish": "lang_da",
    "Chinese": "lang_zh",
    "Persian": "lang_fa"
}

COMPANIES = {
    "Warner Bros. Pictures": "company_Warner_Bros_Pictures",
    "Universal Pictures": "company_Universal_Pictures",
    "Columbia Pictures": "company_Columbia_Pictures",
    "20th Century Fox": "company_20th_Century_Fox",
    "Paramount Pictures": "company_Paramount_Pictures",
    "New Line Cinema": "company_New_Line_Cinema",
    "Marvel Studios": "company_Marvel_Studios",
    "DreamWorks Pictures": "company_DreamWorks_Pictures",
    "Relativity Media": "company_Relativity_Media",
    "Village Roadshow Pictures": "company_Village_Roadshow_Pictures",
    "Amblin Entertainment": "company_Amblin_Entertainment",
    "TSG Entertainment": "company_TSG_Entertainment",
    "Lionsgate": "company_Lionsgate",
    "Legendary Pictures": "company_Legendary_Pictures",
    "Summit Entertainment": "company_Summit_Entertainment",
    "Metro-Goldwyn-Mayer": "company_Metro-Goldwyn-Mayer",
    "Walt Disney Pictures": "company_Walt_Disney_Pictures",
    "Working Title Films": "company_Working_Title_Films",
    "Regency Enterprises": "company_Regency_Enterprises",
    "Touchstone Pictures": "company_Touchstone_Pictures",
    "Scott Free Productions": "company_Scott_Free_Productions",
    "Pixar": "company_Pixar",
    "Marvel Entertainment": "company_Marvel_Entertainment",
    "Heyday Films": "company_Heyday_Films",
    "Miramax": "company_Miramax",
    "Dune Entertainment": "company_Dune_Entertainment",
    "Scott Rudin Productions": "company_Scott_Rudin_Productions",
    "Jerry Bruckheimer Films": "company_Jerry_Bruckheimer_Films",
    "Lucasfilm Ltd": "company_Lucasfilm_Ltd",
    "RatPac Entertainment": "company_RatPac_Entertainment"
}

COUNTRIES = {
    "United States": "country_US",
    "United Kingdom": "country_GB",
    "Germany": "country_DE",
    "France": "country_FR",
    "Canada": "country_CA",
    "Australia": "country_AU",
    "Spain": "country_ES",
    "Japan": "country_JP",
    "Italy": "country_IT",
    "China": "country_CN",
    "New Zealand": "country_NZ",
    "India": "country_IN",
    "Hong Kong": "country_HK",
    "Mexico": "country_MX",
    "Ireland": "country_IE",
    "South Korea": "country_KR",
    "Brazil": "country_BR",
    "South Africa": "country_ZA",
    "Switzerland": "country_CH",
    "Bulgaria": "country_BG"
}


# ---------- STREAMLIT PAGE ---------- #

st.title(" Movie Profit Predictor")

st.write("Enter the movie details below to predict its **estimated revenue**:")

# Genres
selected_genres = st.multiselect("Select genres:", GENRES)
selected_genre_codes = [f"genre_{g}" for g in selected_genres]

# Director & Actor
selected_director = st.selectbox("Select director:", list(DIRECTORS.keys()))
selected_actor = st.selectbox("Select main actor:", list(ACTORS.keys()))

# Country, Company, Language
selected_country = st.selectbox("Select country:", list(COUNTRIES.keys()))
selected_company = st.selectbox("Select production company:", list(COMPANIES.keys()))
selected_language = st.selectbox("Select movie language:", list(LANGUAGES.keys()))

# Numeric fields
budget = st.number_input("Budget (in millions USD):", min_value=0.0, max_value=1000.0, step=1.0)
runtime = st.number_input("Runtime (minutes):", min_value=30, max_value=300, step=1)
year = st.number_input("Release year:", min_value=1900, max_value=2030, step=1)
is_adult = st.checkbox("Is this an adult movie?")

# ---------- PREDICTION LOGIC ---------- #

if st.button("Predict Revenue"):
    try:
        # Load model
        # Ruta base del proyecto (sube dos niveles desde /WebPage/pages/)
        base_path = Path(__file__).resolve().parents[2]

        # Archivos del modelo
        model_path = base_path / "models" / "profit_prediction_model.pkl"
        metadata_path = base_path / "models" / "profit_prediction_metadata.json"

        # Cargar modelo
        if not model_path.exists():
            st.error(f"Model file not found: {model_path}")
        else:
            lr_model = joblib.load(model_path)

        # Cargar metadata
        if not metadata_path.exists():
            st.error(f"Metadata file not found: {metadata_path}")
        else:
            with open(metadata_path, "r") as f:
                feature_info = json.load(f)

        feature_columns = feature_info["feature_columns"]

        # Create zero-filled DataFrame
        input_data = pd.DataFrame(np.zeros((1, len(feature_columns))), columns=feature_columns)

        # Fill in selected categorical features
        selected_director_code = DIRECTORS[selected_director]
        selected_actor_code = ACTORS[selected_actor]
        selected_country_code = COUNTRIES[selected_country]
        selected_company_code = COMPANIES[selected_company]
        selected_language_code = LANGUAGES[selected_language]

        # Set 1s for available categorical columns
        for code in [selected_director_code, selected_actor_code, selected_country_code, selected_company_code, selected_language_code]:
            if code in input_data.columns:
                input_data.loc[0, code] = 1

        for genre_code in selected_genre_codes:
            if genre_code in input_data.columns:
                input_data.loc[0, genre_code] = 1

        # Numeric inputs
        if "budget_millions" in input_data.columns:
            input_data.loc[0, "budget_millions"] = budget
        if "runtime" in input_data.columns:
            input_data.loc[0, "runtime"] = runtime
        if "year" in input_data.columns:
            input_data.loc[0, "year"] = year
        if "genre_count" in input_data.columns:
            input_data.loc[0, "genre_count"] = len(selected_genres)
        if "country_count" in input_data.columns:
            input_data.loc[0, "country_count"] = 1
        if "company_count" in input_data.columns:
            input_data.loc[0, "company_count"] = 1
        if "isAdult" in input_data.columns:
            input_data.loc[0, "isAdult"] = int(is_adult)

        # Make prediction
        predicted_revenue = lr_model.predict(input_data)[0]
        st.metric(" Predicted Movie Profit", f"${predicted_revenue:,.2f}")

    except Exception as e:
        st.error(f"Error during prediction: {e}")
