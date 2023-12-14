from django.utils import timezone

from Core.models.gold import GoldPrice
from Core.models.stock import SaleGold, BuyGold
from LIB.utils import get_user_from_token, check_wallet


def sale_gold(token_key, gold_amount):

    status, user, _ = get_user_from_token(token_key)

    if status:

        wallet_obj = check_wallet(user)

        if wallet_obj.gold_stock >= gold_amount:

            gold_price_obj = GoldPrice.objects.filter(active=True).filter(stock_status=True)

            if len(gold_price_obj) > 0:

                gold_price_obj = gold_price_obj[0]

                # calculate gold price
                gold_price = float(gold_amount) * gold_price_obj.sale_price

                sale_gold_obj = SaleGold(

                    user=user,
                    sale_date=timezone.now(),
                    money_amount=gold_price,
                    gold_amount=gold_amount,

                )

                sale_gold_obj.save()

                sale_gold_obj.gold_price.add(gold_price_obj)

                sale_gold_obj.save()

                return {

                    'responseEN': 'successfully received , after admin approved money will add to your wallet',
                    'responseFA': 'درخواست شما با موفقیت دیافت شد .'
                                   ' به محض تایید این درخواست توسط ادمین مبلغ فروش طلا به کیف پول شما اضافه میشود'

                }, 200

            else:

                return {

                    'responseEN': 'failed . stock closed ',
                    'responseFA': 'بازار خرید و فروش بسته میباشد'
                }, 400
        else:

            return {

                'responseEN': 'failed . you gold amount are out of range',
                'responseFA': 'مقدار طلای درخواستی شما بیشتر از مقدار طلای موجود در کیف پول شماست'
            }, 400

    else:

        return {

            'responseEN': 'user not found',
            'responseFA': 'کاربر یافت نشد'
        }, 400


def buy_gold(token_key, gold_amount):

    _, user, _ = get_user_from_token(token_key)

    gold_price_obj = GoldPrice.objects.filter(active=True).filter(stock_status=True)

    if len(gold_price_obj) > 0:

        gold_price_obj = gold_price_obj[0]

        if gold_amount <= gold_price_obj.total_gold_stock:

            gold_price = gold_amount * gold_price_obj.sale_price + gold_price_obj.price_difference

            buy_gold_obj = BuyGold(

                user=user,
                buy_date=timezone.now(),
                money_amount=gold_price,
                gold_amount=gold_amount,
                request_status=True,

            )

            buy_gold_obj.save()

            buy_gold_obj.gold_price.add(gold_price_obj)

            buy_gold_obj.save()

            wallet_obj = check_wallet(user)
            wallet_obj.gold_stock = wallet_obj.gold_stock + gold_amount
            wallet_obj.save()

            gold_price_obj.total_gold_stock = gold_price_obj.total_gold_stock - gold_amount
            gold_price_obj.save()

            return {

                'responseEN': 'successfully received , after admin approved gold will add to your wallet',
                'responseFA': 'درخواست شما با موفقیت دیافت شد .'
                               ' به محض تایید این درخواست توسط ادمین طلای درخواستی به کیف پول شما اضافه میشود'

            }, 200

        else:

            return {

                'responseEN': 'your requests gold amount is out of range',
                'responseFA': 'طلای درخواستی شما بیش تر از مقدار موجود طلا در انبار است'
            }, 400

    else:

        return {

            'responseEN': 'stock are closed',
            'responseFA': 'بازار خرید و فروش بسته می باشد'
        }, 400
