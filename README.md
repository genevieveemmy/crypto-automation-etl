# Real-Time Crypto Market Tracker & Metrics Pipeline

## 📌 Project Overview
This project is an automated, end-to-end data engineering pipeline designed to ingest, store, and track real-time cryptocurrency market trends. The infrastructure is entirely containerized using Docker, utilizing Apache Airflow for workflow orchestration, MySQL as the relational storage layer, and Grafana for live telemetry and analytical visualizations.

## 🏗️ Architecture & Tech Stack
The architecture implements a standard metrics collection and time-series monitoring pipeline:

```text
[CoinGecko API] 
       │ (Python Script)
       ▼
[Apache Airflow] ────► [MySQL Database] ────► [Grafana]
 (Orchestrator)          (Docker Storage)     (Live Dashboard)
```

*   **Orchestration:** **Apache Airflow 2.5.1** configured in `standalone` mode to schedule hourly execution scripts.
*   **Containerization:** **Docker & Docker Compose** to provision and network isolated microservices locally.
*   **Storage:** **MySQL 8.0** relational database engine optimized for transactional tracking.
*   **Visualization:** **Grafana (Latest)** web-based visualizer pulling directly from the database layer.

## 🗂️ Repository Structure
```text
├── dags/
│   └── crypto_pipeline_dag.py   # Airflow DAG automation file
├── scripts/
│   └── crypto_fetcher.py        # Python API ingestion script
├── docker-compose.yml           # Multi-container Docker configuration
└── README.md                    # Project documentation
```

## 🚀 How to Run Locally

### Prerequisites
*   [Docker Desktop](https://docker.com) installed and running.

### Step 1: Clone the Repository
```bash
git clone https://github.com
cd crypto-metrics-pipeline
```

### Step 2: Spin Up the Infrastructure
Launch your isolated environments in detached background mode using your compose configuration:
```bash
docker compose up -d
```

### Step 3: Trigger the Data Pipeline
1. Open your browser and navigate to the Airflow Web UI at **`http://localhost:8080`**.
2. Locate your crypto workflow DAG and toggle it **On**.
3. Trigger a manual run to execute your Python script and load data into the database.

### Step 4: Configure Grafana Visualizations
1. Navigate to Grafana at **`http://localhost:3000`** (Default credentials: username `admin` / password `admin`).
2. Go to **Connections > Data Sources > Add Data Source** and choose **MySQL**.
3. Fill in the connection properties matching the container network configurations:
   * **Host:** `crypto_mysql:3306` (Uses Docker internal service bridge)
   * **Database:** `crypto_data`
   * **User:** `data_worker`
   * **Password:** `cryptopassword`
4. Click **Save & Test**. You can now construct time-series dashboard panels.

## 📊 Key Data Engineering Principles Demonstrated
*   **Containerized Portability:** Eliminated local system dependency issues by packing computing, storage, and analytics tools into isolated environments.
*   **Database Management:** Leveraged isolated environment credentials (`crypto_data`) using secure schemas to manage data access layers.
*   **Decoupled Architecture:** Separated storage (MySQL) from execution engines (Airflow) and presentation software (Grafana) to align with enterprise design standards.
