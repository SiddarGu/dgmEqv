
import matplotlib.pyplot as plt 
 
# Create figure and set figsize 
fig = plt.figure(figsize=(6, 6)) 
 
# Set data 
political_party = ["Democratic", "Republican", "Libertarian", "Green Party", "Constitution Party", "Other"] 
votes = [36, 30, 10, 8, 4, 12] 
 
# Plot pie chart 
ax = fig.add_subplot() 
ax.pie(votes, labels=political_party, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10}, 
        wedgeprops={'linewidth': 1, 'edgecolor': 'white'}, rotatelabels=True, shadow=True) 
 
# Set title 
plt.title("Party Affiliation in the USA in 2023") 
 
# Automatically resize the image 
plt.tight_layout() 
 
# Save image 
plt.savefig(r'pie chart/png/286.png') 
 
# Clear the current image state 
plt.clf()