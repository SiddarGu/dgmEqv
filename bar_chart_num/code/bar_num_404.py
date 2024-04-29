
import matplotlib.pyplot as plt 
fig, ax = plt.subplots(figsize=(10,6)) 
x = ['Red Cross', 'UNICEF', 'World Vision', 'Save the Children'] 
donations = [20, 25, 15, 18] 
volunteers = [100, 150, 90, 110] 
width = 0.35
ax.bar(x, donations, width=width, label='Donations(million)') 
ax.bar(x, volunteers, width=width, bottom=donations, label='Volunteers') 
ax.set_title('Funds and volunteers received by charity and nonprofit organizations in 2021')
ax.set_ylabel('Number') 
ax.set_xticklabels(x, rotation=45, ha='right', fontsize=10) 
ax.legend(loc="upper left") 
for i in range(0, len(x)): 
    ax.annotate(donations[i], xy=(x[i], donations[i]/2), xytext=(0, 3), 
        textcoords="offset points", ha='center', va='bottom') 
    ax.annotate(volunteers[i], xy=(x[i], donations[i]+volunteers[i]/2), xytext=(0, 3), 
        textcoords="offset points", ha='center', va='bottom') 
plt.tight_layout() 
plt.savefig('Bar Chart/png/84.png') 
plt.clf()