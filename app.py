from flask import Flask, render_template, request, jsonify
from datetime import datetime
import yfinance as yf
from prophet import Prophet
import plotly
import plotly.graph_objs as go
import json
from datetime import datetime, timedelta

app = Flask(__name__)

# Fetch, train, and forecast functions
def fetch_stock_data(ticker, days=365*5):
    end = datetime.now()
    start = end - timedelta(days=days)
    data = yf.download(ticker, start=start, interval='1d')
    return data

def prepare_data(data):
    df = data[['Close']].reset_index()
    df.columns = ['ds', 'y']
    return df

def train_prophet_model(data):
    model = Prophet(daily_seasonality=True, yearly_seasonality=True, weekly_seasonality=True,
                    changepoint_prior_scale=0.05, seasonality_prior_scale=10)
    model.add_country_holidays(country_name='US')
    model.fit(data)
    return model

def make_predictions(model, periods):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast

# API route to fetch predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    ticker = data.get('ticker')
    prediction_duration = data.get('duration')

    # Step duration
    steps = {'1 week': 7, '2 weeks': 14, '1 month': 30, '3 months': 90, '6 months': 180, '1 year': 365}
    forecast_steps = steps[prediction_duration]

    stock_data = fetch_stock_data(ticker)
    df = prepare_data(stock_data)
    model = train_prophet_model(df)
    forecast = make_predictions(model, forecast_steps)

    # Plotting forecast
    fig = go.Figure()
    future_forecast = forecast[forecast['ds'] > datetime.now()]
    fig.add_trace(go.Scatter(x=future_forecast['ds'], y=future_forecast['yhat'], mode='lines', name='Forecast'))
    fig.add_trace(go.Scatter(x=future_forecast['ds'], y=future_forecast['yhat_upper'], fill=None, mode='lines',
                             line_color='rgba(0,0,255,0.2)', name='Upper Bound'))
    fig.add_trace(go.Scatter(x=future_forecast['ds'], y=future_forecast['yhat_lower'], fill='tonexty', mode='lines',
                             line_color='rgba(0,0,255,0.2)', name='Lower Bound'))

    fig.update_layout(title=f'{ticker} Stock Price Prediction for {prediction_duration}',
                      xaxis_title='Date', yaxis_title='Price', template='plotly_white')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return jsonify(graphJSON=graphJSON)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5050)

