
import matplotlib.pyplot as plt
import numpy as np

year = np.array([2001,2002,2003,2004])
production_a=np.array([500,600,400,700])
production_b=np.array([900,1000,800,1100])
production_c=np.array([1100,1200,1000,1300])
production_d=np.array([1300,1400,1200,1500])

plt.figure(figsize=(10,6))
plt.plot(year, production_a,label='Production A')
plt.plot(year, production_b,label='Production B')
plt.plot(year, production_c,label='Production C')
plt.plot(year, production_d,label='Production D')
plt.xticks(year)
plt.title('Production of four types of products in the manufacturing industry')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('line chart/png/534.png')
plt.clf()