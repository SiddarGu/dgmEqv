
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.plot(['January','February','March','April','May','June','July','August'],[1000,1200,1400,1300,1500,1400,1600,1700],'b-o',label='Air Transport (million ton-km)')
plt.plot(['January','February','March','April','May','June','July','August'],[3000,3500,4000,4200,3800,3600,3000,3500],'g-o',label='Railway (million ton-km)')
plt.plot(['January','February','March','April','May','June','July','August'],[5000,4500,5500,6000,5500,6000,5500,6000],'r-o',label='Road (million ton-km)')
plt.xticks(['January','February','March','April','May','June','July','August'])
plt.title('Transportation of goods in China in 2021')
plt.xlabel('Month')
plt.ylabel('Ton-km (million)')
plt.grid(True)
plt.legend(loc='best')
for a,b in zip(['January','February','March','April','May','June','July','August'],[1000,1200,1400,1300,1500,1400,1600,1700]):
    plt.text(a,b+50,b,ha='center',va='bottom',fontsize=10)
for a,b in zip(['January','February','March','April','May','June','July','August'],[3000,3500,4000,4200,3800,3600,3000,3500]):
    plt.text(a,b+50,b,ha='center',va='bottom',fontsize=10)
for a,b in zip(['January','February','March','April','May','June','July','August'],[5000,4500,5500,6000,5500,6000,5500,6000]):
    plt.text(a,b+50,b,ha='center',va='bottom',fontsize=10)
plt.tight_layout()
plt.savefig('line chart/png/428.png')
plt.clf()