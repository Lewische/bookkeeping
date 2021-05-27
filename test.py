import os 
products = []
if os.path.isfile('bookeeping.csv'):
	with open('bookeeping.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if line in 'items, price\n':
				continue
				name, price = line.strip().split(',')
				products.append([name, price])
while True:
   goods = input('請輸入商品名稱: ')
   if goods == 'q':
       break
   price = input('請輸入商品價格: ')
   products.append([goods, price])
for p in products:
	print('已記錄品項', p[0],'價格', p[1], '元')
with open('bookeeping.csv', 'w', encoding = 'utf-8') as f:
	f.write('items, price\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
