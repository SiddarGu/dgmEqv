

import matplotlib.pyplot as plt
import numpy as np

#Create figure
fig=plt.figure()
ax = fig.add_subplot()

#Plot the data
state=['California','New York','Texas','Florida']
Public_Policy_A=[10,20,15,18]
Public_Policy_B=[20,30,25,28]
Public_Policy_C=[30,40,35,38]

width = 0.2
x = np.arange(len(state))
ax.bar(x - width, Public_Policy_A, width, label='Public Policy A')
ax.bar(x , Public_Policy_B, width, label='Public Policy B')
ax.bar(x + width, Public_Policy_C, width, label='Public Policy C')

#Set axis labels
ax.set_xticks(x)
ax.set_xticklabels(state)
ax.set_ylabel('implementation')
ax.set_title('Public policy implementation in four states in 2021')
ax.legend()

#Display the value of each data point for every variables directly on the figure
for x_val, y_val in zip(x, Public_Policy_A):
    plt.text(x_val - width/2, y_val + 0.5, str(y_val))

for x_val, y_val in zip(x, Public_Policy_B):
    plt.text(x_val - width/2, y_val + 0.5, str(y_val))

for x_val, y_val in zip(x, Public_Policy_C):
    plt.text(x_val - width/2, y_val + 0.5, str(y_val))

#Resize the image
fig.tight_layout()

#Save the figure
plt.savefig('Bar Chart/png/73.png')

#Clear the current image state 
plt.clf()