
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Data processing
data = {'Technology': ['Internet of Things (IoT)', 'Artificial Intelligence (AI)', 'Blockchain', 'Virtual Reality (VR)', '5G Technology', 'Edge Computing'],
        'Global Market Share': [35, 25, 15, 10, 8, 5]}
df = pd.DataFrame(data)
df = df.set_index('Technology')

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
plt.title('Technology and the Internet Market Share by Segment')

# Using sns.heatmap()
# sns.heatmap(df, annot=True, cmap="Blues", fmt='g', cbar=False, ax=ax)
# plt.yticks(rotation=0)

# Using imshow()
im = ax.imshow(df, cmap="Blues")
ax.set_xticks(np.arange(len(df.columns)))
ax.set_yticks(np.arange(len(df.index)))
ax.set_xticklabels(df.columns, rotation=45, ha='right', rotation_mode='anchor')
ax.set_yticklabels(df.index, rotation=0, ha='center')

# Adding colorbar
cbar = plt.colorbar(im, shrink=0.5)
cbar.set_label('Global Market Share')

# Automatically resize image
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Save image
plt.savefig('output/final/heatmap/png/20231228-131639_97.png', bbox_inches='tight')

# Clear current image state
plt.clf()