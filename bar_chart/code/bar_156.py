
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(8,6))
ax=fig.add_subplot()
plt.bar(x=['USA', 'UK', 'Germany', 'France'],height=[15.2, 8.1, 4.5, 2.8],width=0.4,label='Total Donations (billion $)',color='#FFC0CB',alpha=0.8)
plt.bar(x=['USA', 'UK', 'Germany', 'France'],height=[60, 50, 45, 40],width=-0.4,label='Number of Donors',color='#F0F8FF',alpha=0.8,bottom=[15.2, 8.1, 4.5, 2.8])
plt.title('Total donations and number of donors in four countries in 2021')
plt.xticks(rotation=60)
plt.legend()
plt.tight_layout()
plt.savefig('bar chart/png/478.png')
plt.clf()