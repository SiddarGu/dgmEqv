import matplotlib.pyplot as plt

# Initial data
data = [
    {"Platform": "Facebook",  "Min": 1.0, "Q1": 1.5, "Median": 2.0, "Q3": 2.5, "Max": 3.0, "Outliers": []},
    {"Platform": "Twitter",   "Min": 0.8, "Q1": 1.3, "Median": 1.9, "Q3": 2.4, "Max": 2.8, "Outliers": []},
    {"Platform": "Instagram", "Min": 0.6, "Q1": 1.1, "Median": 1.7, "Q3": 2.3, "Max": 2.9, "Outliers": [4.5]},
    {"Platform": "Snapchat",  "Min": 0.9, "Q1": 1.4, "Median": 2.2, "Q3": 2.8, "Max": 3.2, "Outliers": [0.3, 0.5, 5.0]},
    {"Platform": "LinkedIn",  "Min": 0.5, "Q1": 0.9, "Median": 1.5, "Q3": 2.1, "Max": 2.6, "Outliers": [0.1, 4.9]}
]

# Restructuring data
categories = [d["Platform"] for d in data]
values = [[d["Min"], d["Q1"], d["Median"], d["Q3"], d["Max"]] for d in data]
outliers = [d["Outliers"] for d in data]

# Creating figure and axis
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1)

# Box plotting
bp = ax.boxplot(values, whis=1.5)
plt.setp(bp['medians'], color='red')

# Plotting outliers
for i, outlier in enumerate(outliers):
    if outlier:
        ax.plot([i + 1] * len(outlier), outlier, "x", color='purple')

# Customizing graph
ax.set_ylabel("User Time (Hours)")
ax.grid(linestyle="--", alpha=0.6)
ax.set_xticklabels(categories, rotation=30)

# Set title
plt.title('User Time Distribution (In Hours) on Social Media Platforms in 2022')

# Save the figure
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/box/png/153_202312310058.png')

# Clear figure
plt.clf()
