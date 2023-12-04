from Core.models.gold import *


def get_gold_stock_price():

    """

        return gold price for buying and saleing

    """

    try:

        gold_price_obj = GoldPrice.objects.filter(active=True).order_by('Date')[0]

    except:

        return {

            "response-fa": 'قیمت ها توسط ادمین ثبت نشده اند',
            "response-en": 'admin didn\'t add gold price ',

        }, 404

    return {

        'sale-price': gold_price_obj.sale_price,
        'buy-price': gold_price_obj.sale_price + gold_price_obj.price_difference,

    }, 200
