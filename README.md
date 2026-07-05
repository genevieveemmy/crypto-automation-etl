# crypto-automation-etl
Project Title: Real-Time Crypto Market Tracker📊 Problem StatementCryptocurrency markets operate 24/7 with massive price volatility. Investors and analysts need a reliable, automated system to track hourly price fluctuations, calculate rolling averages, and visualize trends without manual intervention. You must build an automated pipeline that ingests live market data, cleans it, stores it in a structured database, and updates a dashboard.

⚙️ # Architecture & Tool IntegrationData Source:
* Fetch live prices using Python from a free public API (e.g., CoinGecko API or CoinDesk API).
* Orchestration: Use Apache Airflow to schedule and run the Python ingestion script every hour.
* Containerisation: Run your Airflow environment and your database inside Docker containers using Docker Compose.
* Storage: Write the ingested data into a SQL database (e.g., PostgreSQL) running in Docker.Transformation:
* Use SQL queries or Python to calculate basic metrics like 24-hour price changes.
* Visualization: Connect Tableau to your SQL database to build a auto-refreshing line chart of price trends.

🛠️#  Step-by-Step Implementation PlanSet Up Docker: 
* Create a docker-compose.yml file to launch Apache Airflow and a PostgreSQL database locally.
* Write Ingestion Script: Create a Python script using the requests library to pull current Bitcoin and Ethereum prices from the API.
* Build SQL Schema: Create a database table with columns for timestamp, coin_name, price_usd, and 24h_volume.
* Create Airflow DAG: Write a simple Directed Acyclic Graph (DAG) with two tasks: Task 1 checks if the API is online, and Task 2 runs your Python ingestion script to append data to SQL.
* Connect Tableau: Open Tableau Desktop, choose the PostgreSQL connector, point it to your local database, and design your trend dashboard.

  ### 🐳 Step 1: Docker Compose Setup
  Create a file named docker-compose.yml. This file pulls and runs PostgreSQL (your SQL database) and Apache Airflow in isolated containers that can easily talk to each other.yam

  ### Step 2: SQL Table Schema



  ### 🐍 Step 3: Python Extraction Script
  Save this script as crypto_fetcher.py. It uses the free, no-auth CoinGecko API to pull live market data for Bitcoin, Ethereum, and Solana, then formats it into a clean list of tuples.

  ### 📈 Step 4: Connecting Tableau

