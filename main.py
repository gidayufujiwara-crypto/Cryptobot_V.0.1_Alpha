from indodax_api import fetch_indodax_ohlc
from indicators import calculate_rsi, calculate_sma, calculate_macd
from signals import generate_signal

def main():
    df = fetch_indodax_ohlc()

    df['sma_200'] = calculate_sma(df, 200)
    df['rsi'] = calculate_rsi(df, 14)
    df['macd'], df['signal'], df['hist'] = calculate_macd(df)

    signal, reasons = generate_signal(df)

    print(f"Pair: BTC/IDR")
    print(f"Time: {df['time'].iloc[-1]}")
    print(f"Sinyal: {signal}")
    print("Alasan:")
    for r in reasons:
        print(f" - {r}")

if __name__ == "__main__":
    main()
