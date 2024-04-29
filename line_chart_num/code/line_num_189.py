
import matplotlib.pyplot as plt
plt.figure(figsize=(15, 10))
ax = plt.subplot()
ax.plot([2001,2002,2003,2004], [3.2,3.4,3.6,3.8], '-o', label='GDP (trillion dollars)')
ax.plot([2001,2002,2003,2004], [18.2,19.2,20.2,21.2], '-o', label='GDP per Capita (thousands)')
ax.set_title('Economic Growth in the US from 2001 to 2004')
ax.set_xlabel('Year')
ax.set_ylabel('GDP (trillion dollars) / GDP per Capita (thousands)')
ax.set_xticks([2001,2002,2003,2004])
plt.legend()
for i,j in zip([2001,2002,2003,2004], [3.2,3.4,3.6,3.8]):
    ax.annotate('%s'%j, xy=(i, j))
for i,j in zip([2001,2002,2003,2004], [18.2,19.2,20.2,21.2]):
    ax.annotate('%s'%j, xy=(i, j))
plt.tight_layout()
plt.savefig('line chart/png/124.png')
plt.clf()