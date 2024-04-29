
import matplotlib.pyplot as plt
import numpy as np

# Create figure
plt.figure(figsize=(8,6))

# Plot data
year = np.array([2018, 2019, 2020, 2021])
sports = np.array([200, 300, 400, 500])
music = np.array([300, 250, 150, 200])
movies = np.array([400, 600, 500, 450])
theater = np.array([500, 300, 700, 800])

plt.plot(year, sports, label="Sports")
plt.plot(year, music, label="Music")
plt.plot(year, movies, label="Movies")
plt.plot(year, theater, label="Theater")

# Formatting
plt.title("Entertainment Industry Revenue in the United States from 2018 to 2021")
plt.xlabel('Year')
plt.ylabel('Revenue (in Millions)')
plt.xticks(year)
plt.legend(loc='upper left', bbox_to_anchor=(1,1), ncol=1, fontsize='small')
plt.tight_layout()

# Save figure
plt.savefig('line chart/png/33.png')

# Clear figure
plt.clf()