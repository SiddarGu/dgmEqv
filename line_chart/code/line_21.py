
import matplotlib.pyplot as plt

plt.figure(figsize=(14,7))
plt.plot(['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August'],
         [100, 105, 115, 120, 125, 130, 135, 140],
         label='Online users (million)')
plt.plot(['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August'],
         [200, 220, 250, 270, 290, 310, 330, 350],
         label='Number of devices')
plt.title('Increase of online users and devices in 2020')
plt.xlabel('Month')
plt.ylabel('Unit')
plt.xticks(rotation=45, ha='right', wrap=True)
plt.legend(loc='best')
plt.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/214.png')
plt.clf()