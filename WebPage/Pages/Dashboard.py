import streamlit as st
from PIL import Image

# =====================================
# 🎬 MOVIE RATING PREDICTION PROJECT
# =====================================
st.title("🎥 Exploratory Data Analysis (EDA)")
st.write("""
This page provides an **in-depth exploratory data analysis (EDA)** for the Movie Rating Prediction project.
""")

st.markdown("### 🔍 Key Questions We'll Answer")
st.markdown("""
- 🎭 **Genre Insights:** Which genres are most popular and highest rated?  
- 🎬 **Director Analysis:** Who are the “guarantee” directors? Career ups and downs?  
- 👥 **Actor Influence:** Which actors most impact ratings? Best collaborations?  
- 🧮 **Feature Importance:** What factors most strongly predict ratings?  
- ⏳ **Temporal Patterns:** How have movies and ratings evolved over time?  
- 💡 **Creative Insights:** Runtime effects, voting patterns, outlier analysis  
""")

st.markdown("### 📘 Analysis Scope")
st.markdown("""
- **Dataset:** IMDb + MovieLens data  
- **Focus:** Feature discovery for rating prediction  
- **Approach:** Statistical analysis + creative exploration  
- **Output:** Actionable insights for model building  
""")

# =====================================
# 🧾 DATA OVERVIEW
# =====================================
st.header("🧩 Steps We Followed")

st.subheader("📂 Data Load and Setup")
st.markdown("""
- 🎞️ Movies with ratings: **138,032**  
- 👤 People records: **14,745,597**  
- 🎬 Crew records: **726,969**  
- 🎭 Principal records: **8,374,077**  
- 🌍 Regional records: **3,573,412**  
""")

st.markdown("### 📊 Dataset Overview")
st.markdown("""
- 🎬 **Total movies:** 138,032  
- ⭐ **Average rating:** 5.91  
- 📅 **Year range:** 1903 - 2025  
- 🕒 **Runtime range:** 11 - 580 minutes  
""")

# =====================================
# 🎭 GENRE ANALYSIS
# =====================================
st.header("🎭 Deep Genre Analysis — What Makes Movies Popular?")
st.subheader("📈 Comprehensive Genre Analysis")
st.markdown("""
**Most popular genre:** Drama (72,298 movies)

**Top 5 genres by movie count:**
1. 🎭 Drama — 72,298 movies (avg rating: 6.1)  
2. 😂 Comedy — 42,295 movies (avg rating: 5.8)  
3. 💞 Romance — 20,006 movies (avg rating: 6.1)  
4. 💥 Action — 18,399 movies (avg rating: 5.5)  
5. 🕵️ Crime — 17,066 movies (avg rating: 5.9)
""")

image1 = Image.open("Images/output1.png")
st.image(image1, caption="Comprehensive Genre Analysis", use_container_width=True)

# =====================================
# 🎬 DIRECTOR ANALYSIS
# =====================================
st.header("🎬 Director Performance Analysis")
st.markdown("""
✅ Found crew data for **138,032 movies**  
📊 Analyzed **14,261 directors** with ≥3 movies  
📝 Created name mapping for **14,745,597 people**  
""")

image2 = Image.open("Images/output2.png")
st.image(image2, caption="Director Performance Analysis", use_container_width=True)

st.markdown("### 🏆 Top 5 “Guarantee” Directors")
st.markdown("""
1. **K.R. Devmani** — Avg Rating: 9.10 | Consistency: 0.668 | Movies: 3 | Guarantee Score: 4.26  
2. **Ludmil Staikov** — Avg Rating: 8.73 | Consistency: 0.830 | Movies: 3 | Guarantee Score: 4.26  
3. **Christopher Nolan** — Avg Rating: 8.17 | Consistency: 0.628 | Movies: 12 | Guarantee Score: 4.22  
4. **William Higgins** — Avg Rating: 8.63 | Consistency: 0.809 | Movies: 3 | Guarantee Score: 4.20  
""")

st.markdown("""
**Additional Insights:**
- 🎞️ 2,829 directors with long careers (>23 years) — avg rating **6.19**  
- 🧠 2,827 highly productive directors (>0.7 movies/year) — avg rating **5.62**
""")

# =====================================
# 🎨 CREATIVE INSIGHTS
# =====================================
st.header("🎨 Creative Insights — Runtime, Age & Voting Patterns")

image3 = Image.open("Images/output3.png")
st.image(image3, caption="Creative Insights", use_container_width=True)

st.markdown("""
#### 🕒 Runtime Insights
- Optimal runtime category: **Epic (>150 min)**  
- Runtime–rating correlation: **0.203**

#### 📅 Age Effect
- 2020s avg rating: **5.82**  
- 1900s avg rating: **6.12**  
- Rating change over time: **-0.30**

#### 🗳️ Voting Patterns
- Vote–rating correlation: **0.133**  
- High-vote (top 10%) avg rating: **6.56**  
- Regular movies avg rating: **5.84**

#### 🎯 Outlier Analysis
- **Top 5% (Exceptional movies):**  
  Avg runtime: 114 min | Avg votes: 45,614  
- **Bottom 5% (Poor movies):**  
  Avg runtime: 91 min | Avg votes: 1,357  

#### 🎭 Genre–Runtime Patterns
- Action — Avg runtime: 107 min | Avg rating: 5.53  
- Drama — Avg runtime: 103 min | Avg rating: 6.14  

#### 🔑 Key Findings
✅ Runtime and votes correlate with ratings  
✅ Ratings evolve over decades  
✅ Outlier movies have distinct characteristics  
✅ Genre-specific runtime and quality patterns exist  
""")

# =====================================
# 📊 FEATURE IMPORTANCE
# =====================================
st.header("📊 Feature Importance Analysis — What Drives Ratings?")
image4 = Image.open("Images/output4.png")
st.image(image4, caption="Feature Importance Analysis", use_container_width=True)

st.markdown("""
#### 🧮 Statistically Significant Features (p < 0.05)
| Feature | Corr | p-value |
|:------------------|:------:|:--------:|
| genre_horror | -0.328 | 0.000000 |
| log_votes | +0.204 | 0.000000 |
| runtimeMinutes | +0.203 | 0.000000 |
| genre_drama | +0.188 | 0.000000 |
| runtime_squared | +0.179 | 0.000000 |
| genre_thriller | -0.163 | 0.000000 |
| genre_sci-fi | -0.140 | 0.000000 |
| numVotes | +0.133 | 0.000000 |
| startYear | -0.128 | 0.000000 |
| movie_age | +0.128 | 0.000000 |

#### 🎯 Most Consistent Predictors (Correlation + RF)
- genre_horror — Corr=-0.328 | RF=0.269  
- log_votes — Corr=+0.204 | RF=0.096  
- runtimeMinutes — Corr=+0.203 | RF=0.064  
- runtime_squared — Corr=+0.179 | RF=0.064  
- numVotes — Corr=+0.133 | RF=0.094  
- genre_thriller — Corr=-0.163 | RF=0.058  
- genre_drama — Corr=+0.188 | RF=0.053  
- genre_action — Corr=-0.117 | RF=0.069  

#### 🤖 Model Performance Check
**Random Forest R²:** 0.404  
This suggests moderate predictability and a complex rating landscape.
""")

# =====================================
# ✍️ WRITER/DIRECTOR ANALYSIS
# =====================================
st.header("✍️ Writer/Director Analysis — The Auteurs")

image5 = Image.open("Images/output5.png")
st.image(image5, caption="Writer/Director Analysis", use_container_width=True)

st.markdown("""
#### 📊 Detailed Statistics
- Avg movies per writer/director: **11.2**  
- Avg rating: **7.26**  
- Avg career span: **28.3 years**  
- Total votes (top 30): **140,239,312**

#### 🌟 Notable Patterns
- 🏆 Most prolific: **Woody Allen** — 46 movies  
- ⭐ Highest rated: **Frank Darabont** — Avg 8.33  
- 📈 Most popular: **Christopher Nolan** — 17,265,707 votes  
- ⏰ Longest career: **Francis Ford Coppola** — 50 years (1974–2024)
""")

# =====================================
# 🌍 REGIONAL ANALYSIS
# =====================================
st.header("🌍 Regional & Language Distribution Analysis")

image6 = Image.open("Images/output6.png")
st.image(image6, caption="Regional and Language Distribution Analysis", use_container_width=True)
