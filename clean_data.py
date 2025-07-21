import pandas as pd

df_raw = pd.read_csv("chart.csv", sep=';')

df_clean = df_raw[['timeClose', 'close']].copy()

df_clean.rename(columns={
    'timeClose': 'ds',
    'close': 'y'
}, inplace=True)

df_clean['ds'] = pd.to_datetime(df_clean['ds']).dt.date

df_clean.sort_values('ds', inplace=True)

df_clean.reset_index(drop=True, inplace=True)

df_clean.to_csv("cleaned_chart.csv", index=False)

