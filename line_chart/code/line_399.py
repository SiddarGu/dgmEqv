
import matplotlib.pyplot as plt 

x=['January','February','March','April','May','June','July','August'] 
y1=[100,150,175,225,200,125,150,175] 
y2=[200,250,275,325,300,225,250,275] 
y3=[300,400,450,500,400,350,400,450] 

fig=plt.figure(figsize=(8,5)) 
ax=fig.add_subplot(1,1,1) 
ax.plot(x,y1,c='r',label='Output A(tonnes)',marker='o') 
ax.plot(x,y2,c='b',label='Output B(tonnes)',marker='s') 
ax.plot(x,y3,c='g',label='Output C(tonnes)',marker='^') 

ax.set_xticks(x) 
ax.grid() 
ax.legend(loc='upper left') 
ax.set_title('Manufacturing output trend in the first half of 2023') 
plt.tight_layout() 
plt.savefig('line chart/png/229.png') 
plt.clf()