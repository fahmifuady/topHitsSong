import pandas as pd
import streamlit as st

c1, c2 = st.columns(2)

# menambahkan komponen teks
st.title("TOP HITS SONGS") 
st.subheader("listen now!")
st.markdown("""
Take a musical journey through time with this playlist featuring a collection of hit songs from each year. 
From the classic hits of the past to the chart-topping hits of today, this playlist has it all. 
Perfect for a nostalgic trip down memory lane or for discovering new songs you might have missed. 
Enjoy the best of each year's music all in one place
""")

# membaca data dari file csv yang telah dibuat sebelumnya
df = pd.read_csv("playlists.csv")
years = list(range(2000, 2023))

# menambahkan slider 
year_range = st.slider(label="Start Year", 
                       min_value=2000, 
                       max_value=2023, 
                       value=(2015, 2018))

# menambahkan tombol submit dam memberi logikanya
if st.button('Submit'):

    # memeriksa nilai slider
    if (int(year_range[0]) - int(year_range[1])) == 0:
        playlist_name = f"Top Hits Song : {year_range[0]}"
    else:
        playlist_name = f"Top Hits Song : {year_range[0]}-{year_range[1]}"

    # mengecek apakah nilai slider normal atau berlebihan
    if df[df['name'] == playlist_name].shape[0] > 0:
        playlist = df[df['name'] == playlist_name].to_dict(orient='records')[0]
    else:
        playlist = "Ooops, it looks like we didn't make that playlist yet. Playlists with a range of 1-5 years were created. Try again with a more narrow year range."

    # membuat link berdasarkan pilihan pengguna atau menampilkan error
    if isinstance(playlist, dict):
        link = f"### Your Spotify Playlist: [{playlist['name']}]({playlist['link']})"
        st.write(link, unsafe_allow_html=True)
    else:
        st.write(playlist)

# custom script
# st.write("""
# created by:
# - Muhammad Husni Fahmi Fuady
# - Putri
# """)
# import app_assets