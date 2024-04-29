
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Create figure before plotting
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot()

# Plot the line chart
ax.plot(
    [2001, 2002, 2003, 2004], 
    [200, 210, 220, 230], 
    label="Median Listing Price($)",
    color="blue",
    marker="o",
    linestyle="--"
)
ax.plot(
    [2001, 2002, 2003, 2004], 
    [180, 190, 200, 210], 
    label="Median Sale Price($)",
    color="red",
    marker="x",
    linestyle="--"
)
ax.plot(
    [2001, 2002, 2003, 2004], 
    [5000, 6000, 7000, 8000], 
    label="Number of Houses Sold",
    color="green",
    marker="^",
    linestyle="--"
)

# Set the title
plt.title("US Median Residence Prices and Number of Houses Sold from 2001 to 2004")

# Set the x axis labels
plt.xticks([2001, 2002, 2003, 2004], ["2001", "2002", "2003", "2004"], rotation=45)

# Display legend
plt.legend(loc="best")

# Automatically resize the image
plt.tight_layout()

# Save the figure
plt.savefig(r"line chart/png/147.png")

# Clear the current image state
plt.clf()