import streamlit as st
import pickle
from pathlib import Path
from recommend import recommend

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

# ==========================================
# Project Paths
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

MOVIE_PATH = BASE_DIR / "models" / "movie_list.pkl"

# ==========================================
# Load Movie List
# ==========================================

with open(MOVIE_PATH, "rb") as file:
    movies = pickle.load(file)

# ==========================================
# UI
# ==========================================

st.title("🎬 Movie Recommendation System")

st.write("Select a movie and get 5 similar movie recommendations.")

st.divider()

selected_movie = st.selectbox(
    "Choose a Movie",
    movies["title"].values
)

if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")

    for movie in recommendations:
        st.write(f"🎥 {movie}")