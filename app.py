import streamlit as st

st.title("🌊 Water Risk Estimator")

st.write("Select Area Type")

area = st.selectbox(
    "Area Type",
    ["Rural", "Semi-Urban", "Urban", "Industrial"]
)

risk_score = 0

# Base risk
if area == "Rural":
    risk_score += 2
elif area == "Semi-Urban":
    risk_score += 3
elif area == "Urban":
    risk_score += 4
elif area == "Industrial":
    risk_score += 5

st.write("### Additional Factors")

fertilizers = st.checkbox("Fertilizers / Pesticides Present")
if fertilizers:
    risk_score += 2

sewage = st.checkbox("Untreated Sewage Present")
if sewage:
    risk_score += 3

industrial_waste = st.checkbox("Industrial Chemical Discharge")
if industrial_waste:
    risk_score += 4

if st.button("Calculate Risk"):

    st.write("## Result")

    if risk_score <= 4:
        st.success("🟢 Low Water Contamination Risk")
    elif risk_score <= 8:
        st.warning("🟡 Moderate Water Contamination Risk")
    else:
        st.error("🔴 High Water Contamination Risk")

    st.write(f"Total Risk Score: {risk_score}")
