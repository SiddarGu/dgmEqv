
import matplotlib.pyplot as plt
import pandas as pd

# Read data
data = [['January', 1000, 1300, 100],
        ['February', 1200, 1400, 50],
        ['March', 1400, 1600, 90],
        ['April', 1600, 1400, 100],
        ['May', 1800, 1300, 80]]
df = pd.DataFrame(data, columns=['Month','Patients Cured','Patients Hospitalized','Patients Deceased'])

# Plot figure
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)

# Plot line chart
line1, = ax.plot(df['Month'], df['Patients Cured'], label='Patients Cured', marker='o')
line2, = ax.plot(df['Month'], df['Patients Hospitalized'], label='Patients Hospitalized', marker='o')
line3, = ax.plot(df['Month'], df['Patients Deceased'], label='Patients Deceased', marker='o')

# Set fonts
font = {'family': 'serif',
        'weight': 'normal',
        'size': 10}
plt.rc('font', **font)

# Set xticks
plt.xticks(rotation=45)

# Set legend
plt.legend(handles=[line1, line2, line3], loc='upper left')

# Add title
plt.title('Healthcare trends in 2020: Patients cured, hospitalized, and deceased')

# Annotate value
for x, y in zip(df['Month'], df['Patients Cured']):
    plt.annotate(y, xy=(x, y), xytext=(-10, 10), textcoords='offset points')
for x, y in zip(df['Month'], df['Patients Hospitalized']):
    plt.annotate(y, xy=(x, y), xytext=(-10, 10), textcoords='offset points')
for x, y in zip(df['Month'], df['Patients Deceased']):
    plt.annotate(y, xy=(x, y), xytext=(-10, 10), textcoords='offset points')

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/612.png', dpi=600)

# Clear the current image state
plt.clf()