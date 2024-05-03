import pandas as pd
from darts import TimeSeries
from darts.models import ARIMA, ExponentialSmoothing
from darts.metrics import mae, rmse
import matplotlib.pyplot as plt


# Load data
data = pd.read_csv('/workspaces/Repo_ACCPythonAnalytics202403/kclubb/stockhistory/DIS.csv')
data['datetime_ts'] = pd.to_datetime(data['t'], unit='ms')

data.set_index('datetime_ts', inplace=True)

# Plotting the data
data['vw'].plot(title='Volume Weighted Average Price Over Time')

display(data)

# Preparing the time series for modeling
series = TimeSeries.from_dataframe(data, value_cols = 'vw', freq='10s')

# Splitting the data
train, test = series.split_before(0.8)

# Modeling
model_arima = ARIMA()
model_exp_smoothing = ExponentialSmoothing()

model_arima.fit(train)
model_exp_smoothing.fit(train)

# Forecasting
prediction_arima = model_arima.predict(len(test))
prediction_exp_smoothing = model_exp_smoothing.predict(len(test))

# Plotting forecasts and actual data
plt.figure(figsize=(10, 6))
train.plot(label='Training data')
test.plot(label='Testing data')
prediction_arima.plot(label='ARIMA Predictions')
prediction_exp_smoothing.plot(label='Exponential Smoothing Predictions')
plt.title('Forecast vs Actuals')
plt.legend()
plt.show()

# Performance Metrics
mae_arima = mae(test, prediction_arima)
rmse_arima = rmse(test, prediction_arima)
mae_exp_smoothing = mae(test, prediction_exp_smoothing)
rmse_exp_smoothing = rmse(test, prediction_exp_smoothing)

# Output results
print(f"ARIMA MAE: {mae_arima}, RMSE: {rmse_arima}")
print(f"Exponential Smoothing MAE: {mae_exp_smoothing}, RMSE: {rmse_exp_smoothing}")