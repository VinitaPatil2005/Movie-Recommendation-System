import pickle
from pathlib import Path

# ==========================================
# Project Paths
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

MOVIE_PATH = BASE_DIR / "models" / "movie_list.pkl"
SIMILARITY_PATH = BASE_DIR / "models" / "similarity.pkl"

# ==========================================
# Load Saved Files
# ==========================================

with open(MOVIE_PATH, "rb") as file:
    movies = pickle.load(file)

with open(SIMILARITY_PATH, "rb") as file:
    similarity = pickle.load(file)

# ==========================================
# Recommendation Function
# ==========================================

def recommend(movie):

    movie_index = movies[movies["title"] == movie].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for item in movie_list:
        recommendations.append(
            movies.iloc[item[0]].title
        )

    return recommendations