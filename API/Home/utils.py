from Core.models.gold import *


def get_gold_stock_price():

    """

        return gold price for buying and saleing

    """

    try:

        gold_price_obj = GoldPrice.objects.all().order_by('Date')
        gold_price_obj = gold_price_obj[len(gold_price_obj)-1]

    except:

        return {

            "responseFA": 'قیمت ها توسط ادمین ثبت نشده اند',
            "responseEN": 'admin didn\'t add gold price ',

        }, 404

    return {

        'sale_price': gold_price_obj.sale_price,
        'buy_price': gold_price_obj.sale_price + gold_price_obj.price_difference,

    }, 200
