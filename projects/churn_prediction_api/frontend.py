import streamlit as st
import requests

st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction")
st.markdown("Predict whether a customer is likely to churn.")

st.divider()

# =========================
# CUSTOMER INFORMATION
# =========================

col1, col2 = st.columns(2)

with col1:

    Gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    Senior_Citizen = st.selectbox(
        "Senior Citizen",
        ["Yes", "No"]
    )

    Partner = st.selectbox(
        "Partner",
        ["Yes", "No"]
    )

    Dependents = st.selectbox(
        "Dependents",
        ["Yes", "No"]
    )

    Tenure_Months = st.number_input(
        "Tenure Months",
        min_value=0,
        value=1
    )

    Phone_Service = st.selectbox(
        "Phone Service",
        ["Yes", "No"]
    )

    Multiple_Lines = st.selectbox(
        "Multiple Lines",
        ["Yes", "No", "No phone service"]
    )

    Internet_Service = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )

with col2:

    Online_Security = st.selectbox(
        "Online Security",
        ["Yes", "No", "No internet service"]
    )

    Online_Backup = st.selectbox(
        "Online Backup",
        ["Yes", "No", "No internet service"]
    )

    Device_Protection = st.selectbox(
        "Device Protection",
        ["Yes", "No", "No internet service"]
    )

    Tech_Support = st.selectbox(
        "Tech Support",
        ["Yes", "No", "No internet service"]
    )

    Streaming_TV = st.selectbox(
        "Streaming TV",
        ["Yes", "No", "No internet service"]
    )

    Streaming_Movies = st.selectbox(
        "Streaming Movies",
        ["Yes", "No", "No internet service"]
    )

    Contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

    Paperless_Billing = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

Payment_Method = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

Monthly_Charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=50.0
)

Total_Charges = Tenure_Months * Monthly_Charges

st.info(f"Calculated Total Charges: {Total_Charges:.2f}")

st.divider()

if st.button("Predict Churn"):

    data = {
        "Gender": Gender,
        "Senior_Citizen": Senior_Citizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "Tenure_Months": Tenure_Months,
        "Phone_Service": Phone_Service,
        "Multiple_Lines": Multiple_Lines,
        "Internet_Service": Internet_Service,
        "Online_Security": Online_Security,
        "Online_Backup": Online_Backup,
        "Device_Protection": Device_Protection,
        "Tech_Support": Tech_Support,
        "Streaming_TV": Streaming_TV,
        "Streaming_Movies": Streaming_Movies,
        "Contract": Contract,
        "Paperless_Billing": Paperless_Billing,
        "Payment_Method": Payment_Method,
        "Monthly_Charges": Monthly_Charges
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        if response.status_code == 200:

            result = response.json()

            st.success("Prediction completed.")

            st.subheader("Prediction Result")

            st.json(result)

        else:
            st.error(f"API Error: {response.status_code}")
            st.write(response.text)

    except Exception as e:
        st.error(f"Connection Error: {e}")