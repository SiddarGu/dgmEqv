
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 7))  
plt.title("Revenue and Expenses of ABC Corporation from 2018-2022")
plt.xlabel("Year") 
plt.ylabel("Amount")

year = [2018, 2019, 2020, 2021, 2022] 
revenue = [10000, 12000, 14000, 15000, 17000] 
expenses = [8000, 9000, 10000, 11000, 13000] 

plt.plot(year, revenue, color ='g', label ='Revenue') 
plt.plot(year, expenses, color ='r', label ='Expenses')  
plt.xticks(year)
plt.legend() 

plt.tight_layout()
plt.savefig('line chart/png/96.png')
plt.clf()