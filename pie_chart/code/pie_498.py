
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(10, 8))

# Plotting Pie chart
labels = ['Rock Music', 'Pop Music', 'Jazz Music', 'Classical Music', 'Other Genres']
values = [35, 25, 15, 15, 10]
plt.pie(values, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': 8, 'wrap': True, 'rotation': 90})
plt.title("Music Genre Popularity in the World, 2023")
plt.tight_layout()

# Save chart
plt.savefig('pie chart/png/178.png')

# Clear current image state
plt.clf()