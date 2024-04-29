
import matplotlib.pyplot as plt
import matplotlib as mpl

# Set figure size
plt.figure(figsize=(7,7)) 

# Create pie chart
labels =['Voting', 'Direct Democracy', 'Representative Democracy', 'Totalitarianism']
sizes=[30,25,35,10]
explode = [0,0,0,0.1]
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Add title
plt.title('Popular Government Systems in the World, 2023')

# Add legend
plt.legend(labels, loc="best", bbox_to_anchor=(1, 0.5), shadow=True, ncol=1)

# Draw pie chart
patches, texts, autotexts = plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct="%1.1f%%", shadow=True, startangle=90)

# Avoid text being overwritten
plt.setp(autotexts, size=8, weight="bold", rotation=30)

# Automatically resize the image by tight_layout()
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/9.png')

# Clear the current image state
plt.clf()