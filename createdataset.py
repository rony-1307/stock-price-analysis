# Importing modules
import pandas as pd
import numpy as np

# Generate sales data
np.random.seed(0)
date_rng = pd.date_range(start='2022-01-01', end='2022-01-31', freq='D')
stock_data = pd.DataFrame(date_rng, columns=['Date'])
stock_data['Symbol'] = "AAPL"
stock_data['Opening Stock'] = np.random.uniform(10, 250, size=(len(date_rng)))
stock_data['Closing Stock'] = np.random.uniform(10, 250, size=(len(date_rng)))
stock_data['Daily Return'] = None
stock_data['Profit or Loss'] = None

# Display the rows of the generated data
print(stock_data.to_string())

# Save to CSV
stock_data.to_csv('stock_data.csv',index=False)