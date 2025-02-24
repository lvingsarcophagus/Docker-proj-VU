import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import time
import os  # For creating the results directory

def fetch_crypto_prices():
    url = "https://coinmarketcap.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    crypto_data = []
    table = soup.find('table')
    if not table:
        print("Error: Could not find the table of cryptocurrencies.")
        return pd.DataFrame([])

    rows = table.find_all('tr')[1:11]  # Get top 10 cryptocurrencies
    
    for row in rows:
        columns = row.find_all('td')
        if len(columns) >= 4:  # Ensure there are enough columns
            try:
                name = columns[2].find('p').text.strip()
                price_text = columns[3].find('span').text.strip().replace('$', '').replace(',', '')
                price = float(price_text)
                crypto_data.append({'Name': name, 'Price': price})
            except (AttributeError, ValueError) as e:
                print(f"Error parsing row: {e}")
    
    return pd.DataFrame(crypto_data)

def visualize_data(df, results_folder):
    plt.figure(figsize=(12, 6))
    plt.bar(df['Name'], df['Price'])
    plt.title('Top 10 Cryptocurrency Prices')
    plt.xlabel('Cryptocurrency')
    plt.ylabel('Price (USD)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(results_folder, 'crypto_prices.png'))  # Save to results folder
    plt.close()

def main():
    results_folder = 'results'
    
    # Create results folder if it doesn't exist
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)
        print(f"Created directory: {results_folder}")
    
    print("Current working directory:", os.getcwd())  # Print the current working directory
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=1)
    
    all_data = []
    
    while datetime.now() < end_time:
        try:
            df = fetch_crypto_prices()
            if not df.empty:
                all_data.append(df)
                print(f"Data fetched at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                visualize_data(df, results_folder)  # Pass results folder to the visualization function
            else:
                print("No data fetched in this cycle.")
            time.sleep(10)  # Wait for 10 seconds before next fetch
        except Exception as e:
            print(f"An error occurred: {e}")
    
    # Combine all data and save to CSV in the results folder
    if all_data:
        combined_data = pd.concat(all_data, ignore_index=True)
        combined_data.to_csv(os.path.join(results_folder, 'crypto_prices_history.csv'), index=False)  # Save to results folder
        print("Data collection completed. Results saved to 'results/crypto_prices_history.csv' and 'results/crypto_prices.png'")
    else:
        print("No data collected.")

if __name__ == "__main__":
    main()
