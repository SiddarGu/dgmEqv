
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()
ax.bar(['USA', 'UK', 'Germany', 'France'], [2.3, 2.4, 2.2, 2.1], label='Hospital Beds/1000 People')
ax.bar(['USA', 'UK', 'Germany', 'France'], [2.5, 2.6, 2.4, 2.3], bottom=[2.3, 2.4, 2.2, 2.1], label='Doctors/1000 People')
ax.set_xticks(['USA', 'UK', 'Germany', 'France'])
ax.legend()
ax.set_title('Healthcare resources availability in four countries in 2021')
plt.tight_layout()
plt.savefig('bar chart/png/284.png')
plt.clf()