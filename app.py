import streamlit as st
import requests

API_KEY = 'e4d158133ada83dea4723f4d5e2ecbee'
BASE_URL = 'https://api.themoviedb.org/3/search/movie'

def search_movies(query):
    params = {
        'query': query,
        'api_key': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

def main():
    st.title("Movie Search App")

    search_query = st.text_input("Enter the movie name:")
    if st.button("Search"):
        if search_query:
            movie_data = search_movies(search_query)
            if 'results' in movie_data and movie_data['results']:
                movie = movie_data['results'][0]

                st.subheader(movie['title'])
                st.image(f"https://image.tmdb.org/t/p/w500/{movie['poster_path']}", caption=movie['title'], use_column_width=True)
                st.write(f"Release Date: {movie['release_date']}")
                st.write(f"Overview: {movie['overview']}")
                st.write(f"Popularity: {movie['popularity']}")
                st.write(f"Vote Average: {movie['vote_average']}")
            else:
                st.error("No movies found with that name.")
        else:
            st.warning("Please enter a movie name to search.")

if __name__ == "__main__":
    main()
