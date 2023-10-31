# Template using the dictionary data.
# Your Template must have at least two sentences.
# USD must be converted to BDT
# Example Output: Xiaomi Note 5 is made in China. The price is 300 USD which is almost equal to 30975 BDT

mobile_data = {
    'status': True,
    'data': [
          {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
          {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
          {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
          {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
          {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
          {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
            ],
    'exchnage_rate': 107.25
            }

i = 0
while i < len(mobile_data['data']):
    mobile_names = mobile_data['data'][i]['name']
    price_data = float(mobile_data['data'][i]['price'][:-4])
    Exchange_rate = float(mobile_data['exchnage_rate'])
    Origin_Country = mobile_data['data'][i]['made']
    mobile_individul_price_BDT = price_data * Exchange_rate
    template = f'{mobile_names} is made in {Origin_Country}. The price is {price_data} USD which is almost equal to {mobile_individul_price_BDT} BDT'
    i = i + 1
    print(template)







