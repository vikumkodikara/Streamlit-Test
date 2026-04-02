import numpy as np
import pandas as pd
import streamlit as st

st.title("Data Display and Visualisation")

st.header("DataFrames and Tables")
df = pd.DataFrame(
    {
        "Patient_ID": range(1, 6),
        "Age": [34, 45, 56, 29, 67],
        "Diagnosis": ["Positive", "Negative", "Positive", "Negative", "Positive"],
        "Confidence": [0.92, 0.87, 0.95, 0.73, 0.89],
    }
)

st.dataframe(
    df,
    use_container_width=True,
    column_config={
        "Patient_ID": st.column_config.NumberColumn("ID"),
        "Confidence": st.column_config.ProgressColumn("Confidence", min_value=0, max_value=1, format="%.2f"),
        "Diagnosis": st.column_config.SelectboxColumn("Diagnosis", options=["Positive", "Negative"]),
    },
)
st.table(df.head(3))

st.header("Native Charts")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Model A", "Model B", "Baseline"])
st.line_chart(chart_data)
feat_imp = pd.DataFrame({"importance": [0.35, 0.28, 0.19, 0.11, 0.07]}, index=["income", "age", "score", "region", "edu"])
st.bar_chart(feat_imp)
st.area_chart(chart_data)
st.scatter_chart(chart_data, x="Model A", y="Model B")

st.header("Matplotlib / Seaborn")
try:
    import matplotlib.pyplot as plt
    import seaborn as sns

    cm = np.array([[85, 5], [8, 102]])
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["Pred Neg", "Pred Pos"],
        yticklabels=["True Neg", "True Pos"],
        ax=ax,
    )
    ax.set_title("Confusion Matrix")
    st.pyplot(fig)
    plt.close(fig)
except Exception as exc:
    st.warning(f"Matplotlib/Seaborn section skipped: {exc}")

st.header("Plotly")
try:
    import plotly.express as px
    import plotly.graph_objects as go

    iris = px.data.iris()
    fig = px.scatter(
        iris,
        x="sepal_width",
        y="sepal_length",
        color="species",
        size="petal_length",
        title="Iris Dataset - Feature Correlation",
    )
    st.plotly_chart(fig, use_container_width=True)

    models = ["Logistic Reg", "Random Forest", "SVM", "XGBoost"]
    scores = [0.87, 0.94, 0.91, 0.96]
    fig2 = go.Figure(
        go.Bar(
            x=models,
            y=scores,
            marker_color=["#636EFA", "#EF553B", "#00CC96", "#AB63FA"],
            text=[f"{s:.0%}" for s in scores],
            textposition="outside",
        )
    )
    fig2.update_layout(title="Model Accuracy Comparison", yaxis_range=[0.8, 1.0])
    st.plotly_chart(fig2, use_container_width=True)
except Exception as exc:
    st.warning(f"Plotly section skipped: {exc}")
