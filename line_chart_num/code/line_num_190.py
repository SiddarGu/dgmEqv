
import matplotlib.pyplot as plt
import numpy as np

# Government Spending in Infrastructure, Education and Healthcare in the US from 2001 to 2005

# Create figure
fig = plt.figure()
ax = fig.add_subplot(111)

# Data
x = np.array(['2001','2002','2003','2004','2005'])
y_infrastructure = np.array([800,900,1000,1100,1200])
y_education = np.array([200,250,300,350,400])
y_healthcare = np.array([400,450,500,550,600])

# Plotting
ax.plot(x,y_infrastructure,label='Infrastructure')
ax.plot(x,y_education,label='Education')
ax.plot(x,y_healthcare,label='Healthcare')

# Setting
ax.set_xticks(x)
ax.set_title('Government Spending in Infrastructure, Education and Healthcare in the US from 2001 to 2005')
ax.legend()
ax.grid(True,color='black',linestyle='-',linewidth=0.2)

# Labeling 
for i,j in enumerate(y_infrastructure):
    ax.annotate(str(j),xy=(x[i],y_infrastructure[i]),rotation=90)
for i,j in enumerate(y_education):
    ax.annotate(str(j),xy=(x[i],y_education[i]),rotation=90)
for i,j in enumerate(y_healthcare):
    ax.annotate(str(j),xy=(x[i],y_healthcare[i]),rotation=90)

# Resize
plt.tight_layout()

# Save
plt.savefig('line chart/png/346.png')

# Clear
plt.cla()