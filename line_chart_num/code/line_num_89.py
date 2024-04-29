
import matplotlib.pyplot as plt
import numpy as np

# Set figure size
plt.figure(figsize=(10, 6)) 

# Set data
x = np.array(["Q1","Q2","Q3","Q4"])
y1 = np.array([500,600,620,550])
y2 = np.array([400,450,500,430])
y3 = np.array([600,550,530,580])

# Plot data
plt.plot(x, y1, color="red", linestyle="-", linewidth=2, marker="o", label="Production A")
plt.plot(x, y2, color="blue", linestyle="-", linewidth=2, marker="o", label="Production B")
plt.plot(x, y3, color="green", linestyle="-", linewidth=2, marker="o", label="Production C")

# Add labels and title
plt.xlabel("Quarter")
plt.ylabel("Production (thousand)")
plt.title("Manufacturing production of three categories of goods in 2021")

# Annotate value of each data point
for i, j in zip(x, y1):
    plt.annotate(str(j), xy=(i, j+10))
for i, j in zip(x, y2):
    plt.annotate(str(j), xy=(i, j-10))
for i, j in zip(x, y3):
    plt.annotate(str(j), xy=(i, j+10))

# Add grid and legend
plt.grid(True, linestyle="--", alpha=0.3)
plt.legend(loc="upper right", fontsize=12)

# Set tick and xticks
plt.tick_params(axis='both', which='major', labelsize=12)
plt.xticks(x, x, rotation=45, size=12)

# Adjust figure
plt.tight_layout()

# Save figure
plt.savefig("./line chart/png/341.png")

# Clear current figure
plt.clf()