
import matplotlib.pyplot as plt
plt.figure(figsize=(14, 7))
plt.plot(['Jan', 'Feb', 'Mar', 'Apr'], [1000, 1200, 1400, 1300], label='Revenue A')
plt.plot(['Jan', 'Feb', 'Mar', 'Apr'], [1100, 1300, 1600, 1400], label='Revenue B')
plt.plot(['Jan', 'Feb', 'Mar', 'Apr'], [1300, 1500, 1700, 1800], label='Revenue C')
plt.title('Revenue of three food and beverage companies in 2021')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.legend(loc='best')
plt.xticks(rotation=45, wrap=True)
plt.tight_layout()
plt.savefig('line chart/png/43.png')
plt.clf()