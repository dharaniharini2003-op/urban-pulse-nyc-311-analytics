
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="URBAN PULSE",
    page_icon="🏙️",
    layout="wide"
)
# =====================================
# CUSTOM DASHBOARD STYLING
# =====================================

st.markdown("""
<style>
.stApp {
    background-color: #F5F7FA;
}

h1 {
    color: #17365D !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: #24476B !important;
}

[data-testid="stMetric"] {
    background-color: white !important;
    padding: 20px !important;
    border-radius: 12px !important;
    border: 1px solid #DCE3EB !important;
}

[data-testid="stSidebar"] {
    background-color: #EAF0F7 !important;
}
</style>
""", unsafe_allow_html=True)
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "urbanpulse_dashboard_data.csv"

# =====================================
# LOAD DATASET
# =====================================

@st.cache_data
def load_data():
    df = pd.read_csv(CSV_PATH)

    df["created_date"] = pd.to_datetime(
        df["created_date"], errors="coerce"
    )

    df["closed_date"] = pd.to_datetime(
        df["closed_date"], errors="coerce"
    )

    df["resolution_hours"] = (
        df["closed_date"] - df["created_date"]
    ).dt.total_seconds() / 3600

    return df


df = load_data()
# =====================================
# DASHBOARD HEADING
# =====================================

st.title("🏙️ URBAN PULSE")
# =====================================
# PROJECT OBJECTIVES
# =====================================

with st.expander("🎯 Project Objectives"):

    st.markdown("""
    - Analyze NYC 311 service request patterns.
    - Identify boroughs with the highest complaint volume.
    - Determine the most frequently reported complaint types.
    - Evaluate agency-wise complaint handling.
    - Analyze complaint resolution time.
    - Identify delayed and long-pending complaints.
    - Visualize complaint locations across NYC.
    - Support data-driven insights for public service improvement.
    """)
# =====================================
# PROJECT METHODOLOGY
# =====================================

with st.expander("📌 Project Methodology – How It Works"):

    st.markdown("""
    **1. Data Collection**
    - Collected NYC 311 service request data.

    **2. Data Cleaning**
    - Removed duplicate request IDs.
    - Handled missing values.
    - Converted date columns into datetime format.

    **3. Database Management**
    - Stored cleaned records in MySQL.
    - Performed SQL queries for complaint analysis.

    **4. Data Analysis**
    - Used Python, Pandas and Plotly.
    - Analyzed complaint categories, boroughs and agencies.
    - Calculated complaint resolution times.

    **5. Interactive Visualization**
    - Developed a Streamlit dashboard.
    - Added filters, KPIs, charts and a complaint location map.
    """)

st.subheader(
    "NYC 311 Complaint Intelligence & Resolution Analytics"
)

st.markdown("---")
# =====================================
# PROJECT INSIGHTS
# =====================================

st.header("💡 Key Project Insights")

top_borough = df["borough"].mode()[0]
top_complaint = df["complaint_type"].mode()[0]
top_agency = df["agency"].mode()[0]

st.write(f"📍 Highest complaint volume: {top_borough}")
st.write(f"📢 Most reported complaint: {top_complaint}")
st.write(f"🏢 Agency handling most requests: {top_agency}")

insight_valid_df = df[
    df["resolution_hours"].notna()
    & (df["resolution_hours"] >= 0)
]

insight_average = insight_valid_df["resolution_hours"].mean()

st.write(
    f"⏱️ Average complaint resolution time: "
    f"{insight_average:.2f} hours"
)
st.write(
    f"🚨 Complaints taking more than 72 hours: "
    f"{len(df[df['resolution_hours'] > 72]):,}"
)

st.success("Dataset loaded successfully!")
# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("🏙️ URBAN PULSE")

st.sidebar.markdown("---")

st.sidebar.subheader("Project Overview")

st.sidebar.write(
    "NYC 311 Complaint Intelligence "
    "and Resolution Analytics"
)

st.sidebar.markdown("---")

st.sidebar.subheader("Dataset Information")

st.sidebar.write("Dataset: NYC 311 Service Requests")
st.sidebar.write(f"Total Records: {len(df):,}")
st.sidebar.write("Original Dataset Columns: 10")
st.sidebar.write("Calculated Columns: 1")

st.sidebar.markdown("---")

st.sidebar.caption(
    "Developed using Python, Streamlit, "
    "Pandas, Plotly and MySQL"
)

# =====================================
# KEY PERFORMANCE INDICATORS
# =====================================

st.header("📊 Key Performance Indicators")

total_requests = len(df)

closed_requests = df["closed_date"].notna().sum()

open_requests = df["closed_date"].isna().sum()

closure_rate = (
    closed_requests / total_requests * 100
    if total_requests > 0 else 0
)

valid_resolution = df[
    df["resolution_hours"].notna()
    & (df["resolution_hours"] >= 0)
]

average_resolution = valid_resolution[
    "resolution_hours"
].mean()

median_resolution = valid_resolution[
    "resolution_hours"
].median()

col1, col2, col3 = st.columns(3)

col1.metric("Total Requests", f"{total_requests:,}")
col2.metric("Closed Requests", f"{closed_requests:,}")
col3.metric("Open Requests", f"{open_requests:,}")

col4, col5, col6 = st.columns(3)

col4.metric("Closure Rate", f"{closure_rate:.2f}%")
col5.metric("Average Resolution", f"{average_resolution:.2f} hrs")
col6.metric("Median Resolution", f"{median_resolution:.2f} hrs")

st.markdown("---")

# =====================================
# INTERACTIVE FILTERS
# =====================================

st.header("🔎 Complaint Data Filters")

col1, col2, col3 = st.columns(3)

with col1:
    selected_borough = st.selectbox(
        "Select Borough",
        ["All"] + sorted(df["borough"].dropna().unique().tolist())
    )

with col2:
    selected_agency = st.selectbox(
        "Select Agency",
        ["All"] + sorted(df["agency"].dropna().unique().tolist())
    )

with col3:
    selected_complaint = st.selectbox(
        "Select Complaint Type",
        ["All"] + sorted(df["complaint_type"].dropna().unique().tolist())
    )
# DATE RANGE FILTER

st.sidebar.markdown("---")
st.sidebar.subheader("📅 Date Range")

start_date = df["created_date"].min().date()
end_date = df["created_date"].max().date()

selected_dates = st.sidebar.date_input(
    "Select complaint date range",
    value=(start_date, end_date),
    min_value=start_date,
    max_value=end_date
)
# Apply selected filters

filtered_df = df.copy()
# Apply date range filter

if isinstance(selected_dates, (tuple, list)) and len(selected_dates) == 2:

    start_selected, end_selected = selected_dates

    filtered_df = filtered_df[
        filtered_df["created_date"].dt.date.between(
            start_selected,
            end_selected
        )
    ]

if selected_borough != "All":
    filtered_df = filtered_df[
        filtered_df["borough"] == selected_borough
    ]

if selected_agency != "All":
    filtered_df = filtered_df[
        filtered_df["agency"] == selected_agency
    ]

if selected_complaint != "All":
    filtered_df = filtered_df[
        filtered_df["complaint_type"] == selected_complaint
    ]

st.write("Filtered Records:", f"{len(filtered_df):,}")
csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Data",
    data=csv_data,
    file_name="urbanpulse_filtered_data.csv",
    mime="text/csv"
)

# =====================================
# FILTERED DATASET PREVIEW
# =====================================

st.subheader("📋 Filtered Dataset Preview")

st.dataframe(
    filtered_df.head(10),
    width="stretch"
)
# =====================================
# NYC COMPLAINT LOCATION MAP
# =====================================

st.header("🗺️ NYC Complaint Location Map")

map_df = filtered_df.dropna(
    subset=["latitude", "longitude"]
).copy()

st.write(
    "Complaints with valid location coordinates:",
    f"{len(map_df):,}"
)
# Create interactive complaint map

if not map_df.empty:

    fig_map = px.scatter_map(
        map_df,
        lat="latitude",
        lon="longitude",
        color="borough",
        hover_name="complaint_type",
        hover_data=["agency", "status"],
        zoom=9,
        height=600,
        title="NYC 311 Complaint Locations"
    )

    fig_map.update_layout(
        map_style="open-street-map",
        margin={"r": 0, "t": 50, "l": 0, "b": 0}
    )

    st.plotly_chart(fig_map, width="stretch")

else:
    st.warning("No valid location coordinates available.")
# =====================================
# COMPLAINT ANALYTICS
# =====================================

st.header("📊 Complaint Analytics")

# 1. Borough-wise complaints

st.subheader("1. Borough-wise Complaint Distribution")

borough_data = (
    filtered_df["borough"]
    .fillna("Unspecified")
    .value_counts()
)

fig1 = px.bar(
    x=borough_data.index,
    y=borough_data.values,
    labels={
        "x": "Borough",
        "y": "Number of Complaints"
    },
    title="Complaints by Borough"
)

st.plotly_chart(fig1, width="stretch")

# 2. Top 10 complaint types

st.subheader("2. Top 10 Complaint Types")

complaint_data = (
    filtered_df["complaint_type"]
    .value_counts()
    .head(10)
)

fig2 = px.bar(
    x=complaint_data.values,
    y=complaint_data.index,
    orientation="h",
    labels={
        "x": "Number of Complaints",
        "y": "Complaint Type"
    },
    title="Top 10 Complaint Categories"
)

st.plotly_chart(fig2, width="stretch")

# 3. Agency-wise complaints

st.subheader("3. Agency-wise Complaint Distribution")

agency_data = filtered_df["agency"].value_counts()

fig3 = px.bar(
    x=agency_data.index,
    y=agency_data.values,
    labels={
        "x": "Agency",
        "y": "Number of Complaints"
    },
    title="Complaints Handled by Each Agency"
)

st.plotly_chart(fig3, width="stretch")
# =====================================
# AGENCY PERFORMANCE SUMMARY
# =====================================

st.header("🏢 Agency Performance Summary")

# =====================================
# AGENCY PERFORMANCE SUMMARY
# =====================================

performance_valid_df = filtered_df[
    filtered_df["resolution_hours"].notna()
    & (filtered_df["resolution_hours"] >= 0)
]

performance_df = (
    performance_valid_df.groupby("agency")
    .agg(
        Total_Complaints=("unique_key", "count"),
        Average_Resolution=("resolution_hours", "mean"),
        Median_Resolution=("resolution_hours", "median")
    )
    .reset_index()
    .sort_values(
        by="Average_Resolution",
        ascending=False
    )
)

st.dataframe(
    performance_df.round(2),
    width="stretch"
)
# =====================================
# TOP 10 LONGEST-RESOLVED COMPLAINTS
# =====================================

st.header("🚨 Top 10 Longest-Resolved Complaints")

longest_df = (
    filtered_df[
        filtered_df["resolution_hours"].notna()
        & (filtered_df["resolution_hours"] >= 0)
    ][
        [
            "unique_key",
            "complaint_type",
            "agency",
            "borough",
            "resolution_hours"
        ]
    ]
    .sort_values(
        by="resolution_hours",
        ascending=False
    )
    .head(10)
)

st.dataframe(
    longest_df.round(2),
    width="stretch"
)
# =====================================
# RESOLUTION TIME ANALYSIS
# =====================================

st.header("⏱️ Resolution Time Analytics")

valid_df = filtered_df[
    filtered_df["resolution_hours"].notna()
    & (filtered_df["resolution_hours"] >= 0)
]

agency_resolution = (
    valid_df.groupby("agency")["resolution_hours"]
    .mean()
    .sort_values(ascending=False)
)

fig4 = px.bar(
    x=agency_resolution.index,
    y=agency_resolution.values,
    labels={
        "x": "Agency",
        "y": "Average Resolution Time (Hours)"
    },
    title="Average Resolution Time by Agency"
)

st.plotly_chart(fig4, width="stretch")

# =====================================
# DELAYED COMPLAINT ANALYSIS
# =====================================

st.header("🚨 Delayed Complaint Analysis")

delayed_df = valid_df[
    valid_df["resolution_hours"] > 72
]

delayed_count = len(delayed_df)

total_valid = len(valid_df)

delayed_percentage = (
    delayed_count / total_valid * 100
    if total_valid > 0 else 0
)

col1, col2 = st.columns(2)

col1.metric(
    "Complaints Delayed > 72 Hours",
    f"{delayed_count:,}"
)

col2.metric(
    "Delayed Complaint Percentage",
    f"{delayed_percentage:.2f}%"
)

delayed_agency = delayed_df["agency"].value_counts()

fig5 = px.bar(
    x=delayed_agency.index,
    y=delayed_agency.values,
    labels={
        "x": "Agency",
        "y": "Delayed Complaints"
    },
    title="Delayed Complaints by Agency"
)

st.plotly_chart(fig5, width="stretch")

st.markdown("---")

# =====================================
# PROJECT CONCLUSION
# =====================================

st.header("📝 Project Conclusion")

st.markdown("""
The URBAN PULSE project provides an interactive analytical view of
NYC 311 service requests.

The analysis identified Brooklyn as the borough with the highest
complaint volume, Illegal Parking as the most reported complaint,
and NYPD as the agency handling the largest number of requests.

Resolution-time analysis also highlighted complaints requiring
more than 72 hours for resolution.

The dashboard helps explore complaint patterns, agency workloads,
geographical distribution and resolution delays through interactive
visualizations.
""")

st.markdown("---")

st.caption(
    "URBAN PULSE | NYC 311 Complaint Intelligence & Resolution Analytics | "
    "Developed using Python, Streamlit, Pandas, Plotly and MySQL"
)