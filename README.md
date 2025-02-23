# Movies Recommendation System
A simple and interactive Movies Recommender System built using Streamlit and Python. This project suggests movies based on content-based filtering, making use of a dataset and similarity measures to provide personalized recommendations.

## Project Flow
- Generates recommendations using a content-based filtering approach.
- prepro.ipynb Handles data preprocessing for the movie dataset.
- Computes similarity scores based on content features.
- Saves the processed data as movie_list.pkl and similarity.pkl.
- app.py Loads the movie dataset (movie_list.pkl) and similarity matrix (similarity.pkl).
- Used Streamlit to create an interactive UI.
- Fetches movie posters using TMDb API.

## Demo

- check : https://shorturl.at/MGqXX


## Future improvements 
- Filter option that user can preference the Recommendation. Users may want to filter recommendations based on genre, cast, crew, release year, or language.
