import pandas as pd
import matplotlib.pyplot as plt

# Given data
data = {
    "Government Department": [
        "Defense",
        "Education",
        "Health & Human Services",
        "Energy",
        "Veteran Affairs",
        "Homeland Security",
        "State & International Programs",
        "Environmental Protection",
        "Justice",
        "Agriculture"
    ],
    "Budget Allocation ($ Billion)": [620.2, 68.0, 89.5, 32.1, 85.4, 47.6, 51.3, 9.2, 58.0, 25.0]
}

# Transforming into three variables
data_labels = list(data.keys())[1:]  # Column labels except the first one
line_labels = data["Government Department"]  # Row labels except the first one
data = data["Budget Allocation ($ Billion)"]  # Numerical data

# Create a pandas DataFrame
df = pd.DataFrame(data={
    "Department": line_labels,
    "Budget": data
})

# Create a figure and a subplot
plt.figure(figsize=(14, 8))
ax = plt.subplot()

# Plot a vertical histogram using pandas
df.plot(kind='bar', x='Department', y='Budget', ax=ax, legend=False, color=plt.cm.tab20.colors)

# Title and labels with settings to prevent overlapping
plt.title("U.S. Federal Government Budget Distribution by Department")
plt.xlabel("Government Department")
plt.ylabel("Budget Allocation ($ Billion)")
plt.xticks(rotation=45, ha='right', wrap=True)

# Grid, layout, and style adjustments
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save the image
save_path = "/cpfs01/user/liuqi/workspace/plotchart/data-300/histogram/png/173.png"
plt.savefig(save_path, format='png')

# Clear the current image state
plt.clf()
