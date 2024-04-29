
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
plt.figure(figsize=(10,6)) 
ax = plt.subplot()
ax.bar(['USA','UK','Germany','France'],[1000,800,900,1100], width=0.3, label='Hotels', color='#60A3BC', bottom=[500,600,700,600])
ax.bar(['USA','UK','Germany','France'],[500,600,700,600], width=0.3, label='Restaurants', color='#F7BB41', bottom=[200,180,190,170])
ax.bar(['USA','UK','Germany','France'],[200,180,190,170], width=0.3, label='Tourists(hundred)', color='#F3715C')
ax.set_title('Number of hotels, restaurants, and tourists in four countries in 2021')
ax.set_xlabel('Country')
ax.set_ylabel('Number')
ax.legend(loc='upper left', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('bar_279.png')
plt.clf()