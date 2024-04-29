
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)

# Data
School = ('Harvard', 'Yale', 'Stanford', 'MIT')
Enrollment = (1500, 1300, 1400, 1200)
Graduates = (1000, 950, 950, 1100)

# Plot the bar chart
ax.bar(School, Enrollment, label='Enrollment', alpha=0.7, width=0.3, bottom=0)
ax.bar(School, Graduates, label='Graduates', alpha=0.5, width=0.3, bottom=0)

# Set label, legend and title
ax.set_xlabel('School')
ax.set_ylabel('Number')
ax.legend(loc='best')
ax.set_title('Enrollment and graduates of four top universities in 2021')
ax.set_xticks(np.arange(len(School)))
ax.set_xticklabels(School, rotation=45, wrap=True)

# Resize the figure
plt.tight_layout()

# Save figure
plt.savefig('bar chart/png/433.png', bbox_inches='tight', dpi=300)

# Clear the current image state
plt.clf()