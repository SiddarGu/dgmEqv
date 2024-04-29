
import matplotlib.pyplot as plt
import numpy as np

Country = ['USA', 'UK', 'Germany', 'France']
Voters = [45000, 50000, 40000, 45000]
Votes = [60000, 70000, 55000, 60000]
Eligible_Voters = [100000, 110000, 90000, 95000]

x = np.arange(len(Country))

plt.figure(figsize=(15,7))

ax = plt.subplot()
ax.bar(x - 0.2, Voters, width=0.2, color='tab:orange', label='Voters')
ax.bar(x, Votes, width=0.2, color='tab:blue', label='Votes')
ax.bar(x + 0.2, Eligible_Voters, width=0.2, color='tab:green', label='Eligible Voters')

ax.set_xticks(x)
ax.set_xticklabels(Country)

ax.set_title('Voter turnout and eligible voters in four countries in 2021')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=3)

for i in range(len(Country)):
    ax.annotate('{}'.format(Voters[i]), xy=(x[i] - 0.2, Voters[i] + 500))
    ax.annotate('{}'.format(Votes[i]), xy=(x[i], Votes[i] + 500))
    ax.annotate('{}'.format(Eligible_Voters[i]), xy=(x[i] + 0.2, Eligible_Voters[i] + 500))

plt.tight_layout()

plt.savefig('Bar Chart/png/566.png')
plt.clf()