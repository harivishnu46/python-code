import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

# Load time series data from a CSV file
data = pd.read_csv('time_series_data.csv', parse_dates=['date_column'], index_col='date_column')

# Handle missing values
data.dropna(inplace=True)

# Plot time series data
plt.figure(figsize=(10, 6))
plt.plot(data.index, data['value_column'], label='Original Data')
plt.title('Time Series Data')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.show()

# Resample data to a specific frequency (e.g., monthly)
data_resampled = data.resample('M').mean()

# Decompose time series data into trend, seasonal, and residual components
decomposition = seasonal_decompose(data_resampled['value_column'], model='additive')
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

# Plot decomposed components
plt.figure(figsize=(10, 8))
plt.subplot(411)
plt.plot(data_resampled['value_column'], label='Original')
plt.legend(loc='upper left')
plt.subplot(412)
plt.plot(trend, label='Trend')
plt.legend(loc='upper left')
plt.subplot(413)
plt.plot(seasonal, label='Seasonal')
plt.legend(loc='upper left')
plt.subplot(414)
plt.plot(residual, label='Residual')
plt.legend(loc='upper left')
plt.tight_layout()
plt.show()
