
import matplotlib.pyplot as plt
import numpy as np

# Create figure and subplot
fig, ax = plt.subplots(figsize=(12, 6))

# Set the x axis label
ax.set_xlabel("Country", fontsize=15)

# Set the y axis label
ax.set_ylabel("Users (million)", fontsize=15)

# Set the title of the figure 
ax.set_title("Number of internet and smartphone users in four countries in 2021", fontsize=20)

# Create a list called countries
countries = ["USA", "UK", "Germany", "France"]

# Create a list called internet_users
internet_users = [250, 50, 80, 60]

# Create a list called smartphone_users
smartphone_users = [200, 45, 65, 55]

# Set the x axis 
ax.set_xticks(np.arange(len(countries)))

# Set the x axis labels
ax.set_xticklabels(countries, rotation=45, fontsize=13, wrap=True)

# Plot the bar chart
ax.bar(np.arange(len(countries)), internet_users, color="blue", label="Internet Users")
ax.bar(np.arange(len(countries)), smartphone_users, bottom=internet_users, color="red", label="Smartphone Users")

# Create a legend
ax.legend(loc="best")

# Adjust the image
plt.tight_layout()

# Save the image
plt.savefig("bar chart/png/41.png")

# Clear the current image state
plt.clf()