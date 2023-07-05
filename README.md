# sentiment-analysis-for-comment-data-based-on-LLM

This porject begin from 2023.03 and end at 2023.4, these data is not the latest data.

Scraped forum comment data, and use LLM to analysis it, and creat a structured data base to support business

Crawling user comments from platforms such as miHoYo, hoyolab, Reddit, etc., we utilized LLM for a series of analyses to meet the data requirements of the product and development team.

sentiment analysis.ipynb is the analysis program along with the demo results.

.py files consist of crawlers for various platforms, categorized into two types: post-based crawlers and crawlers for retrieving all posts on miHoYo Forum. When crawling all posts, please ensure to set the crawl sleep time to prevent IP-related restrictions.

.json files contain the demo of user comments that were crawled.

项目开始于2023.3结束语2023.4，这些分析的数据不是最新的数据

爬取米游社，hoyolab，reddit等平台的用户评论，利用了LLM，对其进行的一系列分析，支持产研团队的数据需求

sentiment analysis.ipynb是分析程序以及demo结果

.py文件分别是爬取各个平台的爬虫，分为按帖子爬取以及爬取米游社全部帖子的两种爬虫，爬取全部帖子注意设置爬取睡眠时间，防止ip被风控

.json文件是爬取到的用户评论demo
