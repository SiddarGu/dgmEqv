
import matplotlib.pyplot as plt

# Create figure and subplot.
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

# Create data array for plotting.
month_data = ["January", "February", "March", "April", "May"]
users_A_data = [500, 600, 700, 650, 800]
users_B_data = [1000, 1100, 1200, 1050, 1400]
users_C_data = [1500, 1400, 1300, 1500, 1200]

# Plot data and set parameter.
ax.plot(month_data, users_A_data, label="Users A")
ax.plot(month_data, users_B_data, label="Users B")
ax.plot(month_data, users_C_data, label="Users C")
ax.set_title("Monthly user growth for three social media platforms")
ax.set_xlabel("Month")
ax.set_ylabel("Users")
ax.legend(loc="best")
ax.grid(True)
plt.xticks(month_data)
plt.tight_layout()

# Save the figure.
plt.savefig("line chart/png/126.png")

# Clear the current image state.
plt.clf()