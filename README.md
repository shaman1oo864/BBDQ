# BBDQ
Bollinger Band Double Quantum - Bot

Hi.
So, what does this bot do?
Buys cheap, sells expensive.
The purchase criterion is the intersection of the crypto asset price with the lower BB line from bottom to top.
The sale criterion is the intersection of the crypto asset price with the upper BB line from top to bottom.
All transactions have a fixed value, which makes it possible not to close the entire position,
but to follow the trend.
If the trend is in the opposite direction, the bot will be in the minus, 
but if you do not interfere with it, it will fix everything.

For trading, I recommend using 10 percent or less of the deposit.
I do not recommend leverage higher than 5x.

It is better to use a symbol from the 1 - 50 position by capitalization and minimum volatility.

I use Python ver. 3.13 (64 bit). Also Need install:

pip install ccxt

pip install numpy

pip install pandas

I made an exe file for several bot configurations:
1. pip install pyinstaller
2. In the command line, go to the directory with the bot, for example, cd c:\1
3.pyinstaller --onefile bbdq_h_BTC_30.py

pyinstaller --onefile bbdq_h_ETH_30.py

pyinstaller --onefile bbdq_h_OM_30.py

pyinstaller --onefile bbdq_h_TRX_30.py

pyinstaller --onefile bbdq_subak.py

Sometimes the exchange and the bot lose connection or there is an error, 
it is good to restart the bot (use the task scheduler).
I use a ReStart.bat file that runs the bots.

I'm sure, ccxt can use ANY exchange.

The bot probably has profit and pleasures.

You can thank here:

TRX address:

THWTRuhMbsE42P8q9zSvioMqusiBCb5GQd

TON address:

UQBwW5eZ_kNFPBiCgpbm8iMzydTlijwmDB3UAxBj9E8oGIBe

SOL address:

GbACHstTsSnEARWykTDrRi2ES31d166z7oDHprWm3k9i
