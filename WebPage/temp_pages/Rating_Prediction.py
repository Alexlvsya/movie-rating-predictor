import streamlit as st
import json
import joblib
import numpy as np
import pandas as pd

st.title('Linear Regression Model')
#open data
with open('../data/top_people_mapping.json', 'r') as f:
    people_mapping = json.load(f)

#  name <----> code mapping
def build_options(category):
    """Returns (names, name_to_code) for a given category."""
    name_to_code = {}
    for key, value in people_mapping[category].items():
        name_to_code[value["name"]] = key
    return list(name_to_code.keys()), name_to_code

# directors
director_names, director_map = build_options('directors')
selected_director_name = st.selectbox("Select a Director", director_names)
selected_director_code = director_map[selected_director_name]

# writers
writer_names, writer_map = build_options('writers')
selected_writer_name = st.selectbox("Select a Writer", writer_names)
selected_writer_code = writer_map[selected_writer_name]

# actors 
actor_names, actor_map = build_options('actors')
selected_actor_name = st.selectbox("Select an Actor", actor_names)
selected_actor_code = actor_map[selected_actor_name]

# --- Genres ---
genre_features = [
    "Action","Adult","Adventure","Animation","Biography","Comedy","Crime",
    "Documentary","Drama","Family","Fantasy","Film-Noir","Game-Show",
    "History","Horror","Music","Musical"
]

# Show genres as multi-select for user
selected_genres = st.multiselect("Select Genre(s)", genre_features)

# Map selected genres to model feature names (add prefix "genre_")
selected_genre_features = [f"genre_{g}" for g in selected_genres]
# --------Linear Regresion ------- # 

# Load trained model
model_path = '../models/linear_regression_model.pkl'
lr_model = joblib.load(model_path)

# Load feature configuration
with open('../data/feature_info.json', 'r') as f:
    feature_info = json.load(f)

feature_columns = feature_info['feature_columns']
target_variable = feature_info['target_variable']

#------Single Row Data Framwe for Prediction -----#

# Create an empty row with all features = 0
input_data = pd.DataFrame(np.zeros((1, len(feature_columns))), columns=feature_columns)

# Set the selected people to 1 (if those features exist in the model)
for code in [selected_director_code, selected_writer_code, selected_actor_code]:
    if code in input_data.columns:
        input_data.loc[0, code] = 1
# Set selected genres to 1
for genre_code in selected_genre_features:
    if genre_code in input_data.columns:
        input_data.loc[0, genre_code] = 1

#----prediction ------#
predicted_rating = lr_model.predict(input_data)[0]
st.metric(" Predicted Movie Rating", f"{predicted_rating:.2f} / 10")
