
import matplotlib.pyplot as plt
import numpy as np

#Data
Month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
Production_A = [15, 19, 17, 22, 20, 18, 17, 15, 19, 22, 20, 17]
Production_B = [18, 17, 19, 21, 22, 20, 19, 15, 18, 20, 19, 17]
Production_C = [20, 22, 23, 25, 24, 24, 23, 21, 24, 25, 23, 22]

#Set figure size
plt.figure(figsize=(14,7))

#Plot
plt.plot(Month, Production_A, label='Production A', marker='o')
plt.plot(Month, Production_B, label='Production B', marker='o')
plt.plot(Month, Production_C, label='Production C', marker='o')

#Label
plt.title('Production of three types of products in 2021')
plt.xlabel('Month')
plt.ylabel('Production(million)')

#Show legend
plt.legend(loc='upper left')

#Annotate
for x,y in zip(Month, Production_A):
    plt.annotate(f'{y}', xy=(x,y), xytext=(-20,10), textcoords='offset points')
for x,y in zip(Month, Production_B):
    plt.annotate(f'{y}', xy=(x,y), xytext=(-20,10), textcoords='offset points')
for x,y in zip(Month, Production_C):
    plt.annotate(f'{y}', xy=(x,y), xytext=(-20,10), textcoords='offset points')

#Set ticks
plt.xticks(Month)

#Resize
plt.tight_layout()

#Save
plt.savefig('line chart/png/264.png')

#Clear
plt.clf()