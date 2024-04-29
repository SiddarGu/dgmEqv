
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
plt.figure(figsize=(10,7))

x_data = [2001,2002,2003,2004]
y_data_A = [500,600,400,700]
y_data_B = [400,500,700,600]
y_data_C = [600,800,1000,900]
y_data_D = [700,900,700,500]

ax = plt.subplot()
ax.plot(x_data,y_data_A,label='Movie A',linestyle='-',color='tab:red',marker='o')
ax.plot(x_data,y_data_B,label='Movie B',linestyle='-',color='tab:green',marker='o')
ax.plot(x_data,y_data_C,label='Movie C',linestyle='-',color='tab:blue',marker='o')
ax.plot(x_data,y_data_D,label='Movie D',linestyle='-',color='tab:orange',marker='o')

ax.legend(loc='upper left',fontsize=12)
ax.set_title('Ticket sales of four movies in the US from 2001 to 2004',fontsize=14)
ax.set_xlabel('Year',fontsize=14)
ax.set_ylabel('Million of tickets',fontsize=14)
ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

for x,y_A,y_B,y_C,y_D in zip(x_data,y_data_A,y_data_B,y_data_C,y_data_D):
    ax.annotate('{:.0f}'.format(y_A),(x,y_A+50), xytext=(0,2), textcoords='offset points',rotation=45,fontsize=12,color='tab:red')
    ax.annotate('{:.0f}'.format(y_B),(x,y_B+50), xytext=(0,2), textcoords='offset points',rotation=45,fontsize=12,color='tab:green')
    ax.annotate('{:.0f}'.format(y_C),(x,y_C+50), xytext=(0,2), textcoords='offset points',rotation=45,fontsize=12,color='tab:blue')
    ax.annotate('{:.0f}'.format(y_D),(x,y_D+50), xytext=(0,2), textcoords='offset points',rotation=45,fontsize=12,color='tab:orange')

plt.tight_layout()
plt.savefig('line chart/png/8.png')
plt.clf()