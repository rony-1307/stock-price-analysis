"""Stock Price Analysis"""

# Importing module for this project
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the csv file
df = pd.read_csv('stock_data.csv')

# Show the value of the CSV File
print(df.to_string())

# Calculate and Put the value of Daily Rerun in place of NaN vlue and show the value
daily_return = df['Closing Stock'] - df['Opening Stock']
df['Daily Return'].fillna(daily_return,inplace=True)
print(df.to_string())

# Initiate start and Stop poriton to check profit or loss
inital_index = df.first_valid_index()
last_index = df.last_valid_index()

# Check wheather its Profit or loss
for daily_return in df['Daily Return']:
    if daily_return > 0:
        print(daily_return)
        print('Profit')
    elif daily_return == 0:
        print(daily_return)
        print('No profit no loss')
    else:
        print(daily_return)
        print('Loss')

# Graph plot
xaxis = np.array(df['Date'])

# Opening Stock Plot
plt.title("Opening Stock Plot")
plt.xlabel("Price in Rs.")
plt.ylabel("Date")
plt.barh(xaxis, np.array(df['Opening Stock']), color = '#5CD2E6')
plt.grid()
plt.show()

# Closing Stock Plot
plt.title("Closing Stock Plot")
plt.xlabel("Price in Rs.")
plt.ylabel("Date")
plt.barh(xaxis, np.array(df['Closing Stock']), color = '#E5CFF7')
plt.grid()
plt.show()

# Daily Return Plot
plt.title("Daily Return")
plt.xlabel("Price in Rs.")
plt.ylabel("Date")
plt.barh(xaxis, np.array(df['Daily Return']), color = '#206322')
plt.grid()
plt.show()
