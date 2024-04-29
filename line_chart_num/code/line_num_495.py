
import matplotlib.pyplot as plt

# Set figsize for a larger size to avoid cropping
plt.figure(figsize=(10,6))

# Create a subplot
ax = plt.subplot()

# Add a title
ax.set_title("Technology usage among consumers in the past decade")

# Create x axis from year data
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016]

# Create y axis from data
smartphone_usage = [20, 30, 45, 55, 65, 75, 85]
computer_usage = [50, 55, 60, 70, 75, 80, 85]
tablet_usage = [2, 4, 7, 9, 11, 13, 15]

# Plot line graph
plt.plot(years, smartphone_usage, label="Smartphone Usage(%)")
plt.plot(years, computer_usage, label="Computer Usage(%)")
plt.plot(years, tablet_usage, label="Tablet Usage(%)")

# Use xticks to prevent interpolation
plt.xticks(years)

# Add a legend
plt.legend(loc="upper left")

# Add data labels directly on the figure
for a,b in zip(years, smartphone_usage):
    plt.annotate(str(b), xy=(a,b))
for a,b in zip(years, computer_usage):
    plt.annotate(str(b), xy=(a,b))
for a,b in zip(years, tablet_usage):
    plt.annotate(str(b), xy=(a,b))

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save the figure
plt.savefig("line chart/png/290.png")

# Clear the current image state
plt.clf()