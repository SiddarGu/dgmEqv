
import matplotlib.pyplot as plt
import numpy as np

# Data to plot
Country = ['USA', 'UK', 'Germany', 'France']
Tax_Rate = [20, 30, 15, 25]
Voter_Turnout = [55, 65, 60, 50]

# Create figure before plotting
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

# Plot the data with the type of bar chart
ax.bar(Country, Tax_Rate, color='b', label='Tax Rate')
ax.bar(Country, Voter_Turnout, bottom=Tax_Rate, color='g', label='Voter Turnout')

# Set the title of the figure
ax.set_title('Tax Rates and Voter Turnout in Four Countries in 2021')

# Set the label of x axis
ax.set_xlabel('Country')

# Set the label of y axis
ax.set_ylabel('Rate(%)')

# Set the ticks on x axis
ax.set_xticks(np.arange(len(Country)))

# Set the strings of x axis
ax.set_xticklabels(Country, rotation=90)

# Set legend
ax.legend(loc='lower center', bbox_to_anchor=(0.5, -0.2))

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the image
plt.savefig('bar chart/png/23.png')

# Clear the current image state
plt.clf()