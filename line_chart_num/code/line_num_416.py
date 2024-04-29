

import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax = plt.subplot()
ax.plot(['January','February','March','April','May','June'], [100,150,120,200,180,220], label='Product A')
ax.plot(['January','February','March','April','May','June'], [200,250,220,300,280,320], label='Product B')
ax.plot(['January','February','March','April','May','June'], [300,350,320,400,380,420], label='Product C')
ax.plot(['January','February','March','April','May','June'], [400,450,420,500,480,520], label='Product D')
ax.set_title('Manufacturing Output in Four Different Products in 2021')
ax.set_xlabel('Month')
ax.set_ylabel('Units')
ax.legend()
ax.grid(True)
for x, y in zip(['January','February','March','April','May','June'], [100,150,120,200,180,220]):
    ax.annotate(str(y), xy=(x, y), xytext=(-10, 10), textcoords='offset points',rotation=45, wrap=True)
for x, y in zip(['January','February','March','April','May','June'], [200,250,220,300,280,320]):
    ax.annotate(str(y), xy=(x, y), xytext=(-10, 10), textcoords='offset points',rotation=45, wrap=True)
for x, y in zip(['January','February','March','April','May','June'], [300,350,320,400,380,420]):
    ax.annotate(str(y), xy=(x, y), xytext=(-10, 10), textcoords='offset points',rotation=45, wrap=True)
for x, y in zip(['January','February','March','April','May','June'], [400,450,420,500,480,520]):
    ax.annotate(str(y), xy=(x, y), xytext=(-10, 10), textcoords='offset points',rotation=45, wrap=True)
plt.xticks(['January','February','March','April','May','June'])
plt.tight_layout()
plt.savefig('line chart/png/168.png')
plt.clf()