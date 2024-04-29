
import matplotlib.pyplot as plt
plt.figure(figsize=(15,9))
ax = plt.subplot()
month=['January','February','March','April','May','June','July','August','September']
co2_emission=[390,392,393,394,396,397,398,399,400]
pollution_index=[50,52,55,58,60,62,65,68,70]
ax.plot(month,co2_emission,color='green',label='CO2 Emission')
ax.plot(month,pollution_index,color='red',label='Pollution Index')
ax.set_title('CO2 Emission and Pollution Index in Los Angeles from January to September 2021')
ax.set_xticks(month)
ax.set_xticklabels(month,rotation=45,wrap=True)
ax.legend(loc='best', fontsize=12)
for a,b,c in zip(month,co2_emission,pollution_index):
    ax.annotate(f'CO2:{b}, PI:{c}', xy=(a,b), xytext=(-20,10),rotation=45, textcoords='offset points',arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
plt.tight_layout()
plt.savefig('line chart/png/578.png')
plt.clf()