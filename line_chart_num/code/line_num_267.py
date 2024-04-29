
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))
ax = plt.gca()
ax.plot(['2016','2017','2018','2019','2020'],[120,125,135,140,150], label="Domestic Tourists (millions)", color='purple', marker='o')
ax.plot(['2016','2017','2018','2019','2020'],[150,165,180,190,200], label="International Tourists (millions)", color='orange', marker='o')
ax.set_title("Growth of Tourists in the USA from 2016 to 2020")
for x,y in zip(['2016','2017','2018','2019','2020'],[120,125,135,140,150]):
    plt.annotate(str(y),xy=(x,y), xytext=(0,5), textcoords='offset points')
for x,y in zip(['2016','2017','2018','2019','2020'],[150,165,180,190,200]):
    plt.annotate(str(y),xy=(x,y), xytext=(0,5), textcoords='offset points')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=2)
ax.set_xticks(['2016','2017','2018','2019','2020'])
plt.xticks(rotation=45)
ax.text(0.5, 0.5, 'Growth of Tourists in the USA from 2016 to 2020', ha='center', va='center', transform=ax.transAxes)
plt.tight_layout()
plt.savefig('line chart/png/518.png')
plt.clf()