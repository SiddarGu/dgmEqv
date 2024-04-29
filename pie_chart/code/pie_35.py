
import matplotlib.pyplot as plt
import numpy as np

# Define data
Platforms = ['Facebook', 'YouTube', 'Instagram', 'Twitter', 'Reddit', 'Snapchat', 'LinkedIn', 'Other']
Percentage = [38, 19, 12, 8, 5, 5, 5, 8]
colors = ['#f7cac9', '#fad0c3', '#fef3cd', '#e2f0d9', '#c7ebe5', '#b1e2f2', '#9cdcfd', '#b3b3b3']

# Create figure
plt.figure(figsize=(8, 8))

# Plot
wedges, texts, autotexts = plt.pie(Percentage, autopct='%1.1f%%', colors=colors,
                                  wedgeprops={'edgecolor': 'black'},
                                  textprops={'fontsize': 14, 'color': 'black'})
plt.legend(wedges, Platforms, 
            title="Platforms",
            loc="center left", 
            bbox_to_anchor=(1, 0, 0.5, 1))
plt.setp(autotexts, size=12, weight='bold')
plt.setp(texts, size=12, weight='bold') 
plt.title('Social Media Platform Usage in the USA, 2023')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('pie chart/png/312.png', bbox_inches='tight')
plt.clf()