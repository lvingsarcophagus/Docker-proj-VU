Cryptocurrency Price Fetcher

This project is a Python script that fetches the top 10 cryptocurrency prices from CoinMarketCap every 10 seconds for a duration of 1 minute. The fetched data is then visualized using a bar chart and saved as a CSV file for historical reference.
Features

    Data Fetching: Fetches the top 10 cryptocurrency prices from CoinMarketCap.

    Visualization: Generates a bar chart of the fetched cryptocurrency prices.

    Data Storage: Saves the fetched data in a CSV file for historical analysis.

    Dockerized: The project is containerized using Docker for easy deployment and execution.

Prerequisites

    Python 3.9

    Docker (optional, for containerized execution)

Installation

    Clone the repository:

    git clone https://github.com/yourusername/cryptocurrency-price-fetcher.git
    cd cryptocurrency-price-fetcher

    Install dependencies:

    pip install -r requirements.txt

    Run the script:

    python Cryptopricefetch.py

Docker Usage

    Build the Docker image:

    docker build -t crypto-price-fetcher .

    Run the Docker container:

    docker run -v $(pwd)/results:/app/results crypto-price-fetcher

    This command will run the script inside the Docker container and save the results in the results directory on your host machine.

Project Structure

    Cryptopricefetch.py: The main script that fetches cryptocurrency prices, visualizes the data, and saves it.

    Dockerfile: Dockerfile to containerize the application.

    requirements.txt: List of Python dependencies.

    results/: Directory where the output files (CSV and PNG) are saved.

Output

    CSV File: results/crypto_prices_history.csv - Contains the historical data of cryptocurrency prices fetched during the script's execution.

    PNG File: results/crypto_prices.png - A bar chart visualizing the top 10 cryptocurrency prices.

Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
License

This project is licensed under the MIT License - see the LICENSE file for details.
