import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

data_text = 'City,Property Value (Million $),Population (Millions),Rental Price ($),Unemployment Rate (%),Property Type/n New York,3000,8.5,2800,10,Duplex/n Los Angeles,2700,4,3100,9,Semi-detached/n Chicago,2100,2.7,1800,11,Condominium/n Houston,1900,2.3,2200,5,Single Family/n Phoenix,1400,1.6,1300,5,Townhouse/n Philadelphia,1200,1.6,1400,6,Apartment/n San Antonio,1100,1.5,1600,4,Detached/n Dallas,1000,1.3,2000,4,Bungalow/n San Diego,900,1.4,2500,3,Duplex/n San Jose,800,1,3500,2,Semi-detached'
data_text = data_text.split('/n')

data_labels = data_text[0].split(',')[1:]
data = [d.split(',')[1:-1] for d in data_text[1:]]
line_labels = [d.split(',')[0] + ' ' + d.split(',')[-1] for d in data_text[1:]]

data = np.array(data, dtype=float)

fig, ax = plt.subplots(figsize=(14, 10))
cmap = cm.get_cmap('viridis')

for i in range(len(data)):
    ax.scatter(data[i, 0], data[i, 1], s=(data[i, 2]-data[:, 2].min())/(data[:, 2].max()-data[:, 2].min())*4400+600, c=cmap((data[i, 3]-data[:, 3].min())/(data[:, 3].max()-data[:, 3].min())), label=None)
    ax.scatter([], [], label=line_labels[i] + f' {data[i, 2]}', s=20, color=cmap((data[i, 3]-data[:, 3].min())/(data[:, 3].max()-data[:, 3].min())))

ax.legend(title=data_labels[2])
plt.colorbar(cm.ScalarMappable(norm=Normalize(data[:, 3].min(), data[:, 3].max()), cmap=cmap), ax=ax, label=data_labels[3])

plt.grid()
plt.title('Comparison of Real Estate and Housing Markets across Major US Cities')
plt.xlabel(data_labels[0])
plt.ylabel(data_labels[1])
plt.tight_layout()

plt.savefig('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/bubble/png/146_202312301731.png')
plt.clf()
