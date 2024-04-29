
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(15, 8))
ax = fig.add_subplot(111)

# Data
grades = ["5th Grade", "6th Grade", "7th Grade", "8th Grade", "9th Grade"]
average_score = [80, 85, 90, 95, 98]
number_of_students = [50, 60, 70, 80, 90]

# Plot
ax.plot(grades, average_score, color="red", label="Average Score (out of 100)", linestyle="--")
ax.plot(grades, number_of_students, color="blue", label="Number of Students", linestyle="-")

# Labels
ax.set_title("Average Test Scores by Grade Level in a School District")
ax.set_xlabel("Grade")
ax.set_ylabel("Score/Number of Students")

# Legend
ax.legend(loc="upper left", fontsize="large")

# Annotate
for x, y in zip(grades, average_score):
    ax.annotate(y, xy=(x, y), xytext=(x, y+2), fontsize="x-large")

for x, y in zip(grades, number_of_students):
    ax.annotate(y, xy=(x, y), xytext=(x, y+2), fontsize="x-large")

# xticks
plt.xticks(grades, fontsize="xx-large")

# Resize
plt.tight_layout()

# Save
plt.savefig("line chart/png/451.png")

# Clear
plt.clf()