import plotly.express as px
import streamlit as st

def plot_observability_graph(df):
    df["error_count"] = df["anomaly"].apply(lambda x: 1 if x == "Anomaly" else 0)
    
    # Aggregate anomalies per time window
    trend_data = df.resample("1H", on="timestamp").sum()

    # Plot the trend
    fig = px.line(trend_data, x=trend_data.index, y="error_count", title="📊 Log Anomaly Trend")

    # Highlight anomaly points
    anomalies = df[df["anomaly"] == "Anomaly"]
    fig.add_scatter(x=anomalies["timestamp"], y=[1] * len(anomalies), mode="markers",
                    marker=dict(color="red", size=8), name="Anomalies")

    return fig
