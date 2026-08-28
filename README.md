# 🏥 Healthcare Analytics & Power BI Dashboard

> **Turning healthcare data into actionable insights for operational, clinical, and financial decision-making.**

## 📌 Project Overview

This project analyzes a healthcare dataset of **25,000+ patient records** to identify patterns in **patient demographics, medical conditions, admissions, length of stay, billing, insurance, and hospital performance**.

The project demonstrates an end-to-end analytics workflow, from **data cleaning with Python** to **data modelling, DAX analysis, and interactive dashboard development in Power BI**.

## 🎯 Business Objectives

* Analyze patient demographics and healthcare utilization
* Identify the most frequent and highest-cost medical conditions
* Monitor admission and discharge patterns
* Analyze billing and insurance performance
* Evaluate provider and hospital workload
* Develop interactive KPIs and dashboards for decision support

## 🛠️ Tools & Technologies

| Tool                      | Application                                |
| ------------------------- | ------------------------------------------ |
| 🐍 **Python / Pandas**    | Data cleaning & preparation                |
| 📊 **Power BI**           | Data modelling & dashboard development     |
| ⚡ **DAX**                 | KPI calculations & analytical measures     |
| 📈 **Data Visualization** | Trend, segmentation & performance analysis |
| 🗃️ **Kaggle**            | Healthcare dataset source                  |

## 🔄 Analytics Workflow

**Raw Data → Python Cleaning → Data Preparation → Power BI Model → DAX Measures → Interactive Dashboards → Insights → Recommendations**

### Data Preparation

* Removed duplicate patient records
* Handled missing admission dates
* Cleaned inconsistent clinical categories
* Prepared data for Power BI modelling

### Analysis

Developed KPIs and analytical measures covering:

* Patient volume
* Average age
* Average billing
* Length of stay
* Admissions & discharges
* Readmission rate
* Diagnosis frequency
* Insurance billing
* Provider workload

## 📊 Key Results

| KPI                           |     Result |
| ----------------------------- | ---------: |
| **Patient Records**           |     25,110 |
| **Average Age**               | 51.8 years |
| **Average Billing / Patient** |    $26,879 |
| **Average Length of Stay**    |  15.5 days |
| **Readmission Rate**          |       8.7% |
| **Medical Conditions**        |          6 |

### 🔎 Key Insights

* **Arthritis** was the most frequently recorded condition, with approximately **4.4K cases** and **$112M in billing**.
* **Elective, emergency, and urgent admissions** were relatively balanced at approximately **8.1K–8.5K records** each.
* Longer **hospital stays were associated with higher billing**, highlighting an important operational and financial relationship.
* **2020** recorded the highest reported billing at approximately **$132M**.
* **UnitedHealthcare and Medicare** represented the largest shares of insurance payments in the dashboard analysis.
* Discharge activity declined significantly in **2024**, although the report notes that incomplete-year data may explain the reduction.

## 📈 Dashboard

The Power BI solution provides interactive views for:

1. **Executive Overview**
   
![Executive Overview](dashboard_images/Dashboard%201-Executive%20Overview.png)

2. **Patient Demographics**
   
![Patient Demographics](dashboard_images/Dashboard%202-Patient%20Demographics.png)

3. **Medical Conditions & Outcomes**

![Medical Condition & Outcomes](dashboard_images/Dashboard%203%20-%20Medical%20Condition%20%26%20Outcomes.png)

4. **Financial & Billing Analysis**

![Financial & Billing Analysis](dashboard_images/Dashboard%204%20-%20Financial%20%26%20Billing%20Analysis.png)

5. **Admission & Operation Analysis**

![Admission & Operational Analysis](dashboard_images/Dashboard%205-%20Admission%20%26%20Operation%20Analysis.png)

6. **Diagnosis Analysis**

![Diagnosis Analysis](dashboard_images/Dashboard%206-%20Diagnosis%20Analysis.png)
Users can explore the data through **filters, KPIs, trends, category comparisons, and interactive visualizations**.

## 💡 Business Recommendations

The analysis supports several potential actions:

* Focus care-management strategies on high-cost conditions.
* Optimize patient length of stay and discharge processes.
* Monitor admission and discharge patterns for better resource allocation.
* Use insurance and billing data to support financial planning.
* Monitor provider workloads and billing consistency.
* Expand dashboards toward real-time operational monitoring.

## 🚀 Future Improvements

* Add predictive forecasting for admissions and billing
* Implement anomaly detection for unusual billing patterns
* Introduce automated data refresh
* Add department-level analysis
* Integrate additional clinical and hospital datasets
* Apply statistical testing to validate observed relationships

## 📂 Project Structure

```text
Healthcare-Analytics/
│
├── data/
│   └──raw data
         └── healthcare_dataset.csv
│
├── python/
│   └── data_analysis.py
│
├── powerbi/
│   └── Healthcare Dataset Analysis.pbix
│
├── dashboard_images/
    
│   ├── dashboard 1-overview.png

│   ├── dashboard 2-patient Demographics.png

│   ├── dashboard 3-medical conditions & outcomes.png

│   ├── dashboard 4-financial & billing analysis.png

│   ├── dashboard 5-Admission & operation analysis.png

│   └── dashboard 6-diagnosis.png

│
├── reports/
│   └── healthcare_analysis_report.pdf
│
└── README.md
```

## 🎯 Skills Demonstrated

**Python • Pandas • Data Cleaning • Exploratory Data Analysis • SQL/Data Analytics • Power BI • DAX • Data Modelling • KPI Development • Data Visualization • Business Intelligence • Healthcare Analytics • Insight Generation**

---

### 📌 Project Takeaway

This project demonstrates the ability to transform **raw healthcare data into a structured Business Intelligence solution**, combining technical data preparation with analytical thinking and business-focused visualization to support **operational, clinical, and financial decision-making**.









