
import matplotlib.pyplot as plt

plt.figure(figsize=(15, 8))
ax = plt.subplot()
plt.bar(['USA', 'UK', 'Germany', 'France'], [4000, 3000, 3500, 3600], width=.4, label='Restaurants', color='#6699cc')
plt.bar(['USA', 'UK', 'Germany', 'France'], [8000, 7000, 6000, 7200], width=.4, bottom=[4000, 3000, 3500, 3600], label='Fast Food Chains', color='#ffcc66')
plt.bar(['USA', 'UK', 'Germany', 'France'], [7000, 5000, 4500, 5000], width=.4, bottom=[12000, 10000, 9500, 10800], label='Bar', color='#ff9900')

ax.annotate('{}'.format(4000), xy=('USA', 4000+500))
ax.annotate('{}'.format(3000), xy=('UK', 3000+500))
ax.annotate('{}'.format(3500), xy=('Germany', 3500+500))
ax.annotate('{}'.format(3600), xy=('France', 3600+500))
ax.annotate('{}'.format(8000), xy=('USA', 8000+500))
ax.annotate('{}'.format(7000), xy=('UK', 7000+500))
ax.annotate('{}'.format(6000), xy=('Germany', 6000+500))
ax.annotate('{}'.format(7200), xy=('France', 7200+500))
ax.annotate('{}'.format(7000), xy=('USA', 12000+500))
ax.annotate('{}'.format(5000), xy=('UK', 10000+500))
ax.annotate('{}'.format(4500), xy=('Germany', 9500+500))
ax.annotate('{}'.format(5000), xy=('France', 10800+500))

plt.xticks(rotation=45)
plt.title('Number of food and beverage outlets in four countries in 2021')
plt.legend(loc='upper center')
plt.tight_layout()
plt.savefig('Bar Chart/png/216.png')
plt.clf()