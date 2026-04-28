import streamlit as st

st.set_page_config(page_title="HR AI Suite", layout="wide")

# -----------------------
# CUSTOM CSS (UI UPGRADE)
# -----------------------
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
        color: white;
    }

    .title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(90deg, #4f46e5, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .card {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
        margin-bottom: 20px;
    }

    .card h3 {
        color: #38bdf8;
    }

    .card p {
        color: #cbd5e1;
    }

    .stButton > button {
        background: linear-gradient(90deg, #4f46e5, #06b6d4);
        color: white;
        border-radius: 10px;
        height: 45px;
        width: 100%;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------
# MODEL LINKS
# -----------------------
links = {
    "HR Decision Tool": "https://hrdecisiontool.streamlit.app/",
    "HR KPI Prediction": "https://hr-kpi-prediction-model.streamlit.app/",
    "Employee Attrition": "https://employeeattritionmodel.streamlit.app/",
    "Performance Prediction": "https://employee-performanceprediction.streamlit.app/",
    "HR Payroll Calculator": "https://hrpayrollapp.streamlit.app/"
}

# -----------------------
# HEADER
# -----------------------
st.markdown('<div class="title">🚀 HR AI SUITE</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">All-in-One Intelligent HR Analytics Platform</div>', unsafe_allow_html=True)

# -----------------------
# SIDEBAR
# -----------------------
page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "🧑‍💼 HR Decision", "📊 KPI Model", "📉 Attrition", "📈 Performance", "👥HR Payroll Calculator"]
)

# -----------------------
# HOME PAGE (DASHBOARD UI)
# -----------------------
if page == "🏠 Home":

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
            <h3>🧑‍💼 HR Decision Tool</h3>
            <p>Smart hiring decisions powered by AI classification model.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Open Tool", links["HR Decision Tool"])

        st.markdown("""
        <div class="card">
            <h3>📊 HR KPI Prediction</h3>
            <p>Predict employee performance KPIs using machine learning.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Open KPI Model", links["HR KPI Prediction"])

    with col2:
        st.markdown("""
        <div class="card">
            <h3>📉 Employee Attrition</h3>
            <p>Predict employees likely to leave the company.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Open Attrition Model", links["Employee Attrition"])

        st.markdown("""
        <div class="card">
            <h3>📈 Performance Prediction</h3>
            <p>Forecast employee productivity and performance score.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("Open Performance Model", links["Performance Prediction"])

        st.markdown("""
        <div class="card">
            <h3>📈 HR Payroll Calculator</h3>
            <p>HR payroll calculator.</p>
        </div>
        """, unsafe_allow_html=True)
        st.link_button("HR Payroll Calculator", links["HR Payroll Calculator"])

# -----------------------
# INDIVIDUAL PAGES
# -----------------------
elif page == "🧑‍💼 HR Decision":
    st.title("HR Decision Tool")
    st.components.v1.iframe(links["HR Decision Tool"], height=800)

elif page == "📊 KPI Model":
    st.title("HR KPI Prediction")
    st.components.v1.iframe(links["HR KPI Prediction"], height=800)

elif page == "📉 Attrition":
    st.title("Employee Attrition Prediction")
    st.components.v1.iframe(links["Employee Attrition"], height=800)

elif page == "📈 Performance":
    st.title("Employee Performance Prediction")
    st.components.v1.iframe(links["Performance Prediction"], height=800)

elif page == "📈 HR Payroll Calculator":
    st.title("HR Payroll Calculator")
    st.components.v1.iframe(links["HR Payroll Calculator"], height=800)
