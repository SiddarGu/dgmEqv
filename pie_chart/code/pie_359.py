
import matplotlib.pyplot as plt
plt.figure(figsize=(10,8))
plt.subplot(111)
labels = ['Individual Donations','Government Grants','Corporate Grants','Fundraising Events','Other']
values = [50,15,20,10,5]
explode = (0.1, 0, 0, 0, 0)
plt.title("Sources of Donations for Non-Profits in the USA, 2023")
plt.pie(values, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')
plt.tight_layout()
plt.savefig('pie chart/png/366.png')
plt.clf()