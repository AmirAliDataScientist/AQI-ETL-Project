Overview:

This project implements a production-style ETL (Extract, Transform, Load) pipeline in Python to collect Air Quality Index (AQI) data for multiple Indian cities, transform raw API responses into a clean analytical format, and load the processed data into a CSV file for reporting and analysis.

The pipeline is designed with modularity, error handling, and real-world data issues in mind (e.g., missing data, failed API responses).

Key Features:

API - based AQI extraction.
YAML -driven configuration (Cities, API).
Robust handling of failed or incomplete API responses.
Transformation of nested JSON into flat, tabular data.
Derived AQI category (Good, Poor, Severe etc.).
Clean CSV output suitable for analytics and BI tools.
Modular and extensible project structure.



Project Architecture:

ETL_Project/
│
├── src/
│   ├── main.py                # Pipeline orchestration (entry point)
│   ├── extract.py             # API data extraction
│   ├── config_loader.py       # YAML configuration loader
│   └── load/
│       └── loader.py          # Load logic (CSV output)
│
├── transform/
│   └── transform.py           # Data transformation logic
│
├── config/
│   └── config.example.yaml    # Sample configuration (no secrets)
│
├── data/
│   ├── raw/                   # Raw data (ignored in Git)
│   └── processed/             # Processed output (ignored in Git)
│
│
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore rules
└── README.md


ETL Workflow:

1. Extract: Fetch AQI data from an external API for configure cities.
   Handle API failures gracefully. 

2. Transform: Normalize nested AQI JSON response.
   Preserve city records even when AQI data is unavailable.
   Convert pollutant values into analytics-ready columns.
   
3. Load: Store processed data in a CSV file.
   Output is suitable for Excel, BI Tools or Databases.
