
import matplotlib.pyplot as plt
import numpy as np

# Data
State = ['California', 'Nevada', 'Arizona', 'New Mexico']
Hotels = [150, 200, 180, 230]
Tourists = [450, 500, 400, 470]

# Create figure
fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot()

# Plot Data
x = np.arange(len(State))
width = 0.35
ax.bar(x - width/2, Hotels, width, color='b', label="Hotels")
ax.bar(x + width/2, Tourists, width, color='r', label="Tourists")

# Set Labels
ax.set_xticks(x)
ax.set_xticklabels(State)
ax.set_ylabel('Number')

# Set Title
ax.set_title('Number of hotels and tourists in four US states in 2021')

# Annotate
for i in range(len(State)):
    ax.text(x[i] - width/2, Hotels[i] + 10, str(Hotels[i]), rotation=90, wrap=True)
    ax.text(x[i] + width/2, Tourists[i] + 10, str(Tourists[i]), rotation=90, wrap=True)

# Add Legend
ax.legend()

# Adjust Layout
fig.tight_layout()

# Save
plt.savefig('Bar Chart/png/371.png')

# Clear
plt.clf()