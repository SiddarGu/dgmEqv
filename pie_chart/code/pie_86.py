
import matplotlib.pyplot as plt

# Create pie chart
plt.figure(figsize=(12,8))
labels = ['Primary Education', 'Secondary Education', 'Tertiary Education', 'Vocational Education']
sizes = [30, 25, 35, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, wedgeprops={'linewidth': 0.5, 'edgecolor':'k'})

# Add title
plt.title('Distribution of Education Levels in the USA in 2023', fontsize=15, fontweight='bold')

# Add legend
plt.legend(labels, loc='upper right',bbox_to_anchor=(1.2, 0.9))

# Adjust the image size
plt.tight_layout()

# Save the image
plt.savefig('pie chart/png/22.png')

# Clear the current image state
plt.clf()