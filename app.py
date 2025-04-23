#To run the file use "streamlit run app.py" in terminal
import streamlit as st
import pickle
import pandas as pd

def recommend(movie_name):
    # Find the index of the selected movie
    movie_index = movies[movies['title'] == movie_name].index[0]
    # Get similarity scores for the selected movie
    movies_list = sorted(
        list(enumerate(similarity[movie_index])),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]  # Top 5 similar movies (excluding the selected movie)

    # Get movie titles for recommendations
    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# Load movie data
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

# Load similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app
st.title("Movie Recommender System")
selected_movie_name = st.selectbox(
    "Hey, what movie have you recently watched?",
    movies['title']
)

if st.button("Recommend"):
    # Get recommendations
    recommendations = recommend(selected_movie_name)
    # Display recommendations
    for movie in recommendations:
        st.write(movie)
