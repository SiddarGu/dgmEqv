

import matplotlib.pyplot as plt
year=[2012,2013,2014,2015]
donation_a=[200,250,300,350]
donation_b=[100,150,200,250]
donation_c=[300,350,400,500]
donation_d=[400,500,450,600]

plt.figure(figsize=(8,6))
plt.plot(year,donation_a,label="Donation A(million dollars)",linewidth=2,marker='o',markersize=5,color='black')
plt.plot(year,donation_b,label="Donation B(million dollars)",linewidth=2,marker='o',markersize=5,color='r')
plt.plot(year,donation_c,label="Donation C(million dollars)",linewidth=2,marker='o',markersize=5,color='b')
plt.plot(year,donation_d,label="Donation D(million dollars)",linewidth=2,marker='o',markersize=5,color='g')
plt.title('Donations to four nonprofit organizations from 2012 to 2015',fontsize=20)
plt.xlabel('Year',fontsize=15)
plt.ylabel('Donation (million dollars)',fontsize=15)
plt.xticks(year)
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.,fontsize=15)
plt.tight_layout()
plt.savefig('line chart/png/475.png',dpi=475)
plt.clf()