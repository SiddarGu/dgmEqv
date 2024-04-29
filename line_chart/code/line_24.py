
import matplotlib.pyplot as plt
import pandas as pd

# Generate the dataframe
data= {'Year': [2018, 2019, 2020, 2021, 2022], 'Painting': [100, 150, 180, 200, 220], 'Sculpture': [200, 220, 250, 270, 300], 'Photography': [300, 250, 320, 280, 260]}
df = pd.DataFrame(data)

# Create the figure
fig = plt.figure(figsize=(15, 10))
ax = fig.add_subplot()

# Plot the data
ax.plot(df['Year'], df['Painting'], label='Painting', marker='o', color='b', linestyle='-')
ax.plot(df['Year'], df['Sculpture'], label='Sculpture', marker='o', color='r', linestyle='-')
ax.plot(df['Year'], df['Photography'], label='Photography', marker='o', color='y', linestyle='-')

# Add x-axis label and y-axis label
ax.set_xlabel('Year')
ax.set_ylabel('Number of artworks')

# Set the x ticks
plt.xticks(df['Year'], rotation=45)

# Set the title
ax.set_title('Number of artworks produced in different genres in the last five years')

# Add legend
ax.legend()

# Automatically resize the image
plt.tight_layout()

# Save the image
plt.savefig('line chart/png/93.png')

# Clear the current image state
plt.clf()