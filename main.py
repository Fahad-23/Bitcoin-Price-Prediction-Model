import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_chart.csv")

df['ds'] = pd.to_datetime(df['ds'])

model = Prophet()

model.fit(df)

# Create a future DataFrame for the next 60 days
future = model.make_future_dataframe(periods=60)

# Make predictions
forecast = model.predict(future)

# Plot the forecast
model.plot(forecast)
plt.xlabel('Date')
plt.ylabel('Price of Bitcoin in USD')
plt.title('Forecast of Bitcoin Price')
plt.show()


