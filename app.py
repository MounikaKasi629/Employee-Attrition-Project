import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="👥",
    layout="wide"
)

st.title("HR Analytics Dashboard")
st.write("Employee Attrition Analysis")


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv("employee_attrition.csv")


# --------------------------------------------------
# DATA CLEANING
# --------------------------------------------------

df.drop_duplicates(inplace=True)

df.reset_index(drop=True, inplace=True)

df["BusinessTravel"] = df["BusinessTravel"].replace(
    "TravelRarely",
    "Travel_Rarely"
)


# --------------------------------------------------
# MAIN METRICS
# --------------------------------------------------

total_employees = df.shape[0]

employees_left = (df["Attrition"] == "Yes").sum()

employees_stayed = (df["Attrition"] == "No").sum()

attrition_rate = (employees_left / total_employees) * 100


col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Employees",
    total_employees
)

col2.metric(
    "Employees Left",
    employees_left
)

col3.metric(
    "Attrition Rate",
    f"{attrition_rate:.2f}%"
)


st.divider()


# ==================================================
# ROW 1
# ==================================================

col1, col2 = st.columns(2)


# --------------------------------------------------
# ATTRITION OVERVIEW
# --------------------------------------------------

with col1:

    st.subheader("Employee Attrition")

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.countplot(
        data=df,
        x="Attrition",
        ax=ax
    )

    ax.set_xlabel("Attrition")
    ax.set_ylabel("Number of Employees")

    st.pyplot(fig)


# --------------------------------------------------
# DEPARTMENT ATTRITION
# --------------------------------------------------

with col2:

    st.subheader("Attrition Rate by Department")

    total_dept = df.groupby("Department").size()

    attrition_dept = (
        df[df["Attrition"] == "Yes"]
        .groupby("Department")
        .size()
    )

    department_rate = (
        attrition_dept / total_dept
    ) * 100

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.barplot(
        x=department_rate.index,
        y=department_rate.values,
        ax=ax
    )

    ax.set_xlabel("Department")
    ax.set_ylabel("Attrition Rate (%)")

    plt.xticks(rotation=45)

    st.pyplot(fig)


# ==================================================
# ROW 2
# ==================================================

col1, col2 = st.columns(2)


# --------------------------------------------------
# JOB ROLE
# --------------------------------------------------

with col1:

    st.subheader("Attrition Rate by Job Role")

    total_jobrole = df.groupby("JobRole").size()

    attrition_jobrole = (
        df[df["Attrition"] == "Yes"]
        .groupby("JobRole")
        .size()
    )

    jobrole_rate = (
        attrition_jobrole / total_jobrole
    ) * 100

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.barplot(
        x=jobrole_rate.index,
        y=jobrole_rate.values,
        ax=ax
    )

    ax.set_xlabel("Job Role")
    ax.set_ylabel("Attrition Rate (%)")

    plt.xticks(rotation=45)

    st.pyplot(fig)


# --------------------------------------------------
# OVERTIME
# --------------------------------------------------

with col2:

    st.subheader("Attrition Rate by Overtime")

    total_overtime = df.groupby("OverTime").size()

    attrition_overtime = (
        df[df["Attrition"] == "Yes"]
        .groupby("OverTime")
        .size()
    )

    overtime_rate = (
        attrition_overtime / total_overtime
    ) * 100

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.barplot(
        x=overtime_rate.index,
        y=overtime_rate.values,
        ax=ax
    )

    ax.set_xlabel("OverTime")
    ax.set_ylabel("Attrition Rate (%)")

    st.pyplot(fig)


# ==================================================
# ROW 3
# ==================================================

col1, col2 = st.columns(2)


# --------------------------------------------------
# AGE VS ATTRITION
# --------------------------------------------------

with col1:

    st.subheader("Average Age vs Attrition")

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.barplot(
        data=df,
        x="Attrition",
        y="Age",
        ax=ax
    )

    ax.set_xlabel("Attrition")
    ax.set_ylabel("Average Age")

    st.pyplot(fig)


# --------------------------------------------------
# MONTHLY INCOME
# --------------------------------------------------

with col2:

    st.subheader("Average Monthly Income vs Attrition")

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.barplot(
        data=df,
        x="Attrition",
        y="MonthlyIncome",
        ax=ax
    )

    ax.set_xlabel("Attrition")
    ax.set_ylabel("Average Monthly Income")

    st.pyplot(fig)


# ==================================================
# ROW 4
# ==================================================

col1, col2 = st.columns(2)


# --------------------------------------------------
# JOB SATISFACTION
# --------------------------------------------------

with col1:

    st.subheader("Average Job Satisfaction vs Attrition")

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.barplot(
        data=df,
        x="Attrition",
        y="JobSatisfaction",
        ax=ax
    )

    ax.set_xlabel("Attrition")
    ax.set_ylabel("Average Job Satisfaction")

    st.pyplot(fig)


# --------------------------------------------------
# YEARS AT COMPANY
# --------------------------------------------------

with col2:

    st.subheader("Average Years at Company vs Attrition")

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.barplot(
        data=df,
        x="Attrition",
        y="YearsatCompany",
        ax=ax
    )

    ax.set_xlabel("Attrition")
    ax.set_ylabel("Average Years at Company")

    st.pyplot(fig)


# ==================================================
# ROW 5
# ==================================================

col1, col2 = st.columns(2)


# --------------------------------------------------
# JOB LEVEL
# --------------------------------------------------

with col1:

    st.subheader("Attrition Rate by Job Level")

    total_joblevel = df.groupby("JobLevel").size()

    attrition_joblevel = (
        df[df["Attrition"] == "Yes"]
        .groupby("JobLevel")
        .size()
    )

    joblevel_rate = (
        attrition_joblevel / total_joblevel
    ) * 100

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.barplot(
        x=joblevel_rate.index,
        y=joblevel_rate.values,
        ax=ax
    )

    ax.set_xlabel("Job Level")
    ax.set_ylabel("Attrition Rate (%)")

    st.pyplot(fig)


# --------------------------------------------------
# BUSINESS TRAVEL
# --------------------------------------------------

with col2:

    st.subheader("Attrition Rate by Business Travel")

    total_travel = df.groupby("BusinessTravel").size()

    attrition_travel = (
        df[df["Attrition"] == "Yes"]
        .groupby("BusinessTravel")
        .size()
    )

    travel_rate = (
        attrition_travel / total_travel
    ) * 100

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.barplot(
        x=travel_rate.index,
        y=travel_rate.values,
        ax=ax
    )

    ax.set_xlabel("Business Travel")
    ax.set_ylabel("Attrition Rate (%)")

    plt.xticks(rotation=20)

    st.pyplot(fig)


# ==================================================
# KEY FINDINGS
# ==================================================

st.divider()

st.header("Key Findings")

st.write(
    "• The overall employee attrition rate is 16.17%."
)

st.write(
    "• Job Level 1 has the highest attrition rate."
)

st.write(
    "• Employees who travel frequently have a higher attrition rate."
)

st.write(
    "• Employees who left have lower average job satisfaction."
)

st.write(
    "• Employees who left have fewer average years at the company."
)

st.write(
    "• Attrition varies across departments, job roles and overtime groups."
)


# ==================================================
# CONCLUSION
# ==================================================

st.header("Conclusion")

st.write(
    "The HR Analytics dashboard helps identify employee attrition "
    "patterns and provides insights into factors associated with "
    "employees leaving the organization."
)