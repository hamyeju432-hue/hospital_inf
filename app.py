import folium
import urllib.request
import urllib.parse
import streamlit as st 
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

Korea_Map = folium.Map(location=[36.00, 127.25], zoom_start=7)

file_url = "https://raw.githubusercontent.com/hamyeju432-hue/hospital_inf/refs/heads/main/병원정보.txt"

safe_url = urllib.parse.quote(file_url, safe=":/?=")

response = urllib.request.urlopen(safe_url)

header = response.readline().decode('utf-8')

hp = response.readline().decode('utf-8')

while hp:

    parts = hp.strip().split("*")

    if len(parts) == 5:
        hospital, region, number, x, y = parts
        hospital = hospital.strip()
        region = region.strip()
        number = number.strip()
        x = float(x.strip())
        y = float(y.strip())

        text = hospital + "<br>" + region + "<br>" + number  
        popup_window = folium.Popup(text, max_width=300) 

        folium.CircleMarker(
            location=[y, x], 
            radius=4,
            color="#1f77b4",
            fill=True,
            fill_color="#1f77b4",
            fill_opacity=0.7,
            popup=popup_window,
        ).add_to(Korea_Map)

    hp = response.readline().decode("utf-8")

response.close()

st_folium(
    Korea_Map,
    use_container_width=True,
    height=750,
    returned_objects=[],  # 💡 지도를 움직여도 서버에 데이터를 다시 보내지 않도록 차단!
)
