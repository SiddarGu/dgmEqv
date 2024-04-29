
import matplotlib.pyplot as plt
import numpy as np

#Create figure
fig=plt.figure(figsize=(10,6))

#Define data
data=np.array([[50000,10000],[40000,13000],[60000,9000],[70000,11000]])

#Define labels
countries = ['USA','UK','Germany','France']
production=['Cereal Production(tonnes)','Protein Production(tonnes)']

#Plot data
plt.xticks(np.arange(len(countries)),countries)

#Plot bars
for i in range(data.shape[1]):
    plt.bar(np.arange(len(countries)),data[:,i],bottom= np.sum(data[:,:i],axis=1),label=production[i])

#Adjust figure
plt.title('Cereal and Protein Production in four countries in 2021')
plt.legend(loc='upper center')
plt.tight_layout()

#Label the value of each data point
for i in range(data.shape[1]):
    for j in range(data.shape[0]):
        plt.annotate(data[j,i],xy=(j,data[j,i]),rotation=90,ha='center',va='bottom')

#Save figure
fig.savefig('Bar Chart/png/81.png')

#Clear the current image state
plt.clf()