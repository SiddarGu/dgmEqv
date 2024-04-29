
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the data as a dictionary
data = {'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        '1 Bedroom Apartments (Listings)': [500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050],
        '2 Bedroom Apartments (Listings)': [600, 650, 700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150],
        '3 Bedroom Apartments (Listings)': [700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250],
        '4 Bedroom Apartments (Listings)': [800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350],
        '5+ Bedroom Apartments (Listings)': [900, 950, 1000, 1050, 1100, 1150, 1200, 1250, 1300, 1350, 1400, 1450]}

# Convert the first column to string type
df = pd.DataFrame(data)
df.iloc[:, 0] = df.iloc[:, 0].astype(str)

# Plot the data with an area chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.stackplot(df['Month'], df.iloc[:, 1:].T, labels=df.columns[1:], colors=['#0066CC', '#0099CC', '#00CCCC', '#00CC99', '#00CC66'], alpha=0.7)
ax.legend(loc='upper left', frameon=False)

# Set x and y axis ticks and labels
if np.random.choice([True, False], p=[0.7, 0.3]):
    ax.set_xlim(0, len(df.index) - 1)
    ax.set_xticks(np.arange(len(df.index)))
    ax.set_xticklabels(df['Month'], rotation=45, ha='right', rotation_mode='anchor', wrap=True)

    max_total_value = df.iloc[:, 1:].sum(axis=1).max()
    if max_total_value <= 50:
        yticks = np.linspace(0, 50, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
    elif max_total_value <= 500:
        yticks = np.linspace(0, 500, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
    elif max_total_value <= 5000:
        yticks = np.linspace(0, 5000, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
    else:
        yticks = np.linspace(0, max_total_value, np.random.choice([3, 5, 7, 9, 11]), dtype=np.int32)
    ax.set_ylim(0, max_total_value)
    ax.set_yticks(yticks)
    ax.set_yticklabels(yticks)
else:
    ax.set_xticks([])
    ax.set_xticklabels([])
    ax.set_yticks([])
    ax.set_yticklabels([])

# Set background grid lines
ax.grid(axis='y', alpha=0.3)

# Set title and labels
ax.set_title('Monthly Apartment Listings by Number of Bedrooms in 2018')
ax.set_xlabel('Month')
ax.set_ylabel('Number of Listings')

# Automatically resize the image and save
fig.tight_layout()
plt.savefig('output/final/area_chart/png/20231228-145339_19.png', bbox_inches='tight')

# Clear the current image state
plt.clf()