# 🏙️ URBAN PULSE
## NYC 311 Complaint Intelligence & Resolution Analytics

### 📌 Project Overview
URBAN PULSE is an interactive data analytics dashboard developed to analyze New York City 311 service requests. It helps explore complaint patterns, borough-wise distributions, agency workloads, geographical locations, and complaint resolution times.

The project uses Python, MySQL, Pandas, Plotly, and Streamlit to transform raw service request data into meaningful insights.

### 🎯 Project Objectives
- Analyze NYC 311 service request patterns.
- Identify boroughs with the highest complaint volume.
- Find the most frequently reported complaint categories.
- Evaluate agency-wise complaint handling.
- Analyze complaint resolution times.
- Identify delayed complaints.
- Visualize complaint locations across NYC.
- Support data-driven public service analysis.

### 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| Google Colab | Data cleaning and exploratory analysis |
| Pandas | Data manipulation |
| MySQL | Database storage and SQL analysis |
| Streamlit | Interactive dashboard |
| Plotly | Interactive charts and maps |

### 📊 Dataset Information
- Dataset: NYC 311 Service Requests
- Total records: 99,992
- Original columns: 10
- Calculated columns: 1 (`resolution_hours`)
- Date coverage: October 20–29, 2026

**Dataset fields include:**
- Unique Key
- Created Date
- Closed Date
- Agency
- Complaint Type
- Descriptor
- Borough
- Status
- Latitude
- Longitude

### ⚙️ Project Workflow

1. **Data Collection:** Obtained NYC 311 service request data.
2. **Data Cleaning:** Removed duplicate request IDs, handled missing values, and converted date columns.
3. **Database Management:** Imported cleaned records into MySQL.
4. **SQL Analysis:** Performed complaint distribution, agency workload, and resolution-time analysis.
5. **Python Analysis:** Used Pandas for calculations and Plotly for visualizations.
6. **Dashboard Development:** Built an interactive Streamlit dashboard.

### 📈 Dashboard Features
- Key Performance Indicators (KPIs)
- Borough-wise complaint distribution
- Top 10 complaint categories
- Agency-wise complaint distribution
- Agency performance summary
- Top 10 longest-resolved complaints
- Resolution-time analytics
- Delayed complaint analysis
- Interactive NYC complaint location map
- Borough, agency, complaint type, and date-range filters
- Filtered dataset preview and CSV download
- Project objectives and methodology

### 💡 Key Project Insights

| Metric | Result |
|---|---:|
| Total requests | 99,992 |
| Requests with a closed date | 71,583 |
| Requests without a closed date | 28,409 |
| Closure rate | 71.59% |
| Average resolution time | 18.51 hours |
| Median resolution time | 2.62 hours |
| Complaints delayed over 72 hours | 6,820 |
| Delayed complaint percentage | 9.54% |

**Additional findings:**
- Brooklyn recorded the highest complaint volume.
- Illegal Parking was the most reported complaint type.
- NYPD handled the largest number of requests.

*Note: Resolution-time KPIs are calculated using records with valid, non-negative resolution durations. The delayed complaint percentage uses the 71,583 records with a closed date as its denominator.*

### 🚀 How to Run the Project

**1. Clone the repository**

```bash
git clone https://github.com/dharaniharini2003-op/urban-pulse-nyc-311-analytics.git
```

**2. Navigate to the project folder**

```bash
cd urban-pulse-nyc-311-analytics
```

**3. Install the required libraries**

```bash
pip install streamlit pandas numpy plotly
```

**4. Place the dashboard CSV file**

Place `urbanpulse_dashboard_data.csv` in the same folder as `app.py`.

**5. Run the Streamlit application**

```bash
streamlit run app.py
```

### 📁 Project Structure

```text
urban-pulse-nyc-311-analytics/
│
├── app.py
├── urbanpulse_dashboard_data.csv
├── README.md
└── requirements.txt
```

### 🔮 Future Enhancements
- Deploy the dashboard online.
- Add advanced complaint trend analysis.
- Improve agency performance comparisons.
- Add predictive analytics for complaint resolution.
- Integrate regularly updated NYC 311 data.

### 👩‍💻 Author
**Dharani Bommi K**

M.Sc. Microbiology 

### ⭐ Acknowledgement
Dataset: NYC 311 Service Requests.

## 📸 Dashboard Preview

![URBAN PULSE Dashboard](urban-pulse-dashboard.png)

Developed as a data analytics portfolio project using Python, MySQL, and Streamlit.
