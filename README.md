# weather-telemetry-pipeline

This project collects **hourly weather telemetry data** (e.g., temperature, humidity, wind speed) from the [Open-Meteo API](https://open-meteo.com/) and builds an **end-to-end data pipeline**.

## 🚀 Features
- Fetch weather data from the Open-Meteo API
- Store raw data locally in `data/raw/`
- Transform and clean data into `data/processed/`
- Save datasets in **Delta Lake format** for use with Databricks
- Explore data through interactive **notebooks**
- Version-controlled and reproducible via **GitHub**

## 📂 Project Structure

weather-telemetry-pipeline/
│
├── data/ <- Raw and processed data
│ ├── raw/
│ └── processed/
│
├── notebooks/ <- Databricks notebooks for analysis
│
├── src/ <- Python scripts (ETL pipeline)
│
├── .gitignore
├── README.md



## 🎯 Goals
- Build a **reliable automated pipeline**
- Demonstrate **process optimization** for data engineering
- Create **compelling visual stories** with weather telemetry
