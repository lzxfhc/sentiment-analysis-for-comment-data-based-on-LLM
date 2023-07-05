import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import json
import time

def scroll_to_load(driver, timeout):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            WebDriverWait(driver, timeout).until(
                lambda driver: driver.execute_script("return document.body.scrollHeight;") > last_height
            )
        except:
            break
        last_height = driver.execute_script("return document.body.scrollHeight")

def get_thread_links(url, max_threads):
    options = Options()
    options.headless = True
    options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    scroll_to_load(driver, 3)
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, 'html.parser')
    threads = soup.select('a.mhy-article-card__link[href]')
    thread_links = ['https://www.miyoushe.com' + thread['href'] for thread in threads[:max_threads]]

    return thread_links

def get_user_posts(url):
    options = Options()
    options.headless = True
    options.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    scroll_to_load(driver, 3)
    html = driver.page_source
    driver.quit()

    return html

def parse_user_posts(html):
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find('title').get_text(strip=True)
    posts = soup.find_all(class_='reply-card__content')
    inner_posts = soup.find_all(class_='reply-card-inner-reply__content')
    user_posts = [title]

    for post in posts:
        user_posts.append(post.get_text(strip=True))

    for inner_post in inner_posts:
        user_posts.append(inner_post.get_text(strip=True))

    return user_posts

# ///////////////////////entry max_threads number to specify how many posts you want to crawl.///////////////

def main():
    board_url = 'https://www.miyoushe.com/ys/'
    max_threads = 999
    thread_links = get_thread_links(board_url, max_threads)

    all_user_posts = []
    for thread_url in thread_links:
        all_user_posts.append('/////////////////////////////////////////////')
        all_user_posts.append(thread_url)
        print(f'Processing thread: {thread_url}')
        html = get_user_posts(thread_url)
        user_posts = parse_user_posts(html)
        all_user_posts.extend(user_posts)
        time.sleep(10)

    with open('user_posts_palte_test.json', 'w', encoding='utf-8') as f:
        json.dump(all_user_posts, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()
