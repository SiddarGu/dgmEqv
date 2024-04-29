
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.plot(['2001','2002','2003','2004'],[500,600,700,800],label='Gross Profit(million dollars)')
plt.plot(['2001','2002','2003','2004'],[200,250,300,350],label='Net Profit(million dollars)')
plt.plot(['2001','2002','2003','2004'],[1000,1200,1300,1500],label='Total Revenue(million dollars)')
plt.title('Financial Performance of a Company in 2001-2004')
plt.xlabel('Year')
plt.ylabel('Revenue(million dollars)')
plt.legend()
plt.xticks(['2001','2002','2003','2004'],['2001','2002','2003','2004'])
plt.annotate('Gross Profit(million dollars): 800', xy=('2004', 800), xytext=('2004',1000),arrowprops=dict(arrowstyle='->'))
plt.annotate('Net Profit(million dollars): 350', xy=('2004', 350), xytext=('2004',500),arrowprops=dict(arrowstyle='->'))
plt.annotate('Total Revenue(million dollars): 1500', xy=('2004', 1500), xytext=('2004',1700),arrowprops=dict(arrowstyle='->'))
plt.tight_layout()
plt.savefig('line chart/png/287.png')
plt.clf()