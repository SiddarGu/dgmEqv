
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.plot([15,16,17,18,19,20,21,22], [90,95,92,89,85,80,75,70], color='blue', linestyle='solid', marker='o', markerfacecolor='red', markersize=10)
plt.title('Average SAT Score Changes among Age Groups from 15-22')
plt.xlabel('Age')
plt.ylabel('Average Score')
plt.xticks([15,16,17,18,19,20,21,22])
plt.tight_layout()
plt.savefig('line chart/png/234.png',dpi=300)
plt.clf()