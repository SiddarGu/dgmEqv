
import matplotlib.pyplot as plt
import pandas as pd

#create figure
fig=plt.figure(figsize=(12,8))

#plot pie chart
plt.pie(x=[45,45,10],labels=["Male","Female","Non-Binary"],autopct="%.2f%%",textprops={'fontsize': 12},
    colors=['#0080FF', '#FF3399','#FF8000'],startangle=90)

#title
plt.title("Gender Distribution in the US, 2023")

#Save
plt.savefig("pie chart/png/295.png")

#Clear
plt.clf()