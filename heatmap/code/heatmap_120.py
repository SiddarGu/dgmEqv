
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = {'University': ['Harvard University', 'University of Oxford', 'Stanford University', 'Massachusetts Institute of Technology', 'University of Cambridge'], 'Enrollment (x1000)': [220, 150, 200, 180, 160], 'Degrees Awarded (x1000)': [120, 80, 100, 90, 80], 'Average GPA': [3.8, 3.7, 3.9, 3.8, 3.7], 'SAT Average': [1400, 1350, 1450, 1450, 1350], 'Student-Faculty Ratio': [6.5, 7.0, 6.0, 8.0, 7.5]}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 6))

plt.imshow(df.set_index('University'), cmap='YlGnBu', interpolation='nearest')

# ax = plt.axes()
ax.set_title('Academic Performance Indicators')
ax.set_xlabel('University')
ax.set_ylabel('Student-Faculty Ratio')
ax.set_xticks(np.arange(len(df.columns[1:])))
ax.set_yticks(np.arange(len(df['University'])))
ax.set_xticklabels(df.columns[1:])
ax.set_yticklabels(df['University'])

plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
# plt.yticks(rotation=0, ha='right', rotation_mode='anchor')

plt.colorbar()
plt.tight_layout()

plt.savefig('output/final/heatmap/png/20231228-131639_24.png', bbox_inches='tight')

plt.clf()