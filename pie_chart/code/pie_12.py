
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Create figure
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1, 1, 1)

# Set Pie chart parameters
labels = ["Men", "Women", "18-24", "25-34", "35-44", "45-54", "55-64", "65+"]
data = [48, 52, 14, 18, 18, 20, 16, 14]
explode = [0, 0.1, 0, 0, 0, 0, 0, 0]

# Draw Pie chart
ax.pie(data, labels=labels, explode=explode, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax.axis('equal')

# Set title
ax.set_title("Demographic Breakdown of the US Population in 2023")

# Prevent Labels from Interfering with Chart
ax.legend(loc="upper right", bbox_to_anchor=(1.4, 1))

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Prevent Interpolation
ax.xaxis.set_major_locator(ticker.FixedLocator(range(0, 8)))
ax.xaxis.set_major_formatter(ticker.FixedFormatter(labels))

# Save image
plt.savefig("pie chart/png/167.png")

# Clear the current image state at the end of the code
plt.clf()