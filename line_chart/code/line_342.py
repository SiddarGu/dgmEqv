
import matplotlib.pyplot as plt

x = [1,2,3,4]
m = [2,2.5,3,3.5]
l = [1,1.2,1.5,1.8]
t = [3,2.5,2,1.5]
f = [20,25,30,35]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111)
ax.plot(x,m, label='Mass(kg)')
ax.plot(x,l, label='Length(m)')
ax.plot(x,t, label='Time(s)')
ax.plot(x,f, label='Force(N)')
ax.legend(loc='upper center',bbox_to_anchor=(0.5,0.95),ncol=4,fancybox=True,shadow=True,fontsize='small')
ax.set_title('The Relationship between Mass, Length, Time and Force in a Physics Experiment', fontsize='large')
ax.set_xlabel('Experiment')
ax.set_xticks(x)
ax.set_ylabel('Value')
plt.tight_layout()
plt.savefig('line_342.png')
plt.clf()