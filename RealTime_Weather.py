import streamlit as st
import requests


def get_weather(city):
    api_key = "147db50c298b97fd3730a669e8b57d89"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data["cod"] == 200:
            return data
        else:
            return None
    except requests.exceptions.RequestException:
        return None


def get_weather_emoji(weather_id):
    if 200 <= weather_id <= 232:
        return "⛈️"
    elif 300 <= weather_id <= 321:
        return "🌦️"
    elif 500 <= weather_id <= 531:
        return "🌧️"
    elif 600 <= weather_id <= 622:
        return "❄️"
    elif 701 <= weather_id <= 741:
        return "🌫️"
    elif weather_id == 762:
        return "🌋"
    elif weather_id == 771:
        return "💨"
    elif weather_id == 781:
        return "🌪️"
    elif weather_id == 800:
        return "🌞"
    elif 801 <= weather_id <= 804:
        return "☁️"
    else:
        return "❓"


st.set_page_config(page_title="Real Time Weather App", page_icon="🌤️", layout="centered")

st.title("🌤️ Real Time Weather App")
st.markdown("🌤️ **Real-Time Weather App: Get Live Weather Updates Instantly ⏳ | Accurate Forecasts, Interactive UI & Emoji-Based Weather Insights! 🌎❄️☀️**")

st.markdown("<h3 style='font-size: 24px; font-weight: bold;'>Enter City Name:</h3>",
            unsafe_allow_html=True)
city = st.text_input("", placeholder="Type city name here...")

st.markdown("""
    <style>
        .stButton > button {
            padding: 15px 30px;  /* Add padding (vertical and horizontal) */
            font-size: 18px;  /* Adjust font size */
            font-weight: bold;  /* Bold text */
            background-color: #4CAF50;  /* Green background color */
            color: white;  /* White text color */
            border: none;
            border-radius: 5px;  /* Rounded corners */
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #45a049;  /* Darker green when hovering */
        }
    </style>
""", unsafe_allow_html=True)

if st.button("Get Weather", help="Click to fetch live weather data 🌍"):
    weather_data = get_weather(city)

    if weather_data:
        temperature = weather_data["main"]["temp"]
        weather_id = weather_data["weather"][0]["id"]
        weather_description = weather_data["weather"][0]["description"].capitalize()
        emoji = get_weather_emoji(weather_id)

        st.markdown(f"<h1 style='text-align: center;'>{temperature:.0f}°C {emoji}</h1>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align: center; color: #4A90E2;'>{weather_description}</h2>", unsafe_allow_html=True)
    else:
        st.error("⚠️ Could not retrieve weather data. Please check the city name and try again.")

st.markdown("---")
st.markdown("<p style='text-align: center;'>Created with ❤️ by Mulukutla Sai Krishna</p>", unsafe_allow_html=True)
