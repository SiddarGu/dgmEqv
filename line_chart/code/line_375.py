
import matplotlib.pyplot as plt 
plt.figure(figsize=(10, 8)) 
ax = plt.subplot()
ax.set_title('Pass and Drop Out Rates in Grades 8 to 12') 
ax.set_xlabel('Grade') 
ax.set_ylabel('Rate') 
ax.set_xticks(range(8, 13)) 
ax.plot(range(8, 13), [60, 70, 80, 90, 95], label='Pass Rate') 
ax.plot(range(8, 13), [15, 10, 5, 2, 1], label='Drop Out Rate') 
plt.legend(loc='best') 
plt.tight_layout() 
plt.savefig('line chart/png/199.png')
plt.clf()