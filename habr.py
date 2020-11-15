import requests
from bs4 import BeautifulSoup


KEYWORDS = ['дизайн', 'фото', 'web', 'python']


# def get_posts():
#     response = requests.get('https://habr.com/ru/all/')
#     soup = BeautifulSoup(response.text, 'html.parser')
#     posts = soup.find_all('article', class_='post')
#     for post in posts:
#         preview = post.find('div', class_='post__text-html')
#         for keyword in KEYWORDS:
#             if keyword in preview.text.lower():
#                 date = post.find('span', class_='post__time').text
#                 title_element = post.find('a', class_='post__title_link')
#                 title = title_element.text
#                 link = title_element.attrs.get('href')
#                 print(f'{date} - {title} - {link}')
#                 break


def get_posts():
    response = requests.get('https://habr.com/ru/all/')
    soup = BeautifulSoup(response.text, 'html.parser')
    posts = soup.find_all('article', class_='post')
    for post in posts:
        link = post.find('a', class_='post__title_link').attrs.get('href')
        post_page = requests.get(link)
        soup = BeautifulSoup(post_page.text, 'html.parser')
        post_text = soup.find('div', id='post-content-body')
        for keyword in KEYWORDS:
            if keyword in post_text.text.lower():
                date = soup.find('span', class_='post__time').text
                title = soup.find('span', class_='post__title-text').text
                print(f'{date} - {title} - {link}')
                break


if __name__ == '__main__':
    get_posts()