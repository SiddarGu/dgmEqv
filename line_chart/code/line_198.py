
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

# Create a subplot
ax = plt.subplot()

# Set the x axis labels
ax.set_xticks([2001, 2002, 2003, 2004])
ax.set_xticklabels(['2001', '2002', '2003', '2004'], rotation=45, ha='right', wrap=True)

# Set the y axis labels
ax.tick_params(axis='y', labelsize=10, rotation=90)

# Plot the data
ax.plot([2001, 2002, 2003, 2004], [100, 90, 80, 85], label='Production A (million units)', linestyle='--')
ax.plot([2001, 2002, 2003, 2004], [150, 170, 180, 160], label='Production B (million units)', linestyle='--')
ax.plot([2001, 2002, 2003, 2004], [120, 140, 155, 130], label='Production C (million units)', linestyle='--')
ax.plot([2001, 2002, 2003, 2004], [200, 190, 175, 205], label='Production D (million units)', linestyle='--')

# Add a legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.2), shadow=True, ncol=4)

# Add a title
ax.set_title('Production output of four categories of products in the last decade')

# Tighten the layout
plt.tight_layout()

# Save the figure
plt.savefig('line chart/png/119.png')

# Clear the current figure
plt.clf()