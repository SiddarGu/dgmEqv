
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# set figure size
plt.figure(figsize=(6,6))

# set labels
causes = ["Education", "Healthcare", "Animal Welfare", "Disaster Relief", "Social Welfare", "Environmental Issues", "Other"]
donations_share = [30, 20, 15, 10, 10, 10, 5]

# plot pie chart
plt.pie(donations_share, labels=causes, autopct='%1.1f%%', startangle=90, shadow=True, rotatelabels=True, textprops={'fontsize': 14, 'wrap':True})

# set title
plt.title("Donation Distribution among Nonprofit Causes in the USA, 2023", fontsize=14)

# adjust and save figure
plt.tight_layout()
plt.savefig("pie chart/png/111.png")

# clear current image state
plt.clf()