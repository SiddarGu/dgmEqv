
import matplotlib.pyplot as plt
plt.figure(figsize=(10,7))
ax = plt.subplot()
ax.plot(['January', 'February', 'March', 'April', 'May','June','July','August','September','October','November','December'], 
        [100,110,130,150,125,110,115,130,140,155,145,140], label='Online Sales(million dollars)')
ax.plot(['January', 'February', 'March', 'April', 'May','June','July','August','September','October','November','December'], 
        [80,90,85,95,85,80,90,100,105,115,120,130], label='Retail Sales(million dollars)')
ax.legend(loc='upper left')
ax.set_title('Comparison of Online and Retail Sales in 2020')
ax.set_xlabel('Month')
ax.set_ylabel('Sales(million dollars)')
ax.grid(alpha=0.3)
ax.set_xticks(['January', 'February', 'March', 'April', 'May','June','July','August','September','October','November','December'])
ax.annotate('Online Sales:100', xy=('January', 100), xytext=('February', 105),
            arrowprops=dict(arrowstyle='->'))
ax.annotate('Retail Sales:80', xy=('January', 80), xytext=('February', 85),
            arrowprops=dict(arrowstyle='->'))
ax.annotate('Online Sales:155', xy=('October', 155), xytext=('November', 150),
            arrowprops=dict(arrowstyle='->'))
ax.annotate('Retail Sales:130', xy=('December', 130), xytext=('November', 135),
            arrowprops=dict(arrowstyle='->'))
plt.tight_layout()
plt.savefig('line chart/png/206.png',dpi=200)
plt.clf()