# -*- coding: utf-8 -*-
import unittest
import io
from main import new_tovar


class telegrambot_test(unittest.IsolatedAsyncioTestCase):
    def test_new_tovar(self):
        test_file = 'test_output.txt'
        new_tovar(test_file)
        f = io.open(test_file, mode="r", encoding="utf-8")
        assert f.read() == """ {
    "10630": {
        "article_title": "Лента атласная «Варежки» зелёная 25 мм, 9 м",
        "article_price": "159 руб.",
        "article_price_old": "199 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10630/"
    },
    "10445": {
        "article_title": "Набор декоративных прищепок «С Новым годом», 10 шт.",
        "article_price": "95 руб.",
        "article_price_old": "155 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10445/"
    },
    "10501": {
        "article_title": "Пакет ламинированный «Красный подарок» 31x42x12 см",
        "article_price": "65 руб.",
        "article_price_old": "95 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10501/"
    },
    "10294": {
        "article_title": "Пакет ламинированный «Шарики» 23х27х11,5 см",
        "article_price": "50 руб.",
        "article_price_old": "80 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10294/"
    },
    "10502": {
        "article_title": "Пакет ламинированный «Новогодний дворик» 32x42x12 см",
        "article_price": "68 руб.",
        "article_price_old": "108 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10502/"
    },
    "10295": {
        "article_title": "Пакет ламинированный «Чудес в Новом году» 12х15х5,5 см",
        "article_price": "20 руб.",
        "article_price_old": "60 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10295/"
    },
    "10304": {
        "article_title": "Пакет ламинированный «С Новым годом!» 30х30х12 см",
        "article_price": "60 руб.",
        "article_price_old": "110 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10304/"
    },
    "10296": {
        "article_title": "Пакет ламинированный «Счастливого Нового года» 23х27х8 см",
        "article_price": "45 руб.",
        "article_price_old": "75 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10296/"
    },
    "8653": {
        "article_title": "Набор бирок «Зимние мотивы» 5х9см",
        "article_price": "29 руб.",
        "article_price_old": "69 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/8653/"
    },
    "10335": {
        "article_title": "Набор декоративных прищепок «Новогодние мишки», 10 шт.",
        "article_price": "85 руб.",
        "article_price_old": "155 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10335/"
    },
    "4330": {
        "article_title": "Сахарная посыпка «Морозное утро 2.0», MIXIE, 50 г",
        "article_price": "115 руб.",
        "article_price_old": "175 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/4330/"
    },
    "4334": {
        "article_title": "Сахарная посыпка «Гирлянда на ёлке», MIXIE, 50 г",
        "article_price": "130 руб.",
        "article_price_old": "195 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/4334/"
    },
    "10306": {
        "article_title": "Пакет ламинированный «Счастья» 18х23х10 см",
        "article_price": "40 руб.",
        "article_price_old": "80 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10306/"
    },
    "8021": {
        "article_title": "Грецкий орех очищенный, 50 г",
        "article_price": "65 руб.",
        "article_price_old": "85 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/8021/"
    },
    "10625": {
        "article_title": "Наклейки для декора «Новогодние» в рулоне, 2,5 см, 600 шт",
        "article_price": "190 руб.",
        "article_price_old": "290 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10625/"
    },
    "4918": {
        "article_title": "Сахарная посыпка «Холодные сердца», MIXIE, 50 г",
        "article_price": "195 руб.",
        "article_price_old": "none",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/4918/"
    },
    "10512": {
        "article_title": "Пряник на палочке «Сова» 9 см",
        "article_price": "100 руб.",
        "article_price_old": "170 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10512/"
    },
    "10349": {
        "article_title": "Открытка «Новогодние котики» с голографией 7,5х10 см",
        "article_price": "10 руб.",
        "article_price_old": "35 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10349/"
    },
    "6218": {
        "article_title": "Сахарная посыпка «Хлопушка с конфетти», MIXIE, 50 г",
        "article_price": "105 руб.",
        "article_price_old": "175 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/6218/"
    },
    "10350": {
        "article_title": "Открытка «Лама» с голографией 7,5х10 см",
        "article_price": "15 руб.",
        "article_price_old": "35 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10350/"
    },
    "10629": {
        "article_title": "Лента атласная «Символы Рождества» 25 мм, 9 м",
        "article_price": "159 руб.",
        "article_price_old": "199 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10629/"
    },
    "6435": {
        "article_title": "Сахарная посыпка «Новогоднее настроение», MIXIE, 50 г",
        "article_price": "125 руб.",
        "article_price_old": "175 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/6435/"
    },
    "10444": {
        "article_title": "Пакет ламинированный «Волшебная ночь» 26х30х9 см",
        "article_price": "69 руб.",
        "article_price_old": "109 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10444/"
    },
    "10355": {
        "article_title": "Пакет с клапаном «Волшебных мгновений» синий 18х23х10 см",
        "article_price": "59 руб.",
        "article_price_old": "109 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10355/"
    },
    "5295": {
        "article_title": "Диоксид титана, 500 г",
        "article_price": "360 руб.",
        "article_price_old": "450 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/5295/"
    },
    "8481": {
        "article_title": "Пряник на палочке «Дед мороз» 9 см",
        "article_price": "90 руб.",
        "article_price_old": "170 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/8481/"
    },
    "8593": {
        "article_title": "Трубочки бумажные «Праздник к нам приходит», 10 шт.",
        "article_price": "85 руб.",
        "article_price_old": "135 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/8593/"
    },
    "8676": {
        "article_title": "Форма для шоколада с переводным рисунком «Мишки» 6 ячеек, Pavoni, Италия",
        "article_price": "120 руб.",
        "article_price_old": "220 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/8676/"
    },
    "6851": {
        "article_title": "Леденец \"Трость Новогодняя Большая\" 17 см, 30 г",
        "article_price": "90 руб.",
        "article_price_old": "none",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/6851/"
    },
    "10381": {
        "article_title": "Лента атласная «Снежинки» серебряная 15 мм, 23 м",
        "article_price": "99 руб.",
        "article_price_old": "199 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10381/"
    },
    "9458": {
        "article_title": "Сахарная посыпка «Бленд #7519», УКРАШАЛКИ, 50 г",
        "article_price": "125 руб.",
        "article_price_old": "195 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/9458/"
    },
    "10257": {
        "article_title": "Сахарная посыпка «Бленд #7704», УКРАШАЛКИ, 50 г",
        "article_price": "145 руб.",
        "article_price_old": "195 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10257/"
    },
    "10258": {
        "article_title": "Сахарная посыпка «Бленд #7708», УКРАШАЛКИ, 50 г",
        "article_price": "135 руб.",
        "article_price_old": "195 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10258/"
    },
    "10495": {
        "article_title": "Вырубка с трафаретом «Дед Мороз №2» 11,5 см, Lubimova\n                        \nС трафаретом",
        "article_price": "134 руб.",
        "article_price_old": "184 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10495/"
    },
    "9474": {
        "article_title": "Вырубка с трафаретом «Thank you» 10,3 см, Lubimova",
        "article_price": "144 руб.",
        "article_price_old": "184 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/9474/"
    },
    "9558": {
        "article_title": "Форма для мороженого Mini, Zoku, США, 9 шт.",
        "article_price": "1 480 руб.",
        "article_price_old": "1 880 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/9558/"
    },
    "10494": {
        "article_title": "Вырубка с трафаретом «Тигрёнок с подарком» 11,5 см, Lubimova\n                        \nС трафаретом",
        "article_price": "134 руб.",
        "article_price_old": "184 руб.",
        "article_url": "https://dvemorkovki.ru/catalog/utsenennye_tovary_i_aktsii/10494/"
    }
} """
