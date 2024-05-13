# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv('feeds.csv')

# Convert 'created_at' column to datetime
df['created_at'] = pd.to_datetime(df['created_at'])

# Remove the 'entry_id' column for data cleaning 
df.drop('entry_id', axis=1, inplace=True)

# Find the maximum pollution value in the entire dataset
max_pollution = df['field1'].max()
print("Maximum Pollution Value:", max_pollution)

# Create a time series plot of pollution levels
plt.figure(figsize=(12, 8))
plt.rcParams.update({'font.size': 15})
sns.lineplot(x='created_at', y='field1', data=df)
plt.xlabel("Date & Time")
plt.ylabel("Pollution Level")
plt.title("Hourly Pollution Level")
# Display available date and time slots in the CSV file
available_date_time_slots = df['created_at'].dt.strftime('%Y-%m-%d %H:%M:%S').unique()
print("Available Date & Time Slots in the CSV File:")
for date_time_slot in available_date_time_slots:
    print(date_time_slot)

# User input for date and time
user_date_time = input("Enter a date and time (YYYY-MM-DD HH:MM:SS): ")
try:
    # Convert user input to datet ime and make it timezone-aware with UTC
    user_datetime = pd.to_datetime(user_date_time, format='%Y-%m-%d %H:%M:%S', utc=True)

    # Find the nearest date and time in the dataset
    nearest_datetime = df['created_at'].sub(user_datetime).abs().idxmin()
    nearest_datetime_value = df.at[nearest_datetime, 'created_at']
    pollution_value = df.at[nearest_datetime, 'field1']

    print(f"Nearest Pollution data to {user_datetime}:")
    print(f"Date & Time: {nearest_datetime_value}")
    print(f"Pollution Level: {pollution_value}")

except ValueError:
    print("Invalid date and time format. Please use YYYY-MM-DD HH:MM:SS.")

# Show the plots
plt.show()
