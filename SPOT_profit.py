def spot_profit(purchases,  commission_rate, sell_price):
    total_usdt_spent  = 0
    total_crypt_bought = 0

    for buy_price, entry_price in purchases:
        #ПОКУПКА
        # Рассчитаем количество крипты, которое можно купить с учетом комиссии
        tot_crypt = buy_price / entry_price * (1 - commission_rate)

        # Добавляем в общий объем затраченные средства и количество купленной крипты
        total_usdt_spent += buy_price
        total_crypt_bought += tot_crypt

    # ПРОДАЖА
    # Продажа крипты, ед. [USDT]
    sell_crypt = sell_price *  total_crypt_bought * (1-commission_rate)

    # Общая доходность от покупки и продажи крипты
    tot_active = sell_crypt -  total_usdt_spent

    return tot_active
