import streamlit as st

st.set_page_config(page_title="HR AI Suite", layout="wide")

# ---------------------------
# MODEL LINKS
# ---------------------------
links = {
    "HR Decision Tool": "https://hrdecisiontool.streamlit.app/",
    "HR KPI Prediction": "https://hr-kpi-prediction-model.streamlit.app/",
    "Employee Attrition Prediction": "https://employeeattritionmodel.streamlit.app/",
    "Employee Performance Prediction": "https://employee-performanceprediction.streamlit.app/"
}

# ---------------------------
# SIDEBAR NAVIGATION
# ---------------------------
st.sidebar.title("HR AI SUITE 🧠")
page = st.sidebar.radio(
    "Navigate",
    ["Home", "HR Decision Tool", "HR KPI Prediction", "Attrition Model", "Performance Model"]
)

# ---------------------------
# HOME PAGE
# ---------------------------
if page == "Home":
    st.title("🚀 All-in-One HR AI Dashboard")
    st.write("Welcome to your centralized HR Machine Learning suite.")

    st.subheader("Available Models")

    for name, url in links.items():
        st.markdown(f"### 🔹 {name}")
        st.write(url)
        st.link_button(f"Open {name}", url)

    st.info("Use the sidebar to switch between models quickly.")

# ---------------------------
# MODEL PAGES
# ---------------------------
elif page == "HR Decision Tool":
    st.title("HR Decision Tool 🧑‍💼")
    st.components.v1.iframe(links["HR Decision Tool"], height=800)

elif page == "HR KPI Prediction":
    st.title("HR KPI Prediction 📊")
    st.components.v1.iframe(links["HR KPI Prediction"], height=800)

elif page == "Attrition Model":
    st.title("Employee Attrition Prediction 📉")
    st.components.v1.iframe(links["Employee Attrition Prediction"], height=800)

elif page == "Performance Model":
    st.title("Employee Performance Prediction 📈")
    st.components.v1.iframe(links["Employee Performance Prediction"], height=800)
