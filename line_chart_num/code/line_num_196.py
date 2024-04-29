
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,6))
plt.title('Voter Turnout, Unemployment Rate, Inflation Rate and Welfare Spending in the US from 2000 to 2004')
plt.plot([2000,2001,2002,2003,2004], [60,62,64,58,56], label='Voter Turnout(%)')
plt.plot([2000,2001,2002,2003,2004], [4.2,4.6,4.1,5.3,4.8], label='Unemployment Rate(%)')
plt.plot([2000,2001,2002,2003,2004], [2.2,2.7,2.2,3.5,3.0], label='Inflation Rate(%)')
plt.plot([2000,2001,2002,2003,2004], [20,22,24,26,28], label='Welfare Spending(billion dollars)')
plt.xticks([2000,2001,2002,2003,2004])
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
for i,j in zip([2000,2001,2002,2003,2004], [60,62,64,58,56]):
    plt.annotate(str(j),xy=(i,j))
for i,j in zip([2000,2001,2002,2003,2004], [4.2,4.6,4.1,5.3,4.8]):
    plt.annotate(str(j),xy=(i,j))
for i,j in zip([2000,2001,2002,2003,2004], [2.2,2.7,2.2,3.5,3.0]):
    plt.annotate(str(j),xy=(i,j))
for i,j in zip([2000,2001,2002,2003,2004], [20,22,24,26,28]):
    plt.annotate(str(j),xy=(i,j))
plt.tight_layout()
plt.savefig('line chart/png/121.png')
plt.clf()