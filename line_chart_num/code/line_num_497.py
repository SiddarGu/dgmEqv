
import matplotlib.pyplot as plt
import numpy as np

Year = [2001, 2002, 2003, 2004, 2005]
Air_Travel_m_passengers = [100, 120, 130, 140, 150]
Rail_Travel_m_passengers = [200, 190, 210, 220, 230]
Road_Travel_m_passengers = [400, 420, 390, 380, 360]

# Create a figure
fig = plt.figure(figsize=(10, 6))

# Add a subplot
ax = fig.add_subplot()

# Plot the data
ax.plot(Year, Air_Travel_m_passengers, label="Air Travel (million passengers)", color='red', marker='o', linestyle='solid')
ax.plot(Year, Rail_Travel_m_passengers, label="Rail Travel (million passengers)", color='green', marker='o', linestyle='solid')
ax.plot(Year, Road_Travel_m_passengers, label="Road Travel (million passengers)", color='blue', marker='o', linestyle='solid')

# Add title, labels and legend
ax.set_title("Passenger Travel in Three Modes in the United States from 2001 to 2005")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Passengers (million passengers)")
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=3)

# Set ticks
ax.set_xticks(Year)

# Annotate
for i, j in zip(Year, Air_Travel_m_passengers):
    ax.annotate(str(j), xy=(i, j))
for i, j in zip(Year, Rail_Travel_m_passengers):
    ax.annotate(str(j), xy=(i, j))
for i, j in zip(Year, Road_Travel_m_passengers):
    ax.annotate(str(j), xy=(i, j))
  
# Resize the plot
plt.tight_layout()

# Save the Figure
plt.savefig("line chart/png/609.png")

# Clear the Figure
plt.clf()