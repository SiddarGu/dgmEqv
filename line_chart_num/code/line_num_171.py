
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 8))

plt.plot(['2011', '2012', '2013', '2014', '2015'], [100, 200, 400, 600, 800], label='Facebook')
plt.plot(['2011', '2012', '2013', '2014', '2015'], [50, 100, 200, 400, 600], label='Twitter')
plt.plot(['2011', '2012', '2013', '2014', '2015'], [10, 20, 40, 80, 160], label='Instagram')
plt.plot(['2011', '2012', '2013', '2014', '2015'], [5, 10, 20, 30, 50], label='LinkedIn')

plt.title("Social media user growth from 2011 to 2015")
plt.xlabel('Year')
plt.ylabel('Users (millions)')
plt.legend(loc='upper right')
plt.xticks(['2011', '2012', '2013', '2014', '2015'], rotation=45)

for x, y in zip(['2011', '2012', '2013', '2014', '2015'], [100, 200, 400, 600, 800]):
    plt.annotate(str(y), xy=(x, y))

for x, y in zip(['2011', '2012', '2013', '2014', '2015'], [50, 100, 200, 400, 600]):
    plt.annotate(str(y), xy=(x, y))

for x, y in zip(['2011', '2012', '2013', '2014', '2015'], [10, 20, 40, 80, 160]):
    plt.annotate(str(y), xy=(x, y))

for x, y in zip(['2011', '2012', '2013', '2014', '2015'], [5, 10, 20, 30, 50]):
    plt.annotate(str(y), xy=(x, y))

plt.tight_layout()
plt.savefig('line chart/png/513.png')
plt.clf()