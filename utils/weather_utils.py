def check_for_alerts(weather_data):
    try:
        wind_speed = weather_data['wind']['speed']
        if wind_speed > 20:  # Example threshold
            return "High wind alert!"
        return None
    except KeyError:
        return None  # No wind data available

def ai_weather_analysis(weather_data):
    if weather_data['main']['temp'] > 30:
        return "It's going to be hot! Consider staying indoors."
    return "Weather conditions are favorable."

def activity_recommendation(weather_data):
    if weather_data['weather'][0]['main'] == 'Clear':
        return "Great day for a hike!"
    elif weather_data['weather'][0]['main'] == 'Rain':
        return "Perfect day to visit a museum."
    return "Check out local events!"