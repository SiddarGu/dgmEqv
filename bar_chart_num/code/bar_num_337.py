
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(15, 8))
gs = gridspec.GridSpec(1,1)
ax = fig.add_subplot(gs[0, 0])

Country = ['USA', 'UK', 'Germany', 'France']
Average_Grade_Point = [3.2, 3.5, 3.7, 3.4]
Dropout_Rate = [2, 1.5, 1.2, 1.7]

ax.bar(Country, Average_Grade_Point, label="Average Grade Point", color='green', bottom=Dropout_Rate)
ax.bar(Country, Dropout_Rate, label="Dropout Rate", color='red')

for i in range(len(Country)):
    ax.annotate(Average_Grade_Point[i], xy=(Country[i], Average_Grade_Point[i]/2+Dropout_Rate[i]), rotation=90, size=12, ha='center', va='bottom')
    ax.annotate(Dropout_Rate[i], xy=(Country[i], Dropout_Rate[i]/2), rotation=90, size=12, ha='center', va='top')

ax.set_xticks(Country)
ax.set_title("Average Grade Point and Dropout Rate in four countries in 2021")
ax.legend(loc="best")
plt.tight_layout()
plt.savefig('Bar Chart/png/374.png')
plt.clf()