
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Create figure
fig, ax = plt.subplots(figsize=(13, 8))

# Plot the data
orgs = ['WFP', 'UNICEF', 'Save the Children', 'Red Cross']
donations = [500, 200, 150, 400]
volunteers = [1000, 800, 600, 1100]

# Set width of the bottom
bar_width = 0.3

# Set the bar position
bar_donations = [i for i in range(len(orgs))]
bar_volunteers = [x + bar_width for x in bar_donations]

# Plot the bar chart
ax.bar(bar_donations, donations, width=bar_width, label='Donations (million)', color='#FF7F50')
ax.bar(bar_volunteers, volunteers, width=bar_width, label='Volunteers', color='#66CDAA')

# Add title and axis names
ax.set_title('Donations and volunteers for four charity organizations in 2021', fontsize=16)
ax.set_xticks([r + bar_width for r in range(len(orgs))])
ax.set_xticklabels(orgs)
ax.set_xlabel('Organization')
ax.set_ylabel('Quantity')

# Add labels
for x, y in enumerate(donations):
    label = y
    ax.annotate(label, 
                (bar_donations[x], y), 
                xytext=(0, 5), 
                textcoords='offset points',
                ha='center',
                va='bottom')

for x, y in enumerate(volunteers):
    label = y
    ax.annotate(label, 
                (bar_volunteers[x], y), 
                xytext=(0, 5), 
                textcoords='offset points',
                ha='center',
                va='bottom')

# Add legend
ax.legend(loc='upper right')

# Adjust the output
ax.yaxis.set_major_locator(ticker.MultipleLocator(100))
plt.tight_layout()

# Save the figure
plt.savefig('Bar Chart/png/340.png')

# Clear the current image state
plt.clf()