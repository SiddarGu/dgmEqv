
import matplotlib.pyplot as plt

data = [['January', 2.3, 31.2], 
        ['February', 2.6, 35.5], 
        ['March', 3.2, 41.2],
        ['April', 3.1, 42.8],
        ['May', 3.7, 48.7],
        ['June', 3.4, 47.4],
        ['July', 3.2, 46.5],
        ['August', 2.8, 40.2],
        ['September', 2.3, 36.1],
        ['October', 2.6, 37.9],
        ['November', 2.2, 34.2],
        ['December', 2.4, 36.8]]

month, tourist_arrivals, tourism_revenue = zip(*data)

plt.figure(figsize=(10,6))

plt.plot(month, tourist_arrivals, color='b', label='Tourist Arrivals (million)')
plt.plot(month, tourism_revenue, color='r', label='Tourism Revenue (billion dollars)')

plt.xlabel('Month')
plt.xticks(month)

plt.title('Tourist arrivals and tourism revenue in the US in 2022')
plt.legend(loc='best')

for a, b in zip(month, tourist_arrivals): 
    plt.annotate(str(b),xy=(a,b))

for a, b in zip(month, tourism_revenue): 
    plt.annotate(str(b),xy=(a,b))

plt.tight_layout()
plt.savefig('line chart/png/143.png')
plt.clf()