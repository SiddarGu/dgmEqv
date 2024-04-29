
import matplotlib.pyplot as plt
import numpy as np

#Prepare data
x = np.arange(4)
Month = ['January', 'February', 'March', 'April']
Truck_Fleet = [100, 120, 110, 130]
Train_Fleet = [20, 25, 22, 21]
Air_Fleet = [30, 35, 32, 38]

#Create figure
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot()

#Plot data
ax.plot(x, Truck_Fleet, color='blue', marker='o', label='Truck Fleet')
ax.plot(x, Train_Fleet, color='red', marker='*', label='Train Fleet')
ax.plot(x, Air_Fleet, color='green', marker='^', label='Air Fleet')

#Set xticks
ax.set_xticks(x)
ax.set_xticklabels(Month, rotation=45, ha='right', wrap=True)

#Set chart title
ax.set_title('Fleet Changes of Three Transportation Modes from January to April, 2021')

#Set legend
ax.legend()

#Resize image and save
plt.tight_layout()
plt.savefig('line chart/png/61.png')

#Clear current image state
plt.clf()