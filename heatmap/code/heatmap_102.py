
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Define data
data = {"Disease": ["Cancer", "Heart Disease", "Diabetes", "Respiratory Illness", "Mental Health"],
        "Number of Patients": [500, 1000, 2000, 800, 300],
        "Treatment Cost (USD)": [5000, 10000, 2000, 8000, 3000],
        "Hospital Stay (Days)": [10, 20, 5, 15, 7],
        "Recovery Rate (%)": [90, 80, 95, 85, 92],
        "Mortality Rate (%)": [10, 20, 5, 15, 8],
        "Patient Satisfaction (%)": [80, 75, 85, 70, 90]
        }

# Convert data to dataframe
df = pd.DataFrame(data)

# Set plot size
plt.figure(figsize=(10, 6))

# Create heatmap using seaborn
sns.heatmap(df.set_index('Disease'), annot=True, cmap="Blues")

# Set x and y labels
# plt.ylabel("Disease")
# plt.ylabel("Metrics")

# # Set x and y ticks and ticklabels in the center
# plt.xticks(np.arange(5), df["Disease"], ha="right", rotation_mode="anchor", rotation=45)
# plt.yticks(np.arange(6), df.columns[1:], ha="right", rotation_mode="anchor", rotation=0)

# Add title
plt.title("Healthcare Metrics by Disease")

# Automatically resize image
plt.tight_layout()

# Save figure
plt.savefig("output/final/heatmap/png/20231228-130949_11.png", bbox_inches="tight")

# Clear image state
plt.clf()