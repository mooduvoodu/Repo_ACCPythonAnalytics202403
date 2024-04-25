import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/workspaces/Repo_ACCPythonAnalytics202403/kclubb/stockhistory/DIS.csv')
# Convert the epoch milliseconds in 't' column to datetime
df['t'] = pd.to_datetime(df['t'], unit='ms')

# Plotting the 'vw' column against the 't' datetime column
plt.figure(figsize=(10, 5))
plt.plot(df['t'], df['vw'], label='VW', color='blue')
plt.xlabel('Time')
plt.ylabel('VW')
plt.title('Time Series of VW')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)  # Rotate date labels for better readability
plt.tight_layout()
plt.show()