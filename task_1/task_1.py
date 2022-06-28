"""Задание №1. Написать метод, который вернет домен из url адреса."""


def domain_name(url: str) -> str:
    """Функция вернет домен из url адреса"""
    if "//" in url:
        url = url.split('//')[1]
    url = url.split('.')
    if 'www' in url:
        url = url[1]
    else:
        url = url[0]
    return url


urls = [
    'https://youtube.com',
    'www.xaker.ru',
    'http://google.com',
    'http://google.cojp',
]

for url_adr in urls:
    print('domain name =', domain_name(url_adr))
