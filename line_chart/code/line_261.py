
import matplotlib.pyplot as plt
plt.figure(figsize=(8,8))
ax = plt.subplot()
x_axis = ["2001","2002","2003","2004"]
y_axis_1 = [7.2,6.8,6.4,5.9]
y_axis_2 = [30000,32000,35000,40000]
y_axis_3 = [7.25,7.50,7.90,8.20]
ax.plot(x_axis,y_axis_1,label='Unemployment Rate')
ax.plot(x_axis,y_axis_2,label='Average Income(dollars)')
ax.plot(x_axis,y_axis_3,label='Minimum Wage(dollars)')
plt.title("US Employment and Income Changes from 2001 to 2004",fontsize=16)
plt.xlabel("Year",fontsize=14)
plt.ylabel("Rate/Income(dollars)",fontsize=14)
plt.xticks(x_axis,rotation=45)
plt.legend(loc='upper left',bbox_to_anchor=(0.1,1.02),ncol=3,frameon=False)
plt.tight_layout()
plt.savefig("line chart/png/518.png")
plt.clf()