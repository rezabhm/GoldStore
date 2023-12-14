from django.utils import timezone

from Core.models.gold import GoldPrice


def change_gold_price(gold_price):

    gold_obj = GoldPrice.objects.filter(active=True).order_by('Date')

    for dt in gold_obj:

        dt.active = False
        dt.save()

    gold_obj_new = GoldPrice(

        Date=timezone.now(),
        sale_price=gold_price,
        price_difference=gold_obj[len(gold_obj)-1].price_difference,
        total_gold_stock=gold_obj[len(gold_obj) - 1].total_gold_stock,
        stock_status=gold_obj[len(gold_obj) - 1].stock_status,
        active=True
    )

    gold_obj_new.save()

    return {

        'responseEN': 'successfully ...',
        'responseFA': 'با موفقیت قیمت تفییر کرد'

    }, 200


def open_close_stock():

    try:

        gold_obj = GoldPrice.objects.filter(active=True).order_by('Date')
        gold_obj = gold_obj[len(gold_obj)-1]

        gold_obj.stock_status = not gold_obj.stock_status
        gold_obj.save()

        return {}, 200

    except:

        return {

            'responseEN': 'we didn\'t define stock price ',
            'responseFA': 'وضعیت بازار تعریف نشده است یا قیمتی تعریف نشده است '

        }, 400


def change_store_gold_amount(gold_amount):

    try:

        gold_obj = GoldPrice.objects.filter(active=True).order_by('Date')
        gold_obj = gold_obj[len(gold_obj)-1]

        gold_obj.total_gold_stock = float(gold_amount)
        gold_obj.save()

        return {}, 200

    except:

        return {

            'responseEN': 'we didn\'t define setting ',
            'responseFA': 'تنظیمات اعمال نشده است '

        }, 400


def change_price_difference(price_difference):

    try:

        gold_obj = GoldPrice.objects.filter(active=True).order_by('Date')
        gold_obj = gold_obj[len(gold_obj)-1]

        gold_obj.price_difference = float(price_difference)
        gold_obj.save()

        return {}, 200

    except:

        return {

            'responseEN': 'we didn\'t define setting ',
            'responseFA': 'تنظیمات اعمال نشده است '

        }, 400


