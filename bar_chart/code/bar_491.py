
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
Donation_Type = ['Online donations', 'Donations by mail','Donations in person','Donations by phone']
Donation_Amount = [500, 400, 300, 450]
ax.bar(Donation_Type, Donation_Amount, color='green')
ax.set_title('Total donations received by charity organizations in 2021')
ax.set_xlabel('Donation Type')
ax.set_ylabel('Donation Amount(USD)')
ax.set_xticklabels(Donation_Type, rotation=30, ha='right', wrap=True)
plt.tight_layout()
plt.savefig('bar chart/png/296.png')
plt.clf()