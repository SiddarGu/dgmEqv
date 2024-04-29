
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.plot([18,26,36,46,56,66], [100,150,200,250,200,100], color="darkorange", marker= 'o', linewidth=3)
ax.set_title('Number of Employees in Different Age Groups in an Organization')
ax.set_xlabel('Age')
ax.set_ylabel('Number of Employees')
ax.set_xticks([18,26,36,46,56,66])
ax.grid(color='lightgray', linestyle='-', linewidth=1)
plt.tight_layout()
plt.savefig('line chart/png/77.png')
plt.clf()