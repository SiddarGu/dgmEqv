
# Import required modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create dictionary to represent data
data = {'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        'Hotel Bookings (Units)': [200, 180, 220, 230, 250, 270, 300, 280, 270, 260, 240, 220],
        'Airline Bookings (Units)': [150, 160, 180, 200, 220, 240, 260, 240, 230, 220, 200, 180],
        'Car Rentals (Units)': [180, 200, 150, 180, 190, 200, 220, 200, 190, 180, 160, 150],
        'Restaurant Reservations (Units)': [130, 150, 160, 170, 180, 190, 200, 190, 180, 170, 150, 140]}

# Convert first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Set figure size and create subplots
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the data as an area chart
ax.stackplot(df['Month'], df['Hotel Bookings (Units)'], df['Airline Bookings (Units)'], df['Car Rentals (Units)'], df['Restaurant Reservations (Units)'],
             labels=['Hotel Bookings (Units)', 'Airline Bookings (Units)', 'Car Rentals (Units)', 'Restaurant Reservations (Units)'],
             colors=['#2ca02c', '#1f77b4', '#ff7f0e', '#d62728'],
             alpha=0.5)

# Set x and y axis ticks and ticklabels
if np.random.choice([0, 1]):
    ax.set_xticks(np.arange(len(df['Month'])))
    ax.set_xticklabels(df['Month'])
if np.random.choice([0, 1]):
    ax.set_xlim(0, len(df.index) - 1)
if np.random.choice([0, 1]):
    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    max_total_value = np.ceil(max_total_value / 10) * 10
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32))

# Set grid lines
if np.random.choice([0, 1]):
    ax.grid(True, linestyle='dashed')

# Set legend
legend = ax.legend(loc='upper left')
for text in legend.get_texts():
    text.set_color('black')

# Set title and labels
ax.set_title('Reservation Trends by Month')
ax.set_xlabel('Month')
ax.set_ylabel('Units')

# Automatically resize image by tight_layout() before saving
plt.tight_layout()

# Save image as png
plt.savefig('output/final/area_chart/png/20231226-130527_7.png', bbox_inches='tight')

# Clear current image state
plt.clf()