import pickle
import streamlit as st
import requests


def fetch_movie_details(movie_id):
    api_key = "8265bd1679663a7ea12ac168da84d2e8"  
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    response = requests.get(url)
    
    if response.status_code != 200:
        return None  
    
    data = response.json()
    
    return {
        "title": data.get("title", "Unknown"),
        "poster": f"https://image.tmdb.org/t/p/w500{data.get('poster_path', '')}",
        "overview": data.get("overview", "No description available."),
        "rating": data.get("vote_average", "N/A"),
        "genres": ", ".join([genre["name"] for genre in data.get("genres", [])])
    }


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommendations = []
    for i in distances[1:6]:  
        movie_id = movies.iloc[i[0]].movie_id
        movie_details = fetch_movie_details(movie_id)
        
        if movie_details:
            recommendations.append(movie_details)
    
    return recommendations

st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")
st.title("🎬 Movies Recommender System")
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("🔍 Type or select a movie", movie_list)

if st.button('Show Recommendations'):
    recommendations = recommend(selected_movie)
    
    if recommendations:
        cols = st.columns(5)  
        for col, movie in zip(cols, recommendations):
            with col:
                st.image(movie["poster"], use_container_width=True)
                st.markdown(f"**{movie['title']}**")
                st.write(f"⭐ {movie['rating']} | {movie['genres']}")
                st.caption(movie["overview"][:150] + "...")  
    else:
        st.warning("No recommendations found! Try another movie.")

