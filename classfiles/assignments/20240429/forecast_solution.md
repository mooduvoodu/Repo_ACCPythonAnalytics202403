
### Solution Code



```python
import pandas as pd
from darts import TimeSeries
from darts.models import ARIMA, ExponentialSmoothing
from darts.metrics import mae, rmse
import matplotlib.pyplot as plt


# Load data
data = pd.read_csv('/workspaces/Repo_ACCPythonAnalytics202403/kclubb/stockhistory/DIS.csv')
data['datetime'] = pd.to_datetime(data['t'], unit='ms')
data.set_index('datetime', inplace=True)

# Plotting the data
data['vw'].plot(title='Volume Weighted Average Price Over Time')

# Preparing the time series for modeling
series = TimeSeries.from_dataframe(data, 'datetime', 'vw')

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
```

### Explanation of the Plotting Code:
1. **Initial Plotting of Data:** The initial plot provides a view of the entire volume-weighted average price over time, helping to understand the overall trend and fluctuations.
2. **Plotting Forecasts and Actual Data:**
   - The `train.plot()` and `test.plot()` functions plot the training and testing data, respectively.
   - The `prediction_arima.plot()` and `prediction_exp_smoothing.plot()` functions add the forecasted values from the ARIMA and Exponential Smoothing models to the plot.
   - `plt.legend()` adds a legend to distinguish between different lines on the plot.
   - `plt.title()` sets a title for the plot.

