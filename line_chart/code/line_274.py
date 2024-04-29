
import matplotlib.pyplot as plt
import numpy as np

# Create figure
fig=plt.figure(figsize=(10,6))

# Set data
month=["January","February","March","April","May","June","July","August","September","October","November","December"]
delay=[4,7,6,4,3,5,4,6,5,3,4,5]

# Plot line chart
plt.plot(month,delay,color="green")

# Set label, title and legend
plt.xlabel("Month")
plt.ylabel("Average Hours of Delay")
plt.xticks(month, rotation=45, wrap=True)
plt.title("Average hours of delay in air transportation in 2021")

# Set background grid
plt.grid()

# Adjust the image
plt.tight_layout()

# Save and show figure
plt.savefig("line chart/png/42.png")
plt.show()

# Clear the state of the current image
plt.clf()