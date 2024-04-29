
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

products =  ["Automobiles", "Electronics", "Furniture", "Clothing", "Machinery"]
percentage = [20, 25, 15, 20, 20]

plt.figure(figsize=(8, 6), dpi=100)
plt.suptitle('Distribution of Manufacturing Products in the USA, 2023', fontsize=14)

gs = gridspec.GridSpec(1, 2, width_ratios=[1, 2])

ax1 = plt.subplot(gs[0])
ax1.pie(percentage, labels=products, autopct='%.2f%%', startangle=90)
ax1.set_title("Product Percentages")

ax2 = plt.subplot(gs[1])
ax2.bar(products, percentage, color='#6699CC', width=0.6)
ax2.set_title("Product Percentages")
ax2.set_xlabel("Products")
ax2.set_ylabel("Percentage")
ax2.set_xticklabels(products, rotation=-45, ha='left')

plt.tight_layout(pad=3)
plt.savefig('pie chart/png/489.png')
plt.clf()