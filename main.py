# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import json


def get_new(): # заимствовано из youtube (https://www.youtube.com/watch?v=9onddoBnkRc)
    ''' Эта функция выдает последние товары с сайта со скидками. '''

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"
    }

    url = "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/"
    response = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")
    articles_card = soup.find_all("div",class_="product-card product-card_block")


    tovar_dict = {}

    for article in articles_card:
        article_title = article.find("a", class_="product-card__title").text.strip()
        article_price = article.find("span", class_="product-card__price").text.strip()
        article_price_old = article.find("span", class_="product-card__price_old")
        if article_price_old is not None:
            article_price_old = article_price_old.text.strip()
        else:
            article_price_old = 'none'
        article_url = 'https://dvemorkovki.ru' + article.find_all('a', href=True)[0]['href']
        article_id = article_url.split('/')[-2]

        # print(f"{article_title} | {article_price} | {article_price_old} | {article_url} ")

        tovar_dict[article_id] = {
            'article_title': article_title,
            'article_price': article_price,
            'article_price_old': article_price_old,
            'article_url': article_url
        }

    with open("tovar_dict.json", "w") as file:
        json.dump(tovar_dict, file, indent=4, ensure_ascii=False , sort_keys=False)


def new_tovar(json_path="tovar_dict.json"):
    ''' Эта функция проверяет сайт на обновления - новые товары. '''

    with open("tovar_dict.json", encoding='utf-8') as file:
        new_list = json.load(file)

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36"
    }

    url = "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/"
    response = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")
    articles_card = soup.find_all("div", class_="product-card product-card_block")

    fresh_tovar = {}
    tovar_dict = {}

    for article in articles_card:
        article_url = 'https://dvemorkovki.ru' + article.find_all('a', href=True)[0]['href']
        article_id = article_url.split('/')[-2]

        if article_id in new_list:
            continue
        else:
            article_title = article.find("a", class_="product-card__title").text.strip()
            article_price = article.find("span", class_="product-card__price").text.strip()
            article_price_old = article.find("span", class_="product-card__price_old")
            if article_price_old is not None:
                article_price_old = article_price_old.text.strip()
            else:
                article_price_old = 'none'

            tovar_dict[article_id] = {
                'article_title': article_title,
                'article_price': article_price,
                'article_price_old': article_price_old,
                'article_url': article_url
            }

            fresh_tovar[article_id] = {
                'article_title': article_title,
                'article_price': article_price,
                'article_price_old': article_price_old,
                'article_url': article_url
            }

    with open(json_path, "w", encoding='utf-8') as file:
        json.dump(tovar_dict, file, indent=4, ensure_ascii=False)

    return fresh_tovar


def main():
    ''' Вызываем функцию по сбору товаров. '''

    #get_new()
    print(new_tovar())

if __name__ == '__main__':
    main()