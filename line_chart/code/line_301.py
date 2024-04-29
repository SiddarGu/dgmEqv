
import matplotlib.pyplot as plt
plt.figure(figsize=(12,6))

x = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August']
y_car = [400, 600, 800, 1000, 900, 800, 700, 500]
y_truck = [500, 700, 900, 650, 550, 650, 600, 800]
y_train = [800, 400, 500, 700, 600, 700, 800, 900]

plt.plot(x, y_car, label='Car Shipping(tonnes)', marker='o', linestyle='--')
plt.plot(x, y_truck, label='Truck Shipping(tonnes)', marker='^', linestyle='-.')
plt.plot(x, y_train, label='Train Shipping(tonnes)', marker='s', linestyle=':')

plt.xticks(rotation=45)
plt.title('Transportation of goods by different modes in the US from January to August 2021')
plt.legend(bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.savefig('line chart/png/446.png')
plt.clf()