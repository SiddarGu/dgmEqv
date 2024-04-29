import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import matplotlib.ticker as ticker

#Transform the data
data = """Category,Number of Institutions,Annual Visitors (Millions),Annual Revenue (Millions of Dollars),Average Admission Price (Dollars)
Museum,1200,15,980,15
Art Gallery,810,11,640,10
Theatre,650,10,720,20
Concert Hall,320,8,510,30
Opera House,220,3,460,50
Dance Studio,380,4,250,10
Film Festival,90,1,120,25
Music Festival,180,3,320,35
Comedy Club,450,5,290,15
Literary Festival,70,0.5,50,20"""
data = data.split("\n")[1:]
line_labels = [i.split(",")[0] for i in data]
data = np.array([[float(j) for j in i.split(",")[1:]] for i in data])
data_labels = ['Number of Institutions', 'Annual Visitors (Millions)', 'Annual Revenue (Millions of Dollars)', 'Average Admission Price (Dollars)']
l = len(data_labels)

#plotting
fig = plt.figure(figsize=(20,10))
ax1 = fig.add_subplot(111)
p = ["bar", "line", "scatter", "area"]
color = ['r', 'g', 'b', 'y']
for i in range(l):
    if i == 0:
        ax = ax1
        ax.bar(line_labels, data[:,i], color=color[i], alpha=0.6)
    elif p[i] == "bar":
        ax = ax.twinx()  
        ax.bar(line_labels, data[:,i], color=color[i], alpha=0.6)
    elif p[i] == "line":
        ax = ax.twinx()
        ax.plot(line_labels, data[:,i], color=color[i])
    elif p[i] == "scatter":
        ax = ax.twinx()
        ax.scatter(line_labels, data[:,i], color=color[i])
    elif p[i] == "area":
        ax = ax.twinx()
        ax.fill_between(line_labels, data[:,i], color=color[i], alpha=0.6)
    ax.set_ylabel(data_labels[i], color=color[i]) 
    ax.yaxis.label.set_color(color[i])
    ax.tick_params(axis='y', colors=color[i])
    ax.spines['right'].set_position(('outward', (i-1)*60)) 

plt.title('Arts and Culture Institutions: Their Visitors, Revenue, and Pricing')
plt.grid()
plt.tight_layout()
plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/multi-axes/png/91_2023122292141.png')
plt.clf()
