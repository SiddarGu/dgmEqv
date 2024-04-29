
import matplotlib.pyplot as plt

Age_Group = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']
Voting_Participation = [32, 32, 18, 11, 5, 2]

plt.figure(figsize=(8,8))
ax = plt.subplot()
ax.pie(Voting_Participation, labels=Age_Group,autopct='%1.1f%%', shadow=True, startangle=90)
ax.axis('equal')
plt.title('Voting Participation in the USA by Age Group, 2023')
plt.tight_layout()
plt.savefig('pie chart/png/240.png')
plt.clf()