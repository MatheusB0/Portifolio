import requests
import streamlit  as st


def Busca_Poke(poke_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{poke_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        col1, col2 = st.columns([1,2])
        with col1:
            st.image(data["sprites"]["front_default"]) 
        with col2:
            st.write("**Nome:**", data["name"].title())
            st.write("**ID:**", data["id"])
            st.write("**Tipos:**", ", ".join([t["type"]["name"].title() for t in data["types"]]))
            st.write("**Habilidades:**", ", ".join([h["ability"]["name"].title() for h in data["abilities"]]))
            st.write("**Stats:**")
            for stat in data["stats"]:
                st.write(f"{stat['stat']['name'].title()}: {stat['base_stat']}")
    else:
        st.error("Pokémon não encontrado!")
   