from dotenv import load_dotenv
import os
import requests as r
import streamlit as st
load_dotenv()
api_key = os.getenv("OMDB_API_KEY")

def buscar_filme(Titulo):
    url = f"http://www.omdbapi.com/?apikey={api_key}&s={Titulo}"
    response = r.get(url)
    if response.status_code == 200:
        response = response.json()
        if response.get("Response") == "True":
            filmes = response["Search"]
            for f in filmes:
                detalhe_url = f"http://www.omdbapi.com/?apikey={api_key}&i={f['imdbID']}&plot=full"
                detalhe = r.get(detalhe_url).json()
                
                st.markdown("---") 
                col1, col2 = st.columns([1,2])
                with col1:
                    poster_url = detalhe.get("Poster")
                    if poster_url and poster_url != "N/A":
                        st.image(poster_url)
                    else:
                        st.write("Poster não disponível")
                with col2:
                    st.write("Title:", detalhe["Title"])
                    st.write("Year:", detalhe["Year"])
                    st.write("Plot:", detalhe["Plot"])
                    st.write("Genre:", detalhe["Genre"])
                    st.write("Director:", detalhe["Director"])
                    st.write("Actors:", detalhe["Actors"])
                    st.write("Runtime:", detalhe["Runtime"])
                    st.write("IMDB Rating:", detalhe["imdbRating"])
                    st.write("Votes:", detalhe["imdbVotes"])
                    st.write("Type:", detalhe["Type"])
        else:
            st.error("Filme não encontrado!")
    else:
        st.error("Falha na requisição")