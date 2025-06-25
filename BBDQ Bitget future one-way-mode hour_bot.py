import time
import ccxt
import numpy as np
import pandas as pd
from datetime import datetime

exchange = ccxt.bitget({
	'apiKey': 'YOUR_API_KEY',
	'secret': 'YOUR_API_SECRET',
	'password': 'YOUR_PASSWORD',
	'options': {'defaultType': 'future'}
})

symbol = 'TRX/USDT:USDT'
b = 6 					# USDT per trade (need more than 5 USDT)
q = 0 					# number of contracts per trade, the bot will count below
comma = 0			  	# digits after the decimal point in high prices to determine the minimum contract.
					# for example, the minimum amount to open is 0.0001 BTC, we write 4.
period = 24				# period of Bollinger bands 3 14 20 24 or other
d = 2				    	# deviation 2 or 3
timeframe = '1h'			# Candle interval. One of the values ​​1h, 2h, 3h, 4h, 6h
tf = 1				  	# tf = timeframe ( 1 = '1h' )
last_time = ''				# will be used for calculations later.
kkb = 1					# Correction Factor for buying
kks = 1					# Correction Factor for selling

TS = exchange.fetchTime() 				# Exchange Time
since = TS - ( period * tf * 60 * 60 * 1000) 		# Period * tf * minute ** seconds * milliseconds
balance = exchange.fetch_balance()
ticker = exchange.fetch_ticker(symbol)
latest_price = ticker['bid']
q = b / latest_price
qb = round((q * kkb), comma)
qs = round((q * kks), comma)
if comma == 0:
	qb = round((q * kkb), )
	qs = round((q * kks), )

tfsys = time.time() * 1000

print("")
print(datetime.now(), "The difference in Exchange Time and System Time =", round((TS - tfsys) / 1000, 2), "sec.")
print("                                   Need NOT more than 30 sec.")
print("Balance = ", balance['USDT'])
print(symbol," = ", latest_price)
print("USDT Per trade  buy = ", round(qb * latest_price, 2), "Quantity of contracts =", qb)
print("USDT Per trade sell = ", round(qs * latest_price, 2), "Quantity of contracts =", qs)

ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since = since, limit = period)
df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')	# df # print(df.head(24)) #print(df)

prices = df['close'].tolist() 					# list to keep all closing prices. #print(prices)

bollinger_band_high_values = [prices[period-1], prices[period-1], prices[period-1]]
bollinger_band_low_values = [prices[period-1], prices[period-1], prices[period-1]]

#order = exchange.createOrder(symbol, 'limit', 'buy', qb, bollinger_band_low_values[-1])
#order = exchange.createOrder(symbol, 'limit', 'sell', qs, bollinger_band_high_values[-1])
print("That's it, I'm working. I'm waiting for conditions to buy or sell ...")


def order_buy():
	if prices[-1] > bollinger_band_low_values[-1] and prices[-2] < bollinger_band_low_values[-2]:
		exchange.createOrder(symbol, 'limit', 'buy', qbb, bollinger_band_low_values[-1])
		print(current_time.strftime("%Y-%m-%d %H:%M"), symbol, timeframe, qbb, " Buy by", round(bollinger_band_low_values[-1], 5))
	return

def order_sell():
	if prices[-2] > bollinger_band_high_values[-2] and prices[-1] < bollinger_band_high_values[-1]:
		exchange.createOrder(symbol, 'limit', 'sell', qss, bollinger_band_high_values[-1])
		print(current_time.strftime("%Y-%m-%d %H:%M"), symbol, timeframe, qss, " Sell by", round(bollinger_band_high_values[-1], 5))
	return

# Main loop
while True:
	current_time = datetime.now()
	time.sleep(20)
	if current_time.hour % tf == 0 and current_time.strftime("%H") != last_time:
		last_time = current_time.strftime("%H")
		time.sleep(5)
		latest_price = (exchange.fetch_ticker(symbol))['bid']
		prices.append(latest_price)
		ma = np.mean(prices[-period:])
		ma = round(ma, 6)
		std = np.std(prices[-period:], ddof=1)
		bb_high = ma + (d * std)
		bb_low = ma - (d * std)
		bollinger_band_high_values.append(bb_high)
		bollinger_band_low_values.append(bb_low)
		#print(current_time.strftime("%Y-%m-%d %H:%M"), "bb_high =", round(bb_high, 5), "latest_price =",latest_price, "bb_low =", round(bb_low, 5))
		Posit = exchange.fetchPosition (symbol) # Leveling the number of contracts.
		pos = Posit['info']
		q_old = int(pos.get('total'))
		if q_old < qb:
			qbb = 2*qb-q_old
		else:
			qbb = qb
		order_buy()
		if q_old < qs:
			qss = 2*qs-q_old
		else:
			qss = qs
		order_sell()
		prices = prices[1:]
		bollinger_band_high_values = bollinger_band_high_values[1:]
		bollinger_band_low_values = bollinger_band_low_values[1:]


