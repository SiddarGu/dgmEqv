
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,8))

Donations = ['Cash Donations','In-Kind Donations','Services','Volunteers','Fundraising Events']
Percentage = [30,20,15,25,10]

plt.pie(Percentage, labels=Donations, 
        autopct='%1.1f%%', startangle=90, 
        wedgeprops = {'linewidth': 1.5, 'edgecolor':'black'}) 
plt.title('Distribution of Donations to Nonprofit Organizations in the USA, 2023') 
plt.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/341.png')
plt.clf()