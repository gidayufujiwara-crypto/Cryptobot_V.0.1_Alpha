def generate_signal(df):
    sma = df['sma_200'].iloc[-1]
    rsi = df['rsi'].iloc[-1]
    macd = df['macd'].iloc[-1]
    signal = df['signal'].iloc[-1]

    signal_output = None
    reasons = []

    if rsi < 30:
        signal_output = 'BUY'
        reasons.append('RSI < 30 (oversold)')
    elif rsi > 70:
        signal_output = 'SELL'
        reasons.append('RSI > 70 (overbought)')

    if macd > signal:
        reasons.append('MACD crossover bullish')
        if not signal_output:
            signal_output = 'BUY'
    elif macd < signal:
        reasons.append('MACD crossover bearish')
        if not signal_output:
            signal_output = 'SELL'

    if df['close'].iloc[-1] > sma:
        reasons.append('Harga > SMA200 (bullish trend)')
    else:
        reasons.append('Harga < SMA200 (bearish trend)')

    return signal_output, reasons
