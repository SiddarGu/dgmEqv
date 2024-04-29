
import matplotlib.pyplot as plt

# Create figure
fig = plt.figure(figsize=(14,7))
ax = fig.add_subplot(1, 1, 1)

# Plot data
ax.plot(['10-19','20-29','30-39','40-49','50-59','60-69','70-80'],
        [120,150,175,200,225,250,275], label='Average Weight(lbs)', marker='o')
ax.plot(['10-19','20-29','30-39','40-49','50-59','60-69','70-80'],
        [60,65,68,70,72,74,76], label='Average Height(in)', marker='o')
ax.plot(['10-19','20-29','30-39','40-49','50-59','60-69','70-80'],
        [19,22,25,30,35,40,45], label='Average Body Mass Index(BMI)', marker='o')

# Customize chart
ax.set_title('Average weight, height and BMI of people in different age groups')
ax.set_xlabel('Age')
ax.set_ylabel('Value')
ax.legend(loc='upper left', ncol=1, fontsize=14)
ax.set_xticks(['10-19','20-29','30-39','40-49','50-59','60-69','70-80'])
fig.tight_layout()

# Save image
plt.savefig('line chart/png/215.png')

# Clear current image state
plt.clf()