
import matplotlib.pyplot as plt
import pandas as pd 

# Create dataframe from the data
df = pd.DataFrame({'Time': ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00'],
                   'Gravity': [9.8, 9.7, 9.6, 9.5, 9.4, 9.3, 9.2],
                   'Temperature(Celsius)': [20,19,18,17,16,15,14],
                   'Humidity': [90,85,80,75,70,65,60],
                   'Pressure': [1014,1012,1009,1007,1004,1002,1000]})

# Create figure and plot
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot()
ax.plot('Time', 'Gravity', data=df, label='Gravity', marker='o', color='lightseagreen')
ax.plot('Time', 'Temperature(Celsius)', data=df, label='Temperature', marker='o', color='dodgerblue')
ax.plot('Time', 'Humidity', data=df, label='Humidity', marker='o', color='plum')
ax.plot('Time', 'Pressure', data=df, label='Pressure', marker='o', color='salmon')

# Add title, grids, legend, etc
ax.set_title("Changes in gravity, temperature, humidity and pressure in a laboratory at midnight on May 1, 2021")
ax.set_ylabel("Gravity/Temperature/Humidity/Pressure")
ax.set_xlabel("Time")
ax.legend(loc='center left')
ax.grid(True)
ax.set_xticks(df['Time'])
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/366.png')

# Clear the current figure
plt.clf()