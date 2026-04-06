import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Building Energy Forecasting App", layout="wide")

# -------------------------
# Load data
# -------------------------
df = pd.read_excel("ENB2012_data.xlsx")

df.columns = [
    "relative_compactness",
    "surface_area",
    "wall_area",
    "roof_area",
    "overall_height",
    "orientation",
    "glazing_area",
    "glazing_area_distribution",
    "heating_load",
    "cooling_load"
]

X = df.drop(["heating_load", "cooling_load"], axis=1)
y = df["heating_load"]

# Train model
reg_model = LinearRegression()
reg_model.fit(X, y)

COST_PER_UNIT = 0.12

# -------------------------
# Helper functions
# -------------------------
def predict_energy(input_data: pd.DataFrame):
    prediction = reg_model.predict(input_data)[0]
    cost = prediction * COST_PER_UNIT
    return prediction, cost

def explain_energy_final(energy, cost, savings_pct, glazing_area, overall_height):
    if abs(savings_pct) < 0.1:
        savings_pct = 0.0

    text = (
        f"The building is expected to require {energy:.2f} units of heating energy, "
        f"with an estimated heating cost of ${cost:.2f}. "
    )

    if savings_pct > 0:
        text += (
            f"This scenario suggests a potential cost reduction of {savings_pct:.1f}%, "
            f"indicating an opportunity to improve efficiency. "
        )
    else:
        text += (
            "This scenario does not show a meaningful cost reduction compared with the baseline. "
        )

    if glazing_area > 0.3:
        text += "Higher glazing area may be increasing heat transfer and energy demand. "

    if overall_height > 6:
        text += "Greater building height may also be contributing to higher heating requirements. "

    text += "This analysis can help compare design choices and support cost-aware building decisions."
    return text

# -------------------------
# UI
# -------------------------
st.title("Building Energy Forecasting & Cost Analysis")
st.write(
    "Predict building heating load, estimate energy cost, and compare design scenarios."
)

st.sidebar.header("Building Features")

relative_compactness = st.sidebar.slider("Relative Compactness", 0.62, 0.98, 0.75)
surface_area = st.sidebar.slider("Surface Area", 514.5, 808.5, 673.75)
wall_area = st.sidebar.slider("Wall Area", 245.0, 416.5, 318.5)
roof_area = st.sidebar.slider("Roof Area", 110.25, 220.5, 183.75)
overall_height = st.sidebar.slider("Overall Height", 3.5, 7.0, 5.25)
orientation = st.sidebar.slider("Orientation", 2, 5, 3)
glazing_area = st.sidebar.slider("Glazing Area", 0.0, 0.4, 0.25)
glazing_area_distribution = st.sidebar.slider("Glazing Area Distribution", 0, 5, 3)

input_df = pd.DataFrame([{
    "relative_compactness": relative_compactness,
    "surface_area": surface_area,
    "wall_area": wall_area,
    "roof_area": roof_area,
    "overall_height": overall_height,
    "orientation": orientation,
    "glazing_area": glazing_area,
    "glazing_area_distribution": glazing_area_distribution
}])

energy, cost = predict_energy(input_df)

# Baseline scenario from first row
baseline_df = pd.DataFrame([X.iloc[0]])
baseline_energy, baseline_cost = predict_energy(baseline_df)

savings = baseline_cost - cost
savings_pct = (savings / baseline_cost) * 100 if baseline_cost != 0 else 0.0

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Predicted Heating Load", f"{energy:.2f}")

with col2:
    st.metric("Estimated Heating Cost", f"${cost:.2f}")

with col3:
    st.metric("Savings vs Baseline", f"{savings_pct:.1f}%")

st.subheader("Scenario Comparison")

comparison_df = pd.DataFrame({
    "Scenario": ["Baseline", "Current Input"],
    "Heating Load": [round(baseline_energy, 2), round(energy, 2)],
    "Estimated Cost": [round(baseline_cost, 2), round(cost, 2)]
})

st.dataframe(comparison_df, use_container_width=True)

st.subheader("Business Insight")

final_explanation = explain_energy_final(
    energy,
    cost,
    savings_pct,
    glazing_area,
    overall_height
)

st.write(final_explanation)

st.subheader("Input Summary")
st.dataframe(input_df, use_container_width=True)