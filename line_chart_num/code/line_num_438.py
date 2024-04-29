
import matplotlib.pyplot as plt
import numpy as np

# Set figure size
plt.figure(figsize=(10, 5))

# Create axes
ax = plt.subplot()

# Data
month = ['January', 'February', 'March', 'April', 'May', 'June']
global_users = [3.5, 3.6, 3.7, 3.8, 3.9, 4.0]
us_users = [1.2, 1.3, 1.4, 1.5, 1.6, 1.7]
asia_users = [2.3, 2.4, 2.5, 2.6, 2.7, 2.8]

# Set x axis
x_axis = np.arange(len(month))

# Plot data
plt.plot(x_axis, global_users, marker="o", color="red", label="Global Users")
plt.plot(x_axis, us_users, marker="^", color="green", label="US Users")
plt.plot(x_axis, asia_users, marker="s", color="blue", label="Asia Users")

# Set xticks
plt.xticks(x_axis, month, rotation=45)

# Configure legend
plt.legend(loc="upper left", bbox_to_anchor=(1, 1), frameon=False)

# Set title
plt.title("Global, US and Asia Social Media Users in the first half of 2022")

# Auto resize the image
plt.tight_layout()

# Save image
plt.savefig('line chart/png/207.png')

# Clear current image
plt.clf()