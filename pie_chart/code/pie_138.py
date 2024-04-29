
import matplotlib.pyplot as plt

labels = ['Desktop Computers', 'Laptops', 'Tablets', 'Smartphones', 'Other']
sizes = [35, 30, 15, 15, 5]

fig = plt.figure(figsize=(10, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 12}, startangle=90, wedgeprops={'linewidth': 1.5})
plt.title('Distribution of Device Types Used in the USA in 2023', fontsize=14)
plt.legend(loc='upper left', bbox_to_anchor=(1, 0.5), prop={'size': 12}, shadow=True, frameon=False)
plt.tight_layout()
plt.savefig(r'pie chart/png/483.png')

plt.cla()
plt.clf()
plt.close()