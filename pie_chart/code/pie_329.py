
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Set up figure
fig = plt.figure(figsize=(7,7))
ax1 = fig.add_subplot(111)

# Set up data
labels = ['Education', 'Healthcare', 'Transportation', 'Housing and Community', 'Public Safety', 'Welfare', 'Other']
sizes = [25, 20, 15, 15, 10, 10, 15]

# Set up colors
colors = cm.Set3(np.arange(len(labels))/float(len(labels)))

# Plot
wedges, texts, autotexts = ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize':12}, wedgeprops={'linewidth':2})

# Set up legend
plt.legend(wedges, labels, title="Social Services", bbox_to_anchor=(1.3, 0.85))

# Set up title
plt.title('Distribution of Public Spending on Social Services in the US, 2023', fontsize=16)

# Make sure text is readable
for i, autotext in enumerate(autotexts):
    autotext.set_rotation(45)
    autotext.set_text(autotext.get_text() + "\n")

# Automatically resize the image
plt.tight_layout()

# Save Figure
plt.savefig("pie chart/png/273.png")

# Clear the current image state
plt.clf()