
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
fig = plt.figure(figsize=(10, 6))
gs = gridspec.GridSpec(1, 1)
ax = fig.add_subplot(gs[0, 0])
ax.bar(Country, Crops, width=0.4, label="Crops", color='#f7a072', bottom=Livestock)
ax.bar(Country, Livestock, width=0.4, label="Livestock", color='#3bb4c1')
ax.set_xticks(Country)
ax.set_xticklabels(Country, fontsize=10, rotation=45)
ax.set_title("Number of crops and livestock in four countries in 2021")
ax.set_ylabel("Number of crops and livestock")
ax.set_xlabel("Country")
ax.legend(loc='upper left')
for i, v in enumerate(Crops+Livestock):
    ax.text(i-0.2, v+1000, str(v), color='#000000', fontweight='bold')
plt.tight_layout()
plt.savefig('Bar Chart/png/227.png')
plt.clf()