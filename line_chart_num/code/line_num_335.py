
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(1, 1, 1)
ax.plot(['Los Angeles','New York','Chicago','Austin'],
        [2.7,3.1,2.2,1.8], label="Average Home Price (million dollars)")
ax.plot(['Los Angeles','New York','Chicago','Austin'],
        [1.2,1.5,1.0,0.9], label="Average Apartment Price (million dollars)")
ax.plot(['Los Angeles','New York','Chicago','Austin'],
        [1700,1400,1800,1450], label="Average Home Size (square feet)")
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1),
          ncol=3, fancybox=True, shadow=True)
ax.set_title('Comparative Real Estate Prices and Average Home Sizes in Major US Cities')
ax.set_xlabel('City')
ax.set_ylabel('Price/Size (million dollars/square feet)')
for i, txt in enumerate(['Los Angeles','New York','Chicago','Austin']):
    ax.annotate(txt, (i,ax.get_ylim()[1]))
plt.xticks([0,1,2,3],['Los Angeles','New York','Chicago','Austin'])
plt.tight_layout()
plt.savefig('line chart/png/208.png')
plt.clf()