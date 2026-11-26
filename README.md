# 📊 URBAN PULSE — NYC 311 Complaint Intelligence & Resolution Analytics

An interactive data analytics dashboard built using Python, SQL concepts, Pandas, Plotly and Streamlit to investigate New York City's 311 service requests.

## 🚀 Live Dashboard

**Streamlit App:** Add your permanent Streamlit Community Cloud URL here after deployment.

## 📌 Project Overview

URBAN PULSE is a data analytics project designed to analyze NYC 311 service request data and understand public complaint patterns, agency workload, borough-wise demand, resolution performance and geographical complaint concentration.

The project includes 15 core analyst investigations, interactive visualizations, dynamic filters and automated analytical interpretations.

## 🎯 Project Objectives

- Analyze total distinct service request volume.
- Identify the most frequently reported complaint categories.
- Evaluate agency-wise workload distribution.
- Compare complaint volumes across NYC boroughs.
- Analyze monthly, weekday and hourly complaint trends.
- Examine service request status distribution.
- Evaluate resolution time and statistical patterns.
- Identify unusually long resolution durations using IQR.
- Analyze geographical complaint concentration.
- Compare recorded closure rates across agencies.
- Identify high-volume complaint categories with longer median resolution times.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| Pandas | Data cleaning and manipulation |
| NumPy | Numerical operations |
| Plotly | Interactive data visualizations |
| Streamlit | Dashboard development |
| SQL / MySQL | Database management and querying |
| GitHub | Version control and project hosting |
| Streamlit Community Cloud | Dashboard deployment |

## 📂 Dataset Information

**Data Source:** NYC 311 Service Requests

The dataset contains service request information, including:

- Unique Request ID
- Created Date
- Closed Date
- Agency
- Complaint Type
- Descriptor
- Borough
- Request Status
- Latitude
- Longitude

The dashboard calculates resolution duration using the created and closed timestamps.

## 🔍 15 Core Analyst Investigations

### 1. Total Distinct Request Volume
Calculates the total number of unique NYC 311 service requests.

### 2. Top 10 Complaint Categories by Count
Identifies the most frequently reported complaint categories.

### 3. Agency Workload Distribution
Compares the number of requests handled by each agency.

### 4. Request Volume by Borough
Identifies boroughs with the highest complaint volumes.

### 5. Monthly Request Trend
Examines monthly variations in service request volume.

### 6. Demand by Weekday and Hour
Identifies peak reporting days and hours using temporal analysis.

### 7. Distribution of Recorded Request Statuses
Analyzes the distribution of Closed, Open, In Progress and other recorded statuses.

### 8. Descriptive Statistics for Valid Resolution Durations
Examines resolution-time statistics such as mean, median, minimum, maximum and standard deviation.

### 9. Median Resolution Duration by Complaint Category
Compares median resolution times across complaint categories.

### 10. Median Resolution Duration by Agency
Evaluates differences in median resolution durations among agencies.

### 11. IQR-Based Outlier Investigation
Uses the Interquartile Range method to identify unusually short or long resolution durations.

### 12. Resolution-Time Skewness and Distribution
Examines the distribution and skewness of resolution durations.

### 13. Geographic Complaint Concentration
Uses geographical coordinates to identify complaint clusters and spatial demand patterns.

### 14. Recorded Closure-Rate Comparison
Compares the percentage of recorded closed requests across agencies.

### 15. Categories with High Volume and Long Median Resolution
Identifies complaint categories that combine high request volume with longer median resolution durations.

## 📊 Dashboard Features

- Interactive date-range filter
- Borough selection
- Agency selection
- Dynamic KPI metrics
- Interactive Plotly charts
- Automated analyst interpretations
- Resolution-time statistical analysis
- Geographical complaint visualization
- All 15 investigations displayed separately
- Filter-based analytical updates

## 📈 Key Dashboard Findings

Based on the displayed dataset and selected filters:

| Metric | Result |
|---|---:|
| Distinct Requests | 75,139 |
| Recorded Closed Requests | 51,343 |
| Recorded Closure Rate | 68.33% |
| Valid Median Resolution | 2.50 hours |
| Valid Resolution Records | 53,172 |
| Usable NYC Coordinates | 73,952 |
| IQR Outliers | 7,273 |
| High-Volume and Long-Resolution Categories | 34 |

### Key Insights

- Illegal Parking is the leading complaint category, with 13,489 requests.
- NYPD has the highest recorded workload, with 31,545 requests.
- Brooklyn has the highest complaint volume, with 24,282 requests.
- Tuesday at 11:00 is the busiest reporting period.
- OTI has the highest median resolution duration at 114 hours.
- HEAT/HOT WATER has 9,724 requests and a median resolution time of 50.51 hours among the identified high-volume and long-resolution categories.

*Note: These findings reflect the currently displayed dataset and filter selection. They may change when dashboard filters are modified.*

## ⚙️ Project Workflow

1. Collect NYC 311 service request data.
2. Load the dataset using Pandas.
3. Clean and prepare the data.
4. Handle missing values and duplicate records.
5. Convert date columns into appropriate datetime formats.
6. Calculate resolution durations.
7. Perform exploratory data analysis.
8. Conduct the 15 analyst investigations.
9. Create interactive charts using Plotly.
10. Develop the Streamlit dashboard.
11. Deploy the application using Streamlit Community Cloud.

## 💻 Run the Project Locally

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/urban-pulse-nyc-311-analytics.git
```

### Step 2: Navigate to the project folder

```bash
cd urban-pulse-nyc-311-analytics
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Streamlit application

```bash
streamlit run app.py
```

The dashboard will open in your local browser.

## 📁 Repository Structure

```text
urban-pulse-nyc-311-analytics/
│
├── app.py
├── urbanpulse_dashboard_data.csv
├── requirements.txt
└── README.md
```

## 💡 Project Outcome

URBAN PULSE transforms NYC 311 service request data into an interactive analytical dashboard. It demonstrates practical skills in data cleaning, exploratory data analysis, statistical investigation, data visualization and dashboard development.

The project helps identify public service demand patterns, workload distribution and resolution-time differences to support data-driven decision-making.

## 👩‍💻 Author

**Dharani Bommi K**

M.Sc. Microbiology

---

*URBAN PULSE — Turning Public Service Data into Actionable Insights.*
