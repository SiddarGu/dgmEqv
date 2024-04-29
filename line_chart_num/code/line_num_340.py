
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))
ax = plt.subplot()
ax.plot(['20','25','30','35','40','45','50','55','60'], [20.2,22.1,25.3,27.3,29.8,31.5,33.4,35.2,37.2], 'r-o')
plt.title('Average BMI of people in different age groups')
plt.xticks(['20','25','30','35','40','45','50','55','60'])
for a,b in zip(['20','25','30','35','40','45','50','55','60'], [20.2,22.1,25.3,27.3,29.8,31.5,33.4,35.2,37.2]): 
    plt.text(a, b, str(b), fontsize=10, rotation=45, ha='center', va='bottom')
plt.grid(linestyle='--', linewidth=0.5)
ax.legend(['Average BMI'])
plt.tight_layout()
plt.savefig('line chart/png/530.png')
plt.clf()