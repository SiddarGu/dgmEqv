
import matplotlib.pyplot as plt

# Create figure before plotting
fig = plt.figure(figsize=(10,10))
ax1 = fig.add_subplot()

# Set data
platforms = ["Facebook","YouTube","Instagram","Twitter","LinkedIn","Reddit","Snapchat","Other"]
percentage = [30,25,15,10,10,5,3,2]

# Draw pie chart
ax1.pie(percentage, labels=platforms, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize':12})
ax1.axis('equal')

# Set title
plt.title("Popularity of Social Media Platforms among Global Users in 2023")

# Set legend
plt.legend(bbox_to_anchor=(1,1), loc="upper left")

# Set rotation
plt.xticks(rotation=45)

# Automatically resize the image
plt.tight_layout()

# Save image
plt.savefig("pie chart/png/377.png")

# Clear current image state
plt.clf()