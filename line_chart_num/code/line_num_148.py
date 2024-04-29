
import matplotlib.pyplot as plt
plt.figure(figsize=(7,5))
plt.plot(['Jan','Feb','Mar','Apr'],[1000,1200,800,1500],'b-o',label='Manufacturing A(units)')
plt.plot(['Jan','Feb','Mar','Apr'],[800,900,1100,1200],'g-o',label='Manufacturing B(units)')
plt.plot(['Jan','Feb','Mar','Apr'],[1200,1100,1300,1400],'r-o',label='Manufacturing C(units)')
plt.plot(['Jan','Feb','Mar','Apr'],[1500,1600,1200,800],'y-o',label='Manufacturing D(units)')
plt.xticks(['Jan','Feb','Mar','Apr'])
plt.title('Units of manufactured items by four categories in the first four months of 2021')
plt.xlabel('Month')
plt.ylabel('Units')
for a,b in zip(['Jan','Feb','Mar','Apr'],[1000,1200,800,1500]):
    plt.annotate(str(b),xy=(a,b),xytext=(-20,10),textcoords='offset points')
for a,b in zip(['Jan','Feb','Mar','Apr'],[800,900,1100,1200]):
    plt.annotate(str(b),xy=(a,b),xytext=(-20,10),textcoords='offset points')
for a,b in zip(['Jan','Feb','Mar','Apr'],[1200,1100,1300,1400]):
    plt.annotate(str(b),xy=(a,b),xytext=(-20,10),textcoords='offset points')
for a,b in zip(['Jan','Feb','Mar','Apr'],[1500,1600,1200,800]):
    plt.annotate(str(b),xy=(a,b),xytext=(-20,10),textcoords='offset points')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('./line chart/png/314.png')
plt.clf()