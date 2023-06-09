import pickle
import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="AJ_Song_Recommender_System",
    page_icon=":rocket:",
    layout="wide",
    initial_sidebar_state="expanded",
)


def recommended_song_details(song):
    index = songs[songs['Song_Name'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_song_names = []
    recommended_song_image = []
    recommended_song_movie_name = []
    recommended_song_playlist_url = []
    l=[]
    for i in distances[1:15]:
        l.append((i[0], songs.iloc[i[0]].User_Rating))
    song_list = sorted(l, reverse=True, key=lambda x: x[1])
    for i in song_list[0:9]:
        recommended_song_names.append(songs.iloc[i[0]].Song_Name)
        recommended_song_image.append(songs.iloc[i[0]].Song_Image)
        recommended_song_movie_name.append(songs.iloc[i[0]].Movie_Name)
        recommended_song_playlist_url.append(songs.iloc[i[0]].Song_Playlist)
    return recommended_song_names,recommended_song_image,recommended_song_movie_name,recommended_song_playlist_url
st.header('Song Recommender System')

#songs = pickle.load(open('song.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
songs = pd.read_pickle('song.pkl')
similarity = pd.read_pickle('similarity.pkl')
song_list= songs['Song_Name'].values
Selected_Songs = st.selectbox("Type or select a song from the dropdown",song_list
)

if st.button('Show Recommendation'):
    recommended_song_names,recommended_song_image,recommended_song_movie_name,recommended_song_playlist_url= recommended_song_details(Selected_Songs)
    col1, col2, col3 =st.columns(3,gap="large")
    with col1:
        st.image(recommended_song_image[0],width=160)
        st.text(recommended_song_names[0])
        st.text(recommended_song_movie_name[0])
        st.markdown(recommended_song_playlist_url[0])
    with col2:
        st.image(recommended_song_image[1],width=160)
        st.text(recommended_song_names[1])
        st.text(recommended_song_movie_name[1])
        st.markdown(recommended_song_playlist_url[1])
    with col3:
        st.image(recommended_song_image[2],width=160)
        st.text(recommended_song_names[2])
        st.text(recommended_song_movie_name[2])
        st.markdown(recommended_song_playlist_url[2])
    col4, col5, col6=st.columns(3,gap="large")
    with col4:
        st.image(recommended_song_image[3],width=160)
        st.text(recommended_song_names[3])
        st.text(recommended_song_movie_name[3])
        st.markdown(recommended_song_playlist_url[3])
    with col5:
        st.image(recommended_song_image[4],width=160)
        st.text(recommended_song_names[4])
        st.text(recommended_song_movie_name[4])
        st.markdown(recommended_song_playlist_url[4])
    with col6:
        st.image(recommended_song_image[5],width=160)
        st.text(recommended_song_names[5])
        st.text(recommended_song_movie_name[5])
        st.markdown(recommended_song_playlist_url[5])
    col7, col8, col9 = st.columns(3, gap="large")
    with col7:
        st.image(recommended_song_image[6],width=160)
        st.text(recommended_song_names[6])
        st.text(recommended_song_movie_name[6])
        st.markdown(recommended_song_playlist_url[6])
    with col8:
        st.image(recommended_song_image[7],width=160)
        st.text(recommended_song_names[7])
        st.text(recommended_song_movie_name[7])
        st.markdown(recommended_song_playlist_url[7])
    with col9:
        st.image(recommended_song_image[8],width=160)
        st.text(recommended_song_names[8])
        st.text(recommended_song_movie_name[8])
        st.markdown(recommended_song_playlist_url[8])