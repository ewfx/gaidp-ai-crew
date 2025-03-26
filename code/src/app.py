import streamlit as st
import pandas as pd
from kb_search import search_kb, load_kb
from log_analysis import load_logs, detect_anomalies
from observability_graph import plot_observability_graph

# Streamlit App Styling
st.set_page_config(page_title="Integrated Platform", page_icon="⚙️", layout="wide")

# Custom Header
st.markdown("""
    <h1 style="text-align: center; color: #4A90E2;">🔗 Integrated Platform Environment</h1>
    <hr style="border: 1px solid #4A90E2;">
""", unsafe_allow_html=True)

# Step 1: Knowledge Base Search
with st.container():
    st.subheader("📚 Knowledge Base Search")
    st.markdown("🔍 **Search through the knowledge base to find relevant solutions.**")

    query = st.text_input("Enter your query:")
    
    col1, col2 = st.columns([1, 5])  # Button alignment
    with col1:
        if st.button("🔎 Search KB"):
            with st.spinner("Searching..."):
                results = search_kb(query)
                if results:
                    st.success("✅ Results Found!")
                    st.write(results)
                else:
                    st.warning("❌ No relevant results found.")

# Step 2: Log Analysis & Anomaly Detection
with st.expander("🔍 Log Analysis & Anomaly Detection", expanded=True):
    st.markdown("Analyze logs and detect potential anomalies.")

    if st.button("📂 Load & Analyze Logs"):
        with st.spinner("Processing logs..."):
            df = load_logs()
            df["anomaly"] = detect_anomalies(df["text"])
            st.success("✅ Logs Analyzed!")
            st.dataframe(df.head())

# Step 3: Observability Dashboard
with st.expander("📊 Observability Dashboard", expanded=True):
    st.markdown("View system observability insights and log trends.")

    if st.button("📈 Show Log Trends"):
        with st.spinner("Generating graph..."):
            st.plotly_chart(plot_observability_graph(df), use_container_width=True)

# Footer
st.markdown("""
    <hr>
    <p style="text-align:center;">🚀 Powered by <strong>Gen-AI & Platform Intelligence</strong></p>
""", unsafe_allow_html=True)
