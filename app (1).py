import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Witness Archive Dashboard",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv("data/witness_archive_dataset.csv")
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str)
            df[col] = df[col].str.replace('[\u201c\u201d]', '"', regex=True)
            df[col] = df[col].str.replace('[\u2018\u2019]', "'", regex=True)
    return df

df = load_data()

st.title("📘 Witness Archive: Narratives Dashboard")

if "Source" in df.columns:
    sources = sorted(df["Source"].dropna().unique())
    selected_sources = st.multiselect("Filter by Source", sources)
    if selected_sources:
        df = df[df["Source"].isin(selected_sources)]

st.write(f"### Total Records: {len(df)}")

st.dataframe(df, use_container_width=True)
