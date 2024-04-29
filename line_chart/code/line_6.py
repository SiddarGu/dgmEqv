
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 8))
plt.plot(['John Smith', 'Mary Johnson', 'Jack Wilson', 'Sarah Taylor', 'Mark Brown'],
         [5000, 2000, 1000, 3000, 500], linestyle='--', marker='o', color='b')
plt.xticks(rotation=30, wrap=True)
plt.title('Donations to Charity Organization in 2020')
plt.xlabel('Donor')
plt.ylabel('Donation Amount (in USD)')
plt.legend(['Number of Donations'])
plt.tight_layout()
plt.savefig('line chart/png/553.png')
plt.clf()