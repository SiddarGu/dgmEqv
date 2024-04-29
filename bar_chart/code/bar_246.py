
import matplotlib.pyplot as plt
import numpy as np

# Data
Country = ["USA","UK","Germany","France"]
Doctors = [7,4,6,5]
Nurses = [23,17,20,19]

# Create figure
fig = plt.figure(figsize=(8,6))

# Plot
ax = fig.add_subplot(1, 1, 1)
ax.bar(Country, Doctors, bottom=Nurses, label="Doctors")
ax.bar(Country, Nurses, label="Nurses")

# Label
ax.set_title("Number of doctors and nurses in four countries in 2021")
ax.legend()
ax.set_xticks(Country)

# Display
plt.tight_layout()
plt.savefig("bar chart/png/422.png")
plt.clf()