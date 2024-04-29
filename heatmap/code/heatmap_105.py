
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create a dictionary to store the data
data = {
    'Organization': ['Red Cross', 'Save the Children', 'Oxfam', 'Habitat for Humanity', 'World Wildlife Fund', 'UNICEF'],
    'Revenue (Millions of Dollars)': [500, 300, 200, 100, 50, 400],
    'Expenses (Millions of Dollars)': [450, 280, 190, 90, 40, 380],
    'Programs (%)': [60, 70, 80, 90, 95, 50],
    'Fundraising (%)': [30, 25, 15, 5, 3, 40],
    'Administrative (%)': [10, 5, 5, 5, 2, 10]
}

# Create a pandas dataframe using the dictionary
df = pd.DataFrame(data)

# Set the index to be the organization names
df = df.set_index('Organization')

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10,8))

# Plot the heatmap using the seaborn package
import seaborn as sns
sns.heatmap(df, annot=True, cmap='Blues', cbar=True)

# Set the title and labels
plt.title('Financial Overview of Top Nonprofits')
plt.xlabel('Expenses and Revenue (Millions of Dollars)')
plt.ylabel('Programs, Fundraising and Administrative (%)')

# Resize the figure and save it as a png file
fig.tight_layout()
plt.savefig('output/final/heatmap/png/20231228-130949_2.png', bbox_inches='tight')

# Clear the current image state
plt.clf()