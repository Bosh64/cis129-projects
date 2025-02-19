#print "hello welcome to my cafe, how much coffee would you like?"
print('hello welcome to my cafe, how much coffee would you like?')
#set coffees and muffins at their respected prices plus give total a value
coffee_price = 5.0
muffin_price = 4.0
total = 0
#assign coffee as the number of coffees the user wants and add to total as well as save the coffee total for later
coffee = int(input())
total += coffee * coffee_price
coffee_total = coffee * coffee_price
#print 'Got it! how much muffins would you like?'
print('Got it! how much muffins would you like?')
#assign muffin as the number of muffins the user wants and add to total as well as save the muffin total for later
muffin = int(input())
total += muffin * muffin_price
muffin_total = muffin * muffin_price
#add the tax to the total
tax = total * 0.06
total_with_tax = total + tax
#print out all of the receipt stuff
print('Okay! your total will be $' + str(total_with_tax) + '.')
print('Here is your receipt!:')
print('Coffees bought: ' + str(coffee) + ' for $' + str(coffee_total) + '.')
print('Muffins bought: ' + str(muffin) + ' for $' + str(muffin_total) + '.')
print('tax: $' + str(tax) + '.')
print('total: $' + str(total_with_tax) + '.')
