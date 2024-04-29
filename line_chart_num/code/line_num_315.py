
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 8))

donors = ['James', 'Smith', 'David', 'Peter']

A = [400, 500, 350, 300]
B = [300, 200, 400, 300]
C = [300, 500, 750, 300]

plt.plot(donors, A, label='Charity A', marker='o')
plt.plot(donors, B, label='Charity B', marker='o')
plt.plot(donors, C, label='Charity C', marker='o')

plt.xlabel('Donor')
plt.ylabel('Donation Amount(USD)')
plt.title('Donations to Three Charities by Three Donors in 2020')
plt.xticks(donors, donors, rotation=45)

for i, j in zip(donors, A):
    plt.annotate(str(j), xy=(i, j+10))

for i, j in zip(donors, B):
    plt.annotate(str(j), xy=(i, j+10))

for i, j in zip(donors, C):
    plt.annotate(str(j), xy=(i, j+10))

plt.legend()
plt.tight_layout()
plt.savefig('line chart/png/115.png')
plt.clf()