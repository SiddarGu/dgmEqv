
fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(['January','February','March','April','May'], [1000, 1100, 1300, 1400, 1600], label='Truck Mileage(thousand miles)', marker='o')
ax.plot(['January','February','March','April','May'], [200, 400, 600, 800, 1000], label='Train Mileage(thousand miles)', marker='o')
ax.plot(['January','February','March','April','May'], [500, 700, 900, 1200, 1500], label='Plane Mileage(thousand miles)', marker='o')
for a,b in zip(['January','February','March','April','May'], [1000, 1100, 1300, 1400, 1600]): 
    plt.text(a, b, b, ha='center', va='bottom',fontsize=12)
for a,b in zip(['January','February','March','April','May'], [200, 400, 600, 800, 1000]): 
    plt.text(a, b, b, ha='center', va='bottom',fontsize=12)
for a,b in zip(['January','February','March','April','May'], [500, 700, 900, 1200, 1500]): 
    plt.text(a, b, b, ha='center', va='bottom',fontsize=12)
ax.set_title('Transportation Usage in the US from January to May 2020', fontsize=15)
ax.grid(True, linestyle='--', color='grey', linewidth=1, alpha=0.5)
ax.legend(loc='best')
ax.set_xticks(['January','February','March','April','May'])
plt.tight_layout()
plt.savefig('line chart/png/174.png')
plt.clf()