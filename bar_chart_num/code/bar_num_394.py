
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111)
ax.bar(x=['January', 'February', 'March', 'April'], 
       height=[400, 450, 500, 550], width=0.35, align="center",
       label="Manufacturing Output(million)", color='b', bottom=0)
ax.bar(x=['January', 'February', 'March', 'April'], 
       height=[1000, 1100, 1200, 1300], width=0.35, align="center",
       label="Production Output(million)", color='r', bottom=400)
ax.set_title('Manufacturing and Production Output from January to April 2021')
ax.set_ylabel('Output(million)')
ax.set_xlabel('Month')
ax.legend(loc='upper right')
ax.annotate('450', xy=('February', 975))
ax.annotate('500', xy=('March', 1175))
ax.annotate('550', xy=('April', 1375))
ax.annotate('400', xy=('January', 375))
ax.annotate('1000', xy=('January', 750))
ax.annotate('1100', xy=('February', 1150))
ax.annotate('1200', xy=('March', 1525))
ax.annotate('1300', xy=('April', 1900))
plt.xticks(['January', 'February', 'March', 'April'], rotation=45)
plt.tight_layout()
plt.savefig('Bar Chart/png/294.png')
plt.clf()