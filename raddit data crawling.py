import praw
import json

client_id = "TSGkM_O5mx_1QLWlGE7qIQ"
client_secret = "U9N28v5ctqjefF-dwyxRnep5zeP2QQ"
user_agent = "genshin_scraper"

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

# 设置subreddit和关键字
subreddit_name = "Genshin_Impact"
keyword = "zelda"

# 获取subreddit中的热门帖子
subreddit = reddit.subreddit(subreddit_name)
top_posts = subreddit.top(limit=50, time_filter="week")  # time_filter可设置为'all', 'year', 'month', 'week', 'day', 'hour'
# hot_posts = subreddit.hot(limit=10)  # 更改limit以获取更多或更少的帖子

# 遍历帖子并筛选出包含关键字的帖子
comment_context = []
for post in top_posts:
    if keyword.lower() in post.title.lower() or keyword.lower() in post.selftext.lower():
        print(f"标题：{post.title}\n链接：{post.url}\n内容：{post.selftext}\n")

        post.comments.replace_more(limit=0)
        for comment in post.comments.list():
            comment_context.append(comment.body)

with open('user_posts_raddit_zelda.json', 'w', encoding='utf-8') as f:
    json.dump(comment_context, f, ensure_ascii=False, indent=4)