
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(15, 8))

# Plot data
plt.plot(
    [2020, 2021, 2022, 2023],
    [200, 150, 400, 250],
    label="Investment A(million dollars)",
    color="b",
    linestyle="dashed",
    marker="o",
    markerfacecolor="red",
    markersize=10
)

plt.plot(
    [2020, 2021, 2022, 2023],
    [100, 200, 300, 350],
    label="Investment B(million dollars)",
    color="g",
    linestyle="dashed",
    marker="o",
    markerfacecolor="yellow",
    markersize=10
)

plt.plot(
    [2020, 2021, 2022, 2023],
    [400, 300, 200, 450],
    label="Investment C(million dollars)",
    color="k",
    linestyle="dashed",
    marker="o",
    markerfacecolor="orange",
    markersize=10
)

plt.plot(
    [2020, 2021, 2022, 2023],
    [500, 550, 450, 500],
    label="Investment D(million dollars)",
    color="r",
    linestyle="dashed",
    marker="o",
    markerfacecolor="green",
    markersize=10
)

# Set x and y labels
plt.xlabel('Year')
plt.ylabel('Investment (million dollars)')

# Set ticks
plt.xticks([2020, 2021, 2022, 2023])

# Set legend
plt.legend(loc="upper left")

# Set title
plt.title('Investment in four categories of businesses in the next four years')

# Resize image
plt.tight_layout()

# Save image
plt.savefig('line chart/png/270.png')

# Clear current image state
plt.clf()