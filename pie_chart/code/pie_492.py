
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Create a figure
fig = plt.figure(figsize=(10,7))

# Plot pie chart
plt.pie(x=[25,35,25,15], 
        labels=['18-29','30-45','46-60','60 and Above'], 
        autopct='%.1f%%', 
        textprops={'fontsize':14}, 
        startangle=90, 
        counterclock=False, 
        wedgeprops={"edgecolor": "black"}, 
        explode=[0.02, 0, 0, 0])

# Add legend
plt.legend(labels=['18-29','30-45','46-60','60 and Above'], 
           loc='upper right', 
           bbox_to_anchor=(1.2,1.1), 
           fontsize=14, 
           bbox_transform=fig.transFigure)

# Add title
plt.title('Age Distribution of Home Owners in the USA, 2023', fontsize=18)

# Resize image
plt.tight_layout()

# Save figure
plt.savefig('pie chart/png/230.png')

# Clear the current image state
plt.clf()