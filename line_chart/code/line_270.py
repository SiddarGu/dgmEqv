
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
plt.plot(["January", "February", "March", "April", "May", "June", "July", "August"],[12000,15000,13500,17000,18000,19000,20000,19500],marker='o')
plt.xticks(["January", "February", "March", "April", "May", "June", "July", "August"])
plt.xlabel('Month')
plt.ylabel('Number of Visitors')
plt.title('Yearly Visitor Numbers to New York City from January to August 2023')
plt.grid()
plt.tight_layout()
plt.savefig('line chart/png/353.png')
plt.clf()