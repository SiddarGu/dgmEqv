
import matplotlib.pyplot as plt
import pandas as pd

plt.figure(figsize=(10, 6))

# Read data
data = {'Year': [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
        'Number of Facebook users (millions)': [2, 4, 6, 10, 18, 30, 50, 100, 200, 400, 800, 1200, 1600, 2000, 2500, 3000, 3500, 4000, 4500, 5000],
        'Number of Twitter users (millions)': [1, 2, 4, 8, 14, 24, 40, 80, 160, 320, 640, 960, 1280, 1600, 2000, 2500, 3000, 3500, 4000, 4500],
        'Number of Instagram users (millions)': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 100, 300, 500, 1000, 2000]}

# Create Dataframe
df = pd.DataFrame(data)

# Plot the graph
plt.plot(df['Year'], df['Number of Facebook users (millions)'], 'r', label='Facebook')
plt.plot(df['Year'], df['Number of Twitter users (millions)'], 'g', label='Twitter')
plt.plot(df['Year'], df['Number of Instagram users (millions)'], 'b', label='Instagram')

plt.xticks(df['Year'], rotation=90)
plt.xlabel('Year')
plt.ylabel('Number of Users (Millions)')
plt.title('Growth of Major Social Media Platforms from 2001 to 2020')
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('line chart/png/288.png')
plt.clf()