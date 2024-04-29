
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111)

industries = ["Automobile","Electronics","Food Processing","Aerospace","Pharmaceuticals","Textiles","Chemicals"]
production_share = [20,30,15,10,15,5,5]
colors = ["#0066cc", "#009900", "#ff9900","#ff3300","#99ccff","#990099","#999966"]
ax.pie(production_share, labels=industries, colors=colors, autopct='%1.1f%%',
        startangle=90, wedgeprops={'linewidth': 2, 'edgecolor':'white'})

ax.set_title("Share of Production Across Different Industries in 2023")
ax.legend(loc="upper right", bbox_to_anchor=(1, 1))

plt.tight_layout()
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor") 
plt.savefig("pie chart/png/292.png")
plt.clf()