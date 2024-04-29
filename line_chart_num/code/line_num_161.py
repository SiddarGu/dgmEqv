
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,6,7,8,9])
y1 = np.array([89,87,90,92,94])
y2 = np.array([86,91,94,97,99])
y3 = np.array([90,89,92,94,96])

fig = plt.figure(figsize=(10,8))
plt.plot(x,y1,label='Average Math Score')
plt.plot(x,y2,label='Average Science Score')
plt.plot(x,y3,label='Average English Score')
plt.xticks(x)
plt.xlabel('Grade')
plt.ylabel('Score')
plt.title('Average scores of Math, Science and English in different grades')
plt.legend(loc='best')

for a,b,c in zip(x,y1,y2):
    plt.text(a,b+0.2,b,ha='center',va='center',rotation=0,wrap=True)
    plt.text(a,c+0.2,c,ha='center',va='center',rotation=0,wrap=True)

for a,b,c in zip(x,y1,y3):
    plt.text(a,b-0.2,b,ha='center',va='center',rotation=0,wrap=True)
    plt.text(a,c-0.2,c,ha='center',va='center',rotation=0,wrap=True)

for a,b,c in zip(x,y2,y3):
    plt.text(a,b,b,ha='center',va='center',rotation=0,wrap=True)
    plt.text(a,c,c,ha='center',va='center',rotation=0,wrap=True)

plt.tight_layout()
plt.savefig('line chart/png/66.png')
plt.clf()