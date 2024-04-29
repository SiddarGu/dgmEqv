
import matplotlib.pyplot as plt

# Data
Country = ["USA", "UK", "Germany", "France"]
Number_of_Schools = [120, 90, 95, 85]
Number_of_Students = [250, 200, 190, 180]

# Create figure
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot()

# Plotting
ax.bar(Country, Number_of_Schools, bottom=0, label="Number of Schools")
ax.bar(Country, Number_of_Students, bottom=Number_of_Schools, label="Number of Students(hundred)")

# Labels
ax.set_title("Number of schools and students in four countries in 2021")
ax.set_xlabel("Country")
ax.set_ylabel("Number of Schools and Students")

# Legend
ax.legend(loc="upper right")

# Ticks
plt.xticks(Country, rotation=45, wrap=True)

# Tight layout
plt.tight_layout()

# Save
plt.savefig("bar_285.png")

# Clear
plt.clf()