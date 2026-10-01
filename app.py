
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="👥",
    layout="wide"
)

st.title("HR Analytics Dashboard")
st.write("Employee Attrition Analysis")


df = pd.read_csv("employee_attrition_cleaned.csv")


total_employees = df.shape[0]

employees_left = (df["Attrition"] == "Yes").sum()

employees_stayed = (df["Attrition"] == "No").sum()

attrition_rate = (employees_left / total_employees) * 100


col1, col2, col3 = st.columns(3)

col1.metric("Total Employees", total_employees)

col2.metric("Employees Left", employees_left)

col3.metric("Attrition Rate", f"{attrition_rate:.2f}%")


st.divider()


# Employee Attrition - Pie Chart
col1, col2 = st.columns(2)

with col1:

    st.subheader("Employee Attrition")

    attrition_counts = df["Attrition"].value_counts()

    fig, ax = plt.subplots(figsize=(6, 4))

    ax.pie(attrition_counts.values,labels=attrition_counts.index,autopct="%1.1f%%",startangle=90)

    ax.set_title("Employee Attrition Distribution")

    st.pyplot(fig)


with col2:

    st.subheader("Attrition Rate by Department")

    total_dept = df.groupby("Department").size()

    attrition_dept = (df[df["Attrition"] == "Yes"].groupby("Department").size())

    department_rate = (attrition_dept / total_dept) * 100

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.barplot(x=department_rate.index,y=department_rate.values,ax=ax)

    ax.set_xlabel("Department")
    ax.set_ylabel("Attrition Rate (%)")

    plt.xticks(rotation=45)

    st.pyplot(fig)


# Job Role and Overtime
col1, col2 = st.columns(2)

with col1:

    st.subheader("Attrition Rate by Job Role")

    total_jobrole = df.groupby("JobRole").size()

    attrition_jobrole = (df[df["Attrition"] == "Yes"].groupby("JobRole").size())

    jobrole_rate = (attrition_jobrole / total_jobrole) * 100

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.barplot(x=jobrole_rate.index,y=jobrole_rate.values, ax=ax)

    ax.set_xlabel("Job Role")
    ax.set_ylabel("Attrition Rate (%)")

    plt.xticks(rotation=45)

    st.pyplot(fig)


with col2:

    st.subheader("Attrition Rate by Overtime")

    total_overtime = df.groupby("OverTime").size()

    attrition_overtime = (df[df["Attrition"] == "Yes"].groupby("OverTime").size())

    overtime_rate = (attrition_overtime / total_overtime) * 100

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.barplot(x=overtime_rate.index,y=overtime_rate.values,ax=ax)

    ax.set_xlabel("OverTime")
    ax.set_ylabel("Attrition Rate (%)")

    st.pyplot(fig)


# Age and Monthly Income - Scatter Plots
col1, col2 = st.columns(2)

with col1:

    st.subheader("Age vs Monthly Income")

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.scatterplot(data=df,x="Age",y="MonthlyIncome",hue="Attrition",ax=ax)

    ax.set_xlabel("Age")
    ax.set_ylabel("Monthly Income")

    st.pyplot(fig)


with col2:

    st.subheader("Age vs Years at Company")

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.scatterplot(data=df,x="Age",y="YearsatCompany",hue="Attrition",ax=ax)

    ax.set_xlabel("Age")
    ax.set_ylabel("Years at Company")

    st.pyplot(fig)


# Job Satisfaction and Years at Company
col1, col2 = st.columns(2)

with col1:

    st.subheader("Average Job Satisfaction vs Attrition")

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.barplot(data=df,x="Attrition",y="JobSatisfaction",ax=ax)

    ax.set_xlabel("Attrition")
    ax.set_ylabel("Average Job Satisfaction")

    st.pyplot(fig)


with col2:

    st.subheader("Average Years at Company vs Attrition")

    years_attrition = (df.groupby("Attrition")["YearsatCompany"].mean().reset_index())

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.lineplot(data=years_attrition,x="Attrition",y="YearsatCompany",marker="o",ax=ax)

    ax.set_xlabel("Attrition")
    ax.set_ylabel("Average Years at Company")

    st.pyplot(fig)


# Job Level and Business Travel
col1, col2 = st.columns(2)

with col1:

    st.subheader("Attrition Rate by Job Level")

    total_joblevel = df.groupby("JobLevel").size()

    attrition_joblevel = (df[df["Attrition"] == "Yes"].groupby("JobLevel").size())

    joblevel_rate = (attrition_joblevel / total_joblevel) * 100

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.barplot(x=joblevel_rate.index,y=joblevel_rate.values,ax=ax)

    ax.set_xlabel("Job Level")
    ax.set_ylabel("Attrition Rate (%)")

    st.pyplot(fig)


with col2:

    st.subheader("Attrition Rate by Business Travel")

    total_travel = df.groupby("BusinessTravel").size()

    attrition_travel = (df[df["Attrition"] == "Yes"].groupby("BusinessTravel").size())

    travel_rate = (attrition_travel / total_travel) * 100

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.barplot(x=travel_rate.index,y=travel_rate.values,ax=ax)

    ax.set_xlabel("Business Travel")
    ax.set_ylabel("Attrition Rate (%)")

    plt.xticks(rotation=20)

    st.pyplot(fig)


st.divider()


st.header("Key Findings")

st.write("• The overall employee attrition rate is 16.17%.")

st.write("• Job Level 1 has the highest attrition rate.")

st.write("• Employees who travel frequently have a higher attrition rate.")

st.write("• Employees who left have lower average job satisfaction.")

st.write("• Employees who left have fewer average years at the company.")

st.write("• Attrition varies across departments, job roles and overtime groups.")


st.header("Conclusion")

st.write(
    "The HR Analytics dashboard helps identify employee attrition "
    "patterns and provides insights into factors associated with "
    "employees leaving the organization."
)
