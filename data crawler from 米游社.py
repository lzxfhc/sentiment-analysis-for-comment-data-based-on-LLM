from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import json

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

def get_user_posts(url):
    options = Options()
    options.headless = True
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    scroll_to_load(driver, 3)
    html = driver.page_source
    driver.quit()

    return html


def parse_user_posts(html):
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find_all(class_='reply-card__content')
    inner_posts = soup.find_all(class_='reply-card-inner-reply__content')
    user_posts = []

    for post in posts:
        user_posts.append(post.get_text(strip=True))

    for inner_post in inner_posts:
        user_posts.append(inner_post.get_text(strip=True))

    return user_posts

# ////////////////////////type url of the webpage for data scraping/////////////////////

def main():
    url = 'https://www.miyoushe.com/ys/article/37459160'
    html = get_user_posts(url)
    user_posts = parse_user_posts(html)

    with open('user_posts.json', 'w', encoding='utf-8') as f:
        json.dump(user_posts, f, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    main()
