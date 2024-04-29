
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.plot(['January', 'February', 'March', 'April', 'May', 'June'], [1000, 1200, 900, 1100, 1500, 1300], label='Truck')
ax.plot(['January', 'February', 'March', 'April', 'May', 'June'], [200, 400, 100, 500, 700, 300], label='Plane')
ax.plot(['January', 'February', 'March', 'April', 'May', 'June'], [300, 500, 400, 600, 800, 700], label='Ship')
ax.set_title('Freight shipment of trucks, planes and ships in 2020')
ax.set_xticks(['January', 'February', 'March', 'April', 'May', 'June'])
ax.legend()
for x, y in zip(['January', 'February', 'March', 'April', 'May', 'June'], [1000, 1200, 900, 1100, 1500, 1300]):
    ax.annotate(y, xy=(x, y), xytext=(0, -8), textcoords='offset pixels', ha='center', va='top')
for x, y in zip(['January', 'February', 'March', 'April', 'May', 'June'], [200, 400, 100, 500, 700, 300]):
    ax.annotate(y, xy=(x, y), xytext=(0, 8), textcoords='offset pixels', ha='center', va='bottom')
for x, y in zip(['January', 'February', 'March', 'April', 'May', 'June'], [300, 500, 400, 600, 800, 700]):
    ax.annotate(y, xy=(x, y), xytext=(0, 0), textcoords='offset pixels', ha='center', va='center')
plt.tight_layout()
plt.savefig('line chart/png/225.png')
plt.clf()