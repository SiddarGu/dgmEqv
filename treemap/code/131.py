# Import necessary libraries
import matplotlib.pyplot as plt
import squarify

# Data transformation
data_labels = ['Research Funding (%)']  # Labels of each column except the first one
line_labels = [
    'Psychology', 'Sociology', 'History', 'Linguistics', 
    'Anthropology', 'Political Science', 'Philosophy', 
    'Economics', 'Cultural Studies', 'Area Studies'
]  # Labels of each row except the first one
data = [18, 15, 12, 11, 9, 9, 8, 8, 5, 5]  # Numerical data array

# Plotting
fig, ax = plt.subplots(figsize=(12, 8))
squarify.plot(sizes=data, label=line_labels, alpha=0.8, text_kwargs={'wrap': True})
plt.axis('off')
plt.title('Allocation of Research Funding in Social Sciences and Humanities for 2023', fontsize=18)

# Improve layout
plt.tight_layout()

# Save the image
save_path = '/cpfs01/user/liuqi/workspace/plotchart/data_300/treemap/png/131.png'
plt.savefig(save_path, format='png', bbox_inches='tight', dpi=300)

# Clear the current figure
plt.clf()
