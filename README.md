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

