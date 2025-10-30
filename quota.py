'''This program is aimed at helping small business owners fix 
prices for products and potentially services'''
#variables
cost_price= int (input('Input supplier price: '))
vat= float(input('How much in % was paid for vat? '))
packaging= 3 #fixed unit
customs= float(input('How much in % was paid for customs? '))
shipping= 9 #fixed unit
products_sold_per_month= int(input('How many products do you sell in a month? '))
rent= int(input('How much rent do you pay? '))
marketing= 1 #fixed unit
profit_margin= float(input('What in % would you like your profit margin to be? '))

#computations
rent_per_piece= ((rent/2)/products_sold_per_month)
customs_per_piece= ((customs/100)* cost_price)
vat_per_piece= ((vat/100)* cost_price)
profit_per_piece= (profit_margin/100)


price = ((cost_price + rent_per_piece+ customs_per_piece + 
          vat_per_piece+ packaging+ shipping+ marketing) * (1+ profit_per_piece))

price = round(price, 2) #to round price to 2 decimal places

print('Your price for this piece should be: ' + str(price) + ' euros.')