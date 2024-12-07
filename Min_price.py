
def calc_min_price(purchases, commission_rate):
    total_usdt_spent = 0
    total_crypt_bought = 0

    for buy_price, entry_price in purchases:
        # Рассчитаем количество крипты, которое можно купить с учетом комиссии
        tot_crypt = buy_price / entry_price * (1 - commission_rate)

        # Добавляем в общий объем затраченные средства и количество купленной крипты
        total_usdt_spent += buy_price
        total_crypt_bought += tot_crypt

    # Рассчитаем минимальную цену продажи, чтобы выйти в ноль
    min_sell_price = total_usdt_spent / total_crypt_bought / (1 - commission_rate)

    return min_sell_price
