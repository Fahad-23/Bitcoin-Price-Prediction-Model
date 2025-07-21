import pandas as pd

# Step 1: Read the raw CSV file
df_raw = pd.read_csv("chart.csv", sep=';')

# Step 2: Select only the relevant columns for Prophet
df_clean = df_raw[['timeClose', 'close']].copy()

# Step 3: Rename columns to match Prophet requirements
df_clean.rename(columns={
    'timeClose': 'ds',
    'close': 'y'
}, inplace=True)

# Step 4: Convert 'ds' to datetime format
df_clean['ds'] = pd.to_datetime(df_clean['ds']).dt.date

# Step 5: Sort by date in ascending order
df_clean.sort_values('ds', inplace=True)

# Step 6: Reset index
df_clean.reset_index(drop=True, inplace=True)

# Step 7: Save cleaned data to a new CSV
df_clean.to_csv("cleaned_chart.csv", index=False)

