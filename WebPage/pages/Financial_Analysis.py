import streamlit as st
import pandas as pd
from PIL import Image 
st.write("""
         # TMDb Integration - Financial Data Analysis

This page demonstrates how to integrate TMDb financial data (budget, revenue) with IMDb ratings data.

## What's included:
- Budget and box office revenue
- ROI (Return on Investment) calculations
- Production companies and countries
- TMDb popularity and ratings

## Steps:
1. Set up TMDb API key
2. Load and explore the integrated data
3. Analyze financial features
4. Build enhanced prediction models
         
## What did we analyze?

📊 Dataset Shape: 93,224 movies × 26 features

📅 Year Range: 1906 - 2025

⭐ Rating Range: 1.0 - 9.7
         
TMDb Data Coverage:
   Total movies: 93,224
         
   With TMDb match: 47,244 (50.7%)
         
   With budget data: 15,201 (16.3%)
         
   With revenue data: 16,575 (17.8%)
         
   With complete financial data: 11,558 (12.4%)
""")

#image 
image8_path = "Images/output8.png"
image8 = Image.open(image8_path)
st.image(image8, caption="Regional and Language Distribution Analysis", use_container_width=True)
st.write("""
         
## Insights from Financial Analysis:
         
💰 Budget Statistics:
- Mean $29,506,852
- Median $13,000,000
- Min $1
- Max $583,900,000
    

💵 Revenue Statistics:
   - Mean: $91,765,576
   - Median: $19,489,314
   - Min: $1
   - Max: $2,923,706,026
   

📈 ROI Statistics:
   - Mean: 49473.4%
   - Median: 95.4%
         """)
st.write("""
         
## Budget Analysis
         """)
image9_path = "Images/output9.png"
image9 = Image.open(image9_path)
st.image(image9, caption="Budget Distribution Analysis", use_container_width=True)

st.write("""
         
## Relation Between Financial Data and Ratings 
         """)
image10_path = "Images/output10.png"
image10 = Image.open(image10_path)
st.image(image10, caption="Financial Data vs Ratings", use_container_width=True)

image11_path = "Images/output11.png"
image11 = Image.open(image11_path)
st.image(image11, caption="(Budget & Revenue) vs Ratings", use_container_width=True)


# =====================================
# 🎬 Highest Budget Movies (Sample)
# =====================================
st.header(" Highest Budget Movies")

# Create the DataFrame
data = {
    "primaryTitle": [
        "Jurassic World: Dominion",
        "Star Wars: Episode IX - The Rise of Skywalker",
        "Star Wars: Episode IX - The Rise of Skywalker",
        "Mission: Impossible - The Final Reckoning",
        "Pirates of the Caribbean: On Stranger Tides",
        "Pirates of the Caribbean: On Stranger Tides",
        "Avengers: Age of Ultron",
        "Avengers: Age of Ultron",
        "Avengers: Endgame",
        "Avengers: Endgame"
    ],
    "startYear": [2022, 2019, 2019, 2025, 2011, 2011, 2015, 2015, 2019, 2019],
    "budget": ["$583.9M", "$416.0M", "$416.0M", "$400.0M", "$379.0M", "$379.0M", "$365.0M", "$365.0M", "$356.0M", "$356.0M"],
    "revenue": ["$1004.0M", "$1074.1M", "$1074.1M", "$598.1M", "$1046.7M", "$1046.7M", "$1405.4M", "$1405.4M", "$2799.4M", "$2799.4M"],
    "averageRating": [5.6, 6.4, 6.4, 7.2, 6.6, 6.6, 7.3, 7.3, 8.4, 8.4]
}

df = pd.DataFrame(data)

# Optional: remove duplicates
df = df.drop_duplicates()

# Sort by budget (descending)
df["budget_numeric"] = df["budget"].str.replace("[$M]", "", regex=True).astype(float)
df = df.sort_values(by="budget_numeric", ascending=False).drop(columns="budget_numeric")

# Display the DataFrame
st.dataframe(df, use_container_width=True)

# Optional: Summary text
st.markdown("""
This table presents some of the **highest-budget movies** in the dataset, including their
release year, production cost, box office revenue, and IMDb average rating.
""")

# =====================================
# 💰 Top 10 Highest Revenue Movies
# =====================================
st.header(" Top 10 Highest Revenue Movies")

# Create the DataFrame
data = {
    "primaryTitle": [
        "Avatar",
        "Avatar",
        "Avengers: Endgame",
        "Avengers: Endgame",
        "Avatar: The Way of Water",
        "Avatar: The Way of Water",
        "Titanic",
        "Titanic",
        "How Could I Live Without You?",
        "Ne Zha 2"
    ],
    "startYear": [2009, 2009, 2019, 2019, 2022, 2022, 1997, 1997, 2024, 2025],
    "budget": ["$237.0M", "$237.0M", "$356.0M", "$356.0M", "$350.0M", "$350.0M", "$200.0M", "$200.0M", "$70.0M", "$80.0M"],
    "revenue": ["$2923.7M", "$2923.7M", "$2799.4M", "$2799.4M", "$2330.2M", "$2330.2M", "$2264.2M", "$2264.2M", "$2200.0M", "$2150.0M"],
    "averageRating": [7.9, 7.9, 8.4, 8.4, 7.5, 7.5, 7.9, 7.9, 6.9, 8.0]
}

df = pd.DataFrame(data)

# Remove duplicates
df = df.drop_duplicates()

# Sort by revenue descending
df["revenue_numeric"] = df["revenue"].str.replace("[$M]", "", regex=True).astype(float)
df = df.sort_values(by="revenue_numeric", ascending=False).drop(columns="revenue_numeric")

# Display DataFrame
st.dataframe(df, use_container_width=True)

# Optional: summary text
st.markdown("""
This table highlights the **top 10 highest-grossing movies** worldwide, showing their 
release year, production budget, total box office revenue, and IMDb rating.
""")