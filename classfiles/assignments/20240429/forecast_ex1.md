### Data Stock Data Review

Take one of the stock files you downloaded from Polygon.io. Run code to refresh and update since April 1. Make sure you install the Dart library by running the following command at the the terminal

#### pip install darts

The dataset contains several columns:
- `v`: Volume of trades
- `vw`: Volume weighted average price
- `o`: Opening price
- `c`: Closing price
- `h`: Highest price
- `l`: Lowest price
- `t`: Time in epoch milliseconds
- `n`: Number of trades

### Exercises

#### Exercise 1: Data Preparation
**Objective:** Convert the epoch time to a datetime format and set it as the index of the DataFrame.

**Explanation:** Time series data requires a time-based index to allow for time-based operations and plotting. Converting the epoch time to a human-readable format and indexing the DataFrame by this timestamp will enable efficient slicing and manipulation based on time.

#### Exercise 2: Data Visualization
**Objective:** Plot the volume-weighted average price (VWAP) over time.

**Explanation:** Visualizing the data helps in understanding the trends and patterns in the time series, such as cyclic behavior or anomalies, which is crucial before any modeling.

#### Exercise 3: Building Forecasting Models
**Objective:** Use the Darts library to fit at least two different types of forecasting models to the data.

**Explanation:** Forecasting models predict future values based on historical data. By employing different models, you can compare their performance and choose the best one for your specific data. We will use an ARIMA model and an Exponential Smoothing model.

#### Exercise 4: Model Validation and Performance Metrics
**Objective:** Split the data into training and testing sets, apply the models, and evaluate their performance using metrics like MAE and RMSE.

**Explanation:** Validating the models on a testing set that the model has not seen during training helps in assessing how well the model might perform on unseen data, which is critical for understanding the model's generalization ability.
