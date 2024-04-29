
import matplotlib.pyplot as plt 
import numpy as np 

country = ['USA','UK','Germany','France']
facebook_users = [200,100,80,90]
twitter_users = [50,20,15,25]

fig = plt.figure(figsize=(15,5)) 
ax = fig.add_subplot() 
ax.bar(country, facebook_users, label="Facebook Users", bottom=twitter_users, color="orange") 
ax.bar(country, twitter_users, label="Twitter Users", color="blue") 

ax.set_title("Social Media Users in four countries in 2021") 

ax.set_xlabel("Country") 
ax.set_ylabel("Number of Users (million)") 

ax.legend() 

for i, v in enumerate(facebook_users):
    ax.text(i-0.2, v+2, str(v), fontsize=10, color="black")
for i, v in enumerate(twitter_users):
    ax.text(i-0.2, v+2, str(v), fontsize=10, color="black")

plt.xticks(np.arange(len(country)), country) 
plt.tight_layout() 
plt.savefig("Bar Chart/png/605.png") 
plt.clf()