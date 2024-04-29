
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
plt.plot([2019,2020,2021,2022,2023],[200,180,190,220,240],'r-o',label='Smartphones')
plt.plot([2019,2020,2021,2022,2023],[150,130,140,180,210],'b-o',label='Tablets')
plt.plot([2019,2020,2021,2022,2023],[100,120,110,150,180],'g-o',label='Laptops')
plt.legend(loc='upper left', bbox_to_anchor=(0.03,1.02), ncol=2, shadow=True, title='Technology Devices', fancybox=True)
plt.title('Rise in sales of Technology devices from 2019-2023')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.xticks([2019,2020,2021,2022,2023],['2019','2020','2021','2022','2023'])
plt.tight_layout()
plt.savefig('line chart/png/72.png')
plt.clf()