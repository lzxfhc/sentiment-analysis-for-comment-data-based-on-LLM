# sentiment-analysis-for-comment-data-based-on-LLM
Scraped forum comment data, and use LLM to analysis it, and creat a structured data base to support business

爬取米游社，hoyolab，reddit等平台的用户评论，利用了LLM，对其进行的一系列分析，支持产研团队的数据需求

sentiment analysis.ipynb是分析程序以及demo结果

.py文件分别是爬取各个平台的爬虫，分为按帖子爬取以及爬取米游社全部帖子的两种爬虫，爬取全部帖子注意设置爬取睡眠时间，防止ip被风控

.json文件是爬取到的用户评论demo
