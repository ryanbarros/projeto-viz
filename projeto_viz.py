import pandas as pd
import matplotlib.pyplot as plt

def main():
    # === 1. Carrega os dados ===
    url = 'https://raw.githubusercontent.com/ryanbarros/projeto-viz/main/USD_BRL_hist.csv'
    df = pd.read_csv(url, dayfirst=True, parse_dates=['Data'])
    df.rename(columns={'Data':'Date','USD_BRL':'Rate'}, inplace=True)
    df.set_index('Date', inplace=True)

    # === 2. Gráfico 1: Série temporal ===
    plt.figure(figsize=(10,5))
    df['Rate'].plot()
    plt.title('USD → BRL ao longo do tempo')
    plt.ylabel('Cotação (R$)')
    plt.tight_layout()
    plt.savefig('line_rate.png')
    plt.close()

    # === 3. Gráfico 2: Média anual ===
    annual = df['Rate'].resample('Y').mean()
    annual.index = annual.index.year
    plt.figure(figsize=(8,5))
    annual.plot.bar()
    plt.title('Média anual da cotação USD→BRL')
    plt.ylabel('Média anual (R$)')
    plt.tight_layout()
    plt.savefig('bar_annual.png')
    plt.close()

    # === 4. Gráfico 3: Distribuição de retornos (%) ===
    df['Return_%'] = df['Rate'].pct_change() * 100
    plt.figure(figsize=(8,5))
    df['Return_%'].dropna().hist(bins=50)
    plt.title('Distribuição dos retornos diários (%)')
    plt.xlabel('Retorno (%)')
    plt.ylabel('Frequência')
    plt.tight_layout()
    plt.savefig('hist_returns.png')
    plt.close()

    print("Gráficos gerados: line_rate.png, bar_annual.png e hist_returns.png")

if __name__ == '__main__':
    main()
