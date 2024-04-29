
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

labels = ['Bachelor\'s Degree', 'Master\'s Degree', 'Doctoral Degree', 'Professional Degree', 'Certificate/Diploma']
percentage = [35, 25, 20, 10, 10]
explode = (0.1, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

# Set figure size
fig = plt.figure(figsize=(12, 8))

# Set title
plt.title("Distribution of Degree Types in the USA, 2023")

# Add subplot
gs = gridspec.GridSpec(1, 1)
ax1 = plt.subplot(gs[0, 0])

# Create pie chart
ax1.pie(percentage, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display legend
plt.legend(bbox_to_anchor=(1.0, 0.5), loc="center left", fontsize=10)

# Set x-ticks
plt.xticks(rotation=45)

# Automatically resize the image
plt.tight_layout()

# Save figure
plt.savefig("pie chart/png/137.png")

# Clear current image state
plt.clf()