
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(12,8))

data = {'Location':['New York','Los Angeles','Chicago','Miami','Dallas','Seattle','Denver'],
        'Attendees':[500000,400000,350000,300000,200000,150000,100000]}

df = pd.DataFrame(data)

plt.title('Attendance of Major Sporting Events in the US in 2021')

plt.plot(df['Location'], df['Attendees'], color='red', marker='o', linewidth=3, markersize=10)

plt.xlabel('Location')
plt.ylabel('Attendees')

plt.xticks(rotation=45)

for a,b in zip(df['Location'], df['Attendees']):
    plt.annotate('{}'.format(b),xy=(a,b),xytext=(-3,3),textcoords='offset points',ha='right',va='bottom')

plt.grid(True)
plt.tight_layout()
plt.savefig('line chart/png/603.png')
plt.clf()