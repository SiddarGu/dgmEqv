
import matplotlib.pyplot as plt

labels = ["Smartphones", "Desktops", "Tablets", "Wearables", "Other"]
values = [45,25,15,7,8]

fig = plt.figure(figsize=(9,7))
ax = fig.add_subplot()
ax.pie(values, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 12})
ax.set_title("Distribution of Internet-Connected Devices in 2023")
plt.tight_layout()
plt.savefig('pie chart/png/86.png')
plt.clf()