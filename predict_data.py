import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Data Preprocessing
data = pd.read_csv('feeds.csv')  
data['created_at'] = pd.to_datetime(data['created_at'])

# 2. Feature Engineering
data['hour_of_day'] = data['created_at'].dt.hour
data['day_of_week'] = data['created_at'].dt.dayofweek

# 3. User Input for Prediction
date_time_input = input("Enter the date and time (YYYY-MM-DD HH:MM:SS): ")
date_time_input = pd.to_datetime(date_time_input)
hour_input = date_time_input.hour
day_of_week_input = date_time_input.dayofweek

# 4. Choose a Model (You can choose other regression models too)
model = LinearRegression()

# 5. Train the Model (You can skip this step if you only want to make predictions)
target = data['field1']
features = data[['hour_of_day', 'day_of_week']]
model.fit(features, target)

# 6. Make Predictions
new_data = pd.DataFrame({'hour_of_day': [hour_input], 'day_of_week': [day_of_week_input]})
predicted_pollution = model.predict(new_data)

print(f"Predicted Pollution for {date_time_input}: {predicted_pollution[0]}")
