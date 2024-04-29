
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax = plt.subplot(111)
xlabels = ['USA','UK','Germany','France']
e_commerce = [4.5,3.2,2.7,2.1]
retail = [5.6,6.5,4.3,3.2]
x = range(len(xlabels))
ax.bar(x=x, height=e_commerce, width=0.3, label="E-commerce Sales", color='b')
ax.bar(x=[i+0.3 for i in x], height=retail, width=0.3, label="Retail Sales", color='r')
ax.set_xticks([i+0.3/2 for i in x])
ax.set_xticklabels(xlabels, rotation=45, wrap=True)
ax.set_title('E-commerce and Retail Sales in four Countries in 2021')
ax.legend(loc='best')
plt.tight_layout()
plt.savefig('bar chart/png/128.png')
plt.clf()