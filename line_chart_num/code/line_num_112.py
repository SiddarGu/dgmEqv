
import matplotlib.pyplot as plt
import numpy as np

age = ['20-29','30-39','40-49','50-59','60-69','70-79']
salary = [50000,70000,90000,100000,120000,140000]
package = ['Basic','Basic','Medium','Medium','Advanced','Advanced']

plt.figure(figsize=(10,5))
plt.plot(age, salary, marker='o',color='green',label='Salary')
plt.xticks(np.arange(len(age)), age)
plt.title('Salary and Benefit Package for Employees in Different Age Groups')

for x,y in zip(age,salary):
    plt.annotate(package[age.index(x)], 
                 xy=(age.index(x),y),
                 xytext=(-20, 10),
                 textcoords='offset points',
                 fontsize=10,
                 rotation=90,
                 bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5',color='red'))

plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('line chart/png/552.png', dpi=300)
plt.clf()