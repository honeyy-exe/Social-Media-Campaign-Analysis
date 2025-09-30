import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("campaign_data.csv")
data['Engagement'] = (data['Likes'] + data['Shares'] + data['Comments']) / data['Impressions'] * 100
top_posts = data.sort_values(by='Engagement', ascending=False).head(5)

print("Top 5 Posts by Engagement Rate:")
print(top_posts[['Post', 'Engagement']])

data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace=True)

plt.figure(figsize=(10,6))
plt.plot(data['Date'], data['Engagement'], marker='o', linestyle='-')
plt.title("Engagement Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Engagement Rate (%)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

average_engagement = data['Engagement'].mean()
best_day = data.loc[data['Engagement'].idxmax(), 'Date']
best_post = data.loc[data['Engagement'].idxmax(), 'Post']

print(f"\nAverage Engagement Rate: {average_engagement:.2f}%")
print(f"Best performing post: '{best_post}' on {best_day.date()}")
print("Recommendation: Focus on content type/style of top-performing posts and post more on similar days/times.")
