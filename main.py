import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Sales Analysis Dashboard", layout="wide")

st.title("Sales Data Analysis Dashboard")

file_path = "data/sales_data.csv"
df = pd.read_csv(file_path)

df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df = df.drop_duplicates()

df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df = df.dropna(subset=["sales"])

total_sales = df["sales"].sum()
total_orders = df["order_id"].nunique() if "order_id" in df.columns else len(df)
average_order_value = total_sales / total_orders if total_orders else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"{total_sales:,.2f}")
col2.metric("Total Orders", f"{total_orders}")
col3.metric("Average Order Value", f"{average_order_value:,.2f}")

st.subheader("Top 10 Products by Sales")
top_products = df.groupby("product_name")["sales"].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_products)

st.subheader("Top 10 Customers by Sales")
top_customers = df.groupby("customer_name")["sales"].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_customers)

st.subheader("Monthly Sales Trend")
df["month"] = df["order_date"].dt.to_period("M").astype(str)
monthly_sales = df.groupby("month")["sales"].sum().reset_index()
monthly_sales = monthly_sales.sort_values("month")
st.line_chart(monthly_sales.set_index("month")["sales"])

st.subheader("Raw Data")
st.dataframe(df)