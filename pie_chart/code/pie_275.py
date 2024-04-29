
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111)

# Data
education = ["Primary Education", "Secondary Education", "Higher Education", "Vocational Education", "Non-formal Education"]
percentage = [35, 25, 25, 10, 5]

# Plot
ax.pie(percentage, labels=education, autopct='%1.1f%%', startangle=90, textprops={'wrap': True, 'rotation': 0})

# Title
ax.set_title("Distribution of Educational Expenditures in the US in 2023")

# Remove frame
ax.set_frame_on(False)

# Tight layout
plt.tight_layout()

# Save
plt.savefig("pie chart/png/457.png")

# Clear
plt.clf()