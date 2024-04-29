import pandas as pd
import matplotlib.pyplot as plt

# Given data
data_str = """Daily Active Users (Millions),Social Media Platform
Facebook,1260
YouTube,1220
WhatsApp,1000
Instagram,800
WeChat,1050
TikTok,680
Telegram,550
Snapchat,500
Twitter,330
Pinterest,250"""

# Process the data into DataFrame
data_lines = data_str.split('\n')
data_labels = data_lines[0].split(',')[1:]
line_labels = [line.split(',')[0] for line in data_lines[1:]]
data_values = [int(line.split(',')[1]) for line in data_lines[1:]]
data_df = pd.DataFrame(data={'Social Media Platform': line_labels, 'Daily Active Users (Millions)': data_values})

# Visualize the histogram
plt.figure(figsize=(12, 8))
ax = plt.subplot(111)
data_df.plot(kind='bar', x='Social Media Platform', y='Daily Active Users (Millions)',
             ax=ax, color='skyblue', grid=True, legend=False)

# Set the title and labels
ax.set_title('Daily Active User Counts for Major Social Media Platforms')
ax.set_xlabel('Social Media Platform')
ax.set_ylabel('Daily Active Users (Millions)')

# Rotate x-axis labels if necessary
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)

# Apply tight layout
plt.tight_layout()

# Save the figure
save_path = '/cpfs01/user/liuqi/workspace/plotchart/demo/histogram/png/629.png'
plt.savefig(save_path)

# Clear the current figure state to prevent overlap with any future plots
plt.clf()
