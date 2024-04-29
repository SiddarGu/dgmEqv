
import matplotlib.pyplot as plt

plt.figure(figsize=(8,6))

year = ['2015', '2016', '2017', '2018']
smartphone_users = [2000, 2100, 2200, 2300]
computer_users = [1000, 1100, 1200, 1300]
internet_users = [4000, 4500, 5000, 5500]

x = [i for i, _ in enumerate(year)]

plt.bar(x, smartphone_users, label='Smartphone Users', width=0.3, bottom=computer_users)
plt.bar(x, computer_users, label='Computer Users', width=0.3, bottom=internet_users)
plt.bar(x, internet_users, label='Internet Users', width=0.3)

plt.xlabel('Year')
plt.ylabel('Users')
plt.title('Number of users of smartphones, computers and Internet from 2015 to 2018')

plt.xticks(x, year)
plt.legend()
plt.tight_layout()

for i, v in enumerate(smartphone_users):
    plt.text(x[i] - 0.1, v + 100, str(v))
    plt.text(x[i] + 0.1, computer_users[i] + 100, str(computer_users[i]))
    plt.text(x[i], internet_users[i] + 100, str(internet_users[i]))

plt.savefig('Bar Chart/png/320.png')

plt.cla()