import telebot
import yfinance as yf
import pandas_ta as ta

TOKEN = '8522441030:AAHUMvDVcGdexx_H6j17rC0Hy4pGFpdSCDI'
bot = telebot.TeleBot(TOKEN)
CHANNEL_ID = '@AapkaChannelName' # Faraz 3.O apne channel ka naam daalein

def check_market():
    # BTC ka data 15 minute ke interval par
    data = yf.download("BTC-USD", period="1d", interval="15m")
    rsi = ta.rsi(data['Close'], length=14).iloc[-1]
    
    if rsi < 30:
        bot.send_message(CHANNEL_ID, "🔥 BUY SIGNAL: BTC is Oversold (RSI: {:.2f})".format(rsi))
    elif rsi > 70:
        bot.send_message(CHANNEL_ID, "📉 SELL SIGNAL: BTC is Overbought (RSI: {:.2f})".format(rsi))

check_market()
