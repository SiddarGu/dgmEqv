
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(1,1,1)
country = ['USA','UK','Germany','France']
criminal = [200000,250000,220000,240000]
civil = [180000,220000,200000,190000]
ax.bar(country, criminal, label = 'Criminal Cases', bottom = civil, color = 'r')
ax.bar(country, civil, label = 'Civil Cases', color = 'b')
ax.set_title('Number of criminal and civil cases in four countries in 2021')
ax.set_xticklabels(country, rotation=0, wrap=True)
ax.legend()
plt.tight_layout()
plt.savefig(r'bar chart/png/320.png')
plt.clf()