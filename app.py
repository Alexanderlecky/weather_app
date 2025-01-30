from flask import Flask, request, render_template
from utils.data_fetcher import fetch_weather_data
from utils.weather_utils import check_for_alerts, ai_weather_analysis, activity_recommendation

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        weather_data = fetch_weather_data('your_api_key', location)
        alert = check_for_alerts(weather_data)
        analysis = ai_weather_analysis(weather_data)
        recommendation = activity_recommendation(weather_data)
        return render_template('weather.html', data=weather_data, alert=alert, analysis=analysis, recommendation=recommendation)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)