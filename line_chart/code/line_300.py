
import matplotlib.pyplot as plt
import numpy as np

# Create figure 
fig = plt.figure(figsize=(15,6))

# Get the GDP and unemployment rate data
year = np.array([2001, 2002, 2003, 2004])
gdp = np.array([10, 12, 14, 16])
unemployment = np.array([12, 14, 10, 8])

# Plot the GDP and unemployment rate line chart
plt.plot(year, gdp, label="GDP")
plt.plot(year, unemployment, label="Unemployment rate")

# Set x, y, title and legend
plt.xticks(year, rotation=90)
plt.xlabel("Year")
plt.ylabel("GDP/Unemployment rate(billion dollars/%)")
plt.title("GDP and Unemployment rate in the US from 2001 to 2004", fontsize=20)
plt.legend()

# Resize the image
plt.tight_layout()

# Save and clear the image
plt.savefig(r'line chart/png/224.png')
plt.clf()