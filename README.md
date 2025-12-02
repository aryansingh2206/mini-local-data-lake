# 🗂️ Local AWS-Style Mini Data Lake

A lightweight, AWS-style data lake implemented locally using Python.  
The project simulates the raw → processed → curated architecture found in cloud data lakes, complete with data cleaning, transformation, normalization, and Parquet-based partitioning.

---

## ⭐ Features

- **Data Lake Zones**
  - `raw/` – unprocessed incoming data  
  - `processed/` – cleaned & normalized data  
  - `curated/` – optimized, partitioned parquet files  

- **Python ETL Pipeline**
  - Cleaning missing & inconsistent values  
  - Category normalization  
  - Price column standardization  
  - Synthetic date assignment for partitioning  
  - Year-based Parquet output  

- **Tech Stack**
  - Python  
  - Pandas  
  - PyArrow  

---

## 📂 Folder Structure
```

local-data-lake/
│── raw/
│── processed/
│── curated/
│── scripts/
│     ├── process.py
│     └── transform.py
│── requirements.txt
│── .gitignore
│── README.md

````

---

## 🚀 How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
````

### 2️⃣ Add your dataset

Place your dataset here:

```
raw/sales.csv
```

### 3️⃣ Process the data (cleaning + normalization)

```bash
python scripts/process.py
```

Output:

```
processed/sales_cleaned.csv
```

### 4️⃣ Transform & partition the data (curated zone)

```bash
python scripts/transform.py
```

Output example:

```
curated/
   year=2022/sales.parquet
   year=2023/sales.parquet
```

---

## 🛠 Example Transformations

* Converted price fields to numeric
* Normalized category values
* Fixed missing rating fields
* Added synthetic partitioning dates
* Partitioned output by year using Parquet

---

## 📊 Example Use Cases

* Demonstrating data lake architecture without AWS
* Practicing ETL & data engineering fundamentals
* Portfolio project for Data Engineering interviews
* A template for future cloud migration (S3/Glue/Athena)

---

## 📌 Future Enhancements

* Add metadata catalog
* Add schema validation
* Add real ingestion script
* Convert to Delta Lake format
* Add Airflow/Dagster orchestration


Just tell me!
```
