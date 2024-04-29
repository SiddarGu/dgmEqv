
import matplotlib.pyplot as plt

Year = [2001, 2002, 2003, 2004]
Local_Produce_Consumption = [500000, 400000, 450000, 500000]
Imported_Produce_Consumption = [400000, 500000, 450000, 350000]
Local_Meat_Consumption = [300000, 250000, 350000, 400000]
Imported_Meat_Consumption = [200000, 250000, 200000, 250000]

fig = plt.figure(figsize=(15, 7))
plt.plot(Year, Local_Produce_Consumption, label = 'Local Produce Consumption')
plt.plot(Year, Imported_Produce_Consumption, label = 'Imported Produce Consumption')
plt.plot(Year, Local_Meat_Consumption, label = 'Local Meat Consumption')
plt.plot(Year, Imported_Meat_Consumption, label = 'Imported Meat Consumption')
plt.title('Increase in Consumption of Local and Imported Produce and Meat in the Food and Beverage Industry')
plt.xticks(Year)
plt.legend(loc='upper left')

for a,b in zip(Year,Local_Produce_Consumption): 
    plt.annotate(str(b),xy=(a,b),xytext=(a-0.2,b+10000))
for a,b in zip(Year,Imported_Produce_Consumption): 
    plt.annotate(str(b),xy=(a,b),xytext=(a-0.2,b+10000))
for a,b in zip(Year,Local_Meat_Consumption): 
    plt.annotate(str(b),xy=(a,b),xytext=(a-0.2,b+10000))
for a,b in zip(Year,Imported_Meat_Consumption): 
    plt.annotate(str(b),xy=(a,b),xytext=(a-0.2,b+10000))

plt.grid()
plt.tight_layout()
plt.savefig('line chart/png/4.png')
plt.clf()