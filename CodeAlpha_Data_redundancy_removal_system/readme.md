# Data Redundancy Removal System

## 📝 Overview

The Data Redundancy Removal System is an efficient tool designed to detect and eliminate duplicate records within large datasets. By utilizing hashing algorithms and data structure optimization, the system ensures data integrity, reduces storage overhead, and improves overall database performance.

## 🚀 Key Objectives

* **Duplicate Detection:** Identifying exact matches and fuzzy duplicates within the dataset.
* **Performance Optimization:** Efficiently processing records to minimize computation time (O(n) complexity).
* **Data Integrity:** Ensuring that original data remains consistent while removing unnecessary redundant entries.
* **Scalability:** Handling large-scale datasets across different file formats (e.g., CSV, JSON).

## 🛠️ Technologies Used

* **Language:** Python
* **Data Processing:** `Pandas`, `NumPy`
* **Hashing Algorithms:** `MD5` or `SHA-256` (for unique fingerprinting of rows).
* **Environment:** Jupyter Notebook / VS Code

## ⚙️ Core Logic

1. **Data Ingestion:** Loading raw datasets from local storage.
2. **Fingerprinting:** Generating a unique hash for every row based on its content.
3. **De-duplication:** Comparing hashes to filter out records that already exist in the target set.
4. **Reporting:** Generating a summary report showing the number of original records vs. unique records and total space saved.

## 📂 Repository Structure

* `/data` — Contains sample datasets used for testing.
* `/src` — The primary script for the redundancy removal engine.
* `/results` — Output files showing the cleaned dataset.

## ⚙️ How to Run

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/redundancy-removal-system.git

```



```
2. **Install dependencies:**
   ```bash
pip install pandas numpy

```

3. **Run the script:**
```bash
python remove_redundancy.py --input data/raw_file.csv --output data/cleaned_file.csv

```



```

## 📈 Status
* Completed as part of the CodeAlpha Data Science internship.

## 📧 Contact
Mitushi Jain
