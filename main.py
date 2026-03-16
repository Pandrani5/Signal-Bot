import telebot
import yfinance as yf
import pandas_ta as ta

# Yahan apna token daalein
TOKEN = '8522441030:AAHUMvDVcGdexx_H6j17rC0Hy4pGFpdSCDI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['signal'])
def send_signal(message):
    try:
        data = yf.download("BTC-USD", period="1d", interval="15m")
        rsi = ta.rsi(data['Close'], length=14).iloc[-1]
        if rsi < 30:
            msg = "🔥 BUY SIGNAL: BTC is Oversold!"
        elif rsi > 70:
            msg = "📉 SELL SIGNAL: BTC is Overbought!"
        else:
            msg = "Market neutral hai, wait karein."
        bot.reply_to(message, msg)
    except Exception as e:
        bot.reply_to(message, "Error aa gaya: " + str(e))

bot.polling()
