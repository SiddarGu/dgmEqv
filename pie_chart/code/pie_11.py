
import matplotlib.pyplot as plt

labels = ["Luxury Hotels", "Boutique Hotels", "Business Hotels", "Budget Hotels", "Resorts"]
sizes = [30, 20, 20, 15, 15]

plt.figure(figsize=(10,10)) 
ax = plt.subplot()

ax.pie(sizes, labels=labels, rotatelabels=True, autopct="%1.1f%%", startangle=90, textprops={'fontsize': 10})
ax.set_title("Hotel Accommodations in the Global Tourism Industry in 2023", fontsize=15)
plt.tight_layout()
plt.savefig('pie chart/png/326.png')
plt.cla()