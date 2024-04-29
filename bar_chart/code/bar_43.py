
import matplotlib.pyplot as plt
import numpy as np

data = [[500,1000],[400,900],[350,800],[450,1100]]

plt.figure(figsize=(12,8))
ax = plt.subplot(111)

width = 0.8
ticks = np.arange(4)

ax.bar(ticks-width/2, [i[0] for i in data], width=width, label='Number of Lawyers')
ax.bar(ticks+width/2, [i[1] for i in data], width=width, label='Number of Cases')

plt.xticks(ticks, ('Civil Law', 'Criminal Law', 'Tax Law', 'Contract Law'))
ax.set_title('Number of Lawyers and Cases under four types of law in 2021')
ax.legend(loc="upper left")

plt.tight_layout()
plt.savefig('bar chart/png/372.png')
plt.clf()