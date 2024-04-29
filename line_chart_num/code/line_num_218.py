
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

monthly_data = {'January': [1000, 1100, 1200], 'February': [1300, 1200, 1300], 'March': [1500, 1400, 1100], 'April': [1200, 1400, 1400], 'May': [1300, 1100, 1200], 'June': [1000, 1300, 1300], 'July': [1400, 1200, 1000], 'August': [1100, 1300, 1200]}

month_list = list(monthly_data.keys())
production_a_list = [monthly_data[x][0] for x in month_list]
production_b_list = [monthly_data[x][1] for x in month_list]
production_c_list = [monthly_data[x][2] for x in month_list]

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

ax.plot(month_list, production_a_list, label='Production A(Units)', color='red')
ax.plot(month_list, production_b_list, label='Production B(Units)', color='blue')
ax.plot(month_list, production_c_list, label='Production C(Units)', color='green')

ax.set_title('Production of three types of products in a manufacturing company in 2021')
ax.xaxis.set_major_locator(ticker.MultipleLocator())
ax.legend(loc='upper left')
for i,j in zip(month_list, production_a_list):
    ax.annotate(str(j),xy=(i,j))
for i,j in zip(month_list, production_b_list):
    ax.annotate(str(j),xy=(i,j))
for i,j in zip(month_list, production_c_list):
    ax.annotate(str(j),xy=(i,j))
plt.tight_layout()
plt.savefig('line chart/png/439.png')
plt.close()