
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(6,6))

# Data
job_types = ["Office-based","Remote-based","Field-based","Contractor-based","Part-time-based","Full-time-based"]
percentages = [27,26,15,13,14,5]

# Plot
ax = fig.add_subplot(111) # add_subplot() follows plt.figure()
ax.pie(percentages, labels=job_types, autopct='%1.1f%%', startangle=90)
ax.set_title("Employment Distribution in the USA, 2023") # The title of the figure

# Legend
leg = ax.legend(loc="best", bbox_to_anchor=(1,0.5),title="Job Types") # The positioning of the legend
for text in leg.get_texts():
    text.set_wrap(True) # wrap=true
    
# Resize image
plt.tight_layout()

# Save image
plt.savefig("pie chart/png/380.png")

# Clear current image state
plt.clf()