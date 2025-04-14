# 🌤️ MLH API WEEK - CONNECT TWO APIS

This Python script fetches **air pollution data** for a specific location (Chennai, by default) using the **OpenWeatherMap API**, formats it into a readable message, and sends it to a **Telegram chat** using a bot.

---

## 🚀 Features

- 📡 Pulls real-time air quality data from OpenWeatherMap
- 🤖 Sends formatted AQI and pollutant data to a Telegram chat
- 🌐 Uses coordinates (lat/lon) to localize data
- 🕒 Includes human-readable timestamp

---

## 🛠️ Requirements

- Python 3.7+
- Telegram bot token and chat ID
- OpenWeatherMap API key

Install required package:

```bash
pip install python-dotenv requests
```

---

## 🔐 Environment Variables

Create a `.env` file in the same folder as your script with the following:

```env
OPENWEATHER=your_openweathermap_api_key
TELEGRAM_TOKEN=your_telegram_bot_token
CHAT_ID=your_telegram_chat_id
```

---

## 🧪 How to Run

```bash
python weatherReportToTelegram.py
```

After running the script, you’ll receive a message like this in your Telegram:

```
Air Quality Update 🌍:
- Overall AQI: 2
- Components:
  • CO (Carbon Monoxide): 201.94 µg/m³
  • NO (Nitric Oxide): 0.0 µg/m³
  ...
Timestamp: 2025-04-14 08:30:00
```

---

## 📍 Coordinates Used

Currently hardcoded to Chennai:
- Latitude: `13.0843`
- Longitude: `80.2705`

To change location, modify these two lines in `weatherReportToTelegram.py`:
```python
lat = 13.0843
lon = 80.2705
```

---

## 📌 Notes

- AQI values range from 1 (Good) to 5 (Very Poor) per OpenWeatherMap's standard.
- Make sure to send a message to your bot first before accessing `getUpdates` to retrieve the `chat_id`.
