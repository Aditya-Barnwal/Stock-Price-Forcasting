# Stock Price Prediction Website

A professional web application that provides stock price forecasts using Facebook's Prophet algorithm. The application features an intuitive user interface with dark mode support and interactive charts powered by Plotly.

## Features

- Real-time stock data fetching using yfinance
- Advanced time series forecasting using Facebook Prophet
- Interactive price prediction charts with Plotly
- Customizable prediction durations (1 week to 1 year)
- Dark mode support
- Responsive design
- Confidence intervals for predictions
- Performance metrics calculation

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **CSS Framework**: Tailwind CSS
- **Libraries**:
  - Prophet (Facebook's time series forecasting)
  - yfinance (Yahoo Finance data)
  - Plotly (Interactive charts)
  - NumPy (Numerical computations)
  - scikit-learn (Performance metrics)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/stock-prediction-website.git
cd stock-prediction-website
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install flask prophet yfinance plotly numpy scikit-learn
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and navigate to:
```
http://localhost:5050
```

## Usage

1. Enter a valid stock ticker symbol (e.g., AAPL, GOOGL, MSFT)
2. Select your desired prediction duration from the dropdown
3. Click "Get Prediction" to generate the forecast
4. View the interactive chart showing the predicted stock prices with confidence intervals

## Project Structure

```
├── app.py              # Main Flask application
├── templates
│   └── index.html     # Main HTML template
├── static
│   └── styles.css     # Custom CSS styles
└── performance.py     # Performance metrics calculation
```

## Performance Metrics

The application calculates several performance metrics to evaluate prediction accuracy:
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- Confidence Intervals (95%)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details

## Acknowledgments

- Facebook Prophet team for the forecasting algorithm
- Yahoo Finance for providing stock data
- Plotly team for the interactive visualization library
- Tailwind CSS team for the styling framework

## Disclaimer

This tool is for educational purposes only. Stock predictions are based on historical data and should not be used as the sole basis for investment decisions. Always do your own research and consider consulting with a financial advisor before making investment decisions.
