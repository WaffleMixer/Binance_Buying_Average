import csv


def average_counter():
    coin_price = {}
    coin_amount = {}

    first_line = True
    with open('price_data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if first_line == True:
                first_line = False
            else:
                executed = row[4]
                coin_name = ''
                for i in executed:
                    if i.isdigit() or i == '.' or i == ',':
                        pass
                    else:
                        coin_name += i
                buy_price = float(row[3].replace(',', ''))

                if ',' in row[4]:
                    amount = row[4].replace(coin_name, '')
                else:
                    amount = float(row[4].replace(coin_name, ''))
                try:
                    if ',' in amount:
                        amount = float(amount.replace(',', ''))
                except:
                    pass

                buy_or_sell = row[2]

                if buy_or_sell == 'BUY':
                    if coin_name in coin_price:
                        coin_price[coin_name] += buy_price * amount
                    else:
                        coin_price[coin_name] = buy_price * amount

                    if coin_name in coin_amount:
                        coin_amount[coin_name] += amount
                    else:
                        coin_amount[coin_name] = amount

    for coin in coin_price:
        average_price = coin_price[coin]/coin_amount[coin]
        print(f'average buy price of {coin}:', average_price)


average_counter()
