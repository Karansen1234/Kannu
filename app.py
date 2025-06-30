import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Employee Attrition Dashboard", layout="wide")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("EA.csv")

df = load_data()

# Sidebar filters
st.sidebar.title("Filters")
department = st.sidebar.multiselect("Select Department", options=df["Department"].unique(), default=df["Department"].unique())
education_field = st.sidebar.multiselect("Select Education Field", options=df["EducationField"].unique(), default=df["EducationField"].unique())
gender = st.sidebar.multiselect("Select Gender", options=df["Gender"].unique(), default=df["Gender"].unique())

filtered_df = df[
    (df["Department"].isin(department)) &
    (df["EducationField"].isin(education_field)) &
    (df["Gender"].isin(gender))
]

# Dashboard Title
st.title("📊 Employee Attrition Dashboard")
st.markdown("This dashboard provides HR and leadership teams with deep insights into employee attrition using demographic, performance, and satisfaction metrics.")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["👥 Overview", "🏢 Department View", "📚 Education & Age", "💼 Work & Satisfaction", "📈 Prediction Insight"])

with tab1:
    st.subheader("1. Attrition Distribution")
    st.markdown("This chart shows the overall distribution of employees who have left vs stayed.")
    attr_pie = px.pie(df, names='Attrition', title='Overall Attrition Split')
    st.plotly_chart(attr_pie, use_container_width=True)

    st.subheader("2. Gender Distribution")
    st.markdown("Visualizes employee gender distribution.")
    gender_chart = px.histogram(filtered_df, x='Gender', color='Attrition', barmode='group')
    st.plotly_chart(gender_chart, use_container_width=True)

    st.subheader("3. Marital Status & Attrition")
    st.markdown("Evaluates how marital status may relate to attrition.")
    marital_chart = px.histogram(filtered_df, x='MaritalStatus', color='Attrition', barmode='group')
    st.plotly_chart(marital_chart, use_container_width=True)

with tab2:
    st.subheader("4. Department-wise Attrition")
    st.markdown("Compares attrition rate across departments.")
    dept_chart = px.histogram(filtered_df, x='Department', color='Attrition', barmode='group')
    st.plotly_chart(dept_chart, use_container_width=True)

    st.subheader("5. Job Role vs Attrition")
    st.markdown("Identifies roles with higher attrition.")
    job_chart = px.histogram(filtered_df, x='JobRole', color='Attrition', barmode='group')
    st.plotly_chart(job_chart, use_container_width=True)

    st.subheader("6. Business Travel & Attrition")
    travel_chart = px.histogram(filtered_df, x='BusinessTravel', color='Attrition', barmode='group')
    st.markdown("Does frequent travel impact attrition? Let's see.")
    st.plotly_chart(travel_chart, use_container_width=True)

with tab3:
    st.subheader("7. Age vs Attrition")
    st.markdown("This visual shows how attrition trends with age.")
    age_chart = px.histogram(filtered_df, x='Age', color='Attrition')
    st.plotly_chart(age_chart, use_container_width=True)

    st.subheader("8. Education Field & Attrition")
    edu_chart = px.histogram(filtered_df, x='EducationField', color='Attrition', barmode='group')
    st.plotly_chart(edu_chart, use_container_width=True)

    st.subheader("9. Distance from Home")
    dist_chart = px.box(filtered_df, x='Attrition', y='DistanceFromHome', color='Attrition')
    st.markdown("Longer commutes may affect retention.")
    st.plotly_chart(dist_chart, use_container_width=True)

with tab4:
    st.subheader("10. Monthly Income & Attrition")
    income_chart = px.violin(filtered_df, y='MonthlyIncome', x='Attrition', box=True, color='Attrition')
    st.plotly_chart(income_chart, use_container_width=True)

    st.subheader("11. Job Satisfaction Levels")
    sat_chart = px.histogram(filtered_df, x='JobSatisfaction', color='Attrition', barmode='group')
    st.plotly_chart(sat_chart, use_container_width=True)

    st.subheader("12. Years at Company")
    st.markdown("Examines tenure vs attrition.")
    years_chart = px.box(filtered_df, x='Attrition', y='YearsAtCompany', color='Attrition')
    st.plotly_chart(years_chart, use_container_width=True)

    st.subheader("13. Training Times Last Year")
    train_chart = px.histogram(filtered_df, x='TrainingTimesLastYear', color='Attrition', barmode='group')
    st.plotly_chart(train_chart, use_container_width=True)

    st.subheader("14. Work-Life Balance")
    wl_chart = px.histogram(filtered_df, x='WorkLifeBalance', color='Attrition', barmode='group')
    st.plotly_chart(wl_chart, use_container_width=True)

    st.subheader("15. Relationship Satisfaction")
    rs_chart = px.histogram(filtered_df, x='RelationshipSatisfaction', color='Attrition', barmode='group')
    st.plotly_chart(rs_chart, use_container_width=True)

with tab5:
    st.subheader("16. Heatmap: Correlation with Attrition")
    st.markdown("Numerical features correlated with Attrition (Yes=1, No=0).")
    df_num = df.copy()
    df_num['Attrition'] = df_num['Attrition'].map({'Yes':1, 'No':0})
    corr = df_num.corr(numeric_only=True)
    fig, ax = plt.subplots()
    sns.heatmap(corr[['Attrition']].sort_values(by='Attrition', ascending=False), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    st.subheader("17. Attrition by Overtime")
    ot_chart = px.histogram(filtered_df, x='OverTime', color='Attrition', barmode='group')
    st.plotly_chart(ot_chart, use_container_width=True)

    st.subheader("18. Years Since Last Promotion")
    promo_chart = px.box(filtered_df, x='Attrition', y='YearsSinceLastPromotion', color='Attrition')
    st.plotly_chart(promo_chart, use_container_width=True)

    st.subheader("19. Attrition by Stock Option Level")
    stock_chart = px.histogram(filtered_df, x='StockOptionLevel', color='Attrition', barmode='group')
    st.plotly_chart(stock_chart, use_container_width=True)

    st.subheader("20. Performance Rating")
    perf_chart = px.histogram(filtered_df, x='PerformanceRating', color='Attrition', barmode='group')
    st.plotly_chart(perf_chart, use_container_width=True)

# End of dashboard
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit | MBA Dashboard for HR Decision-Making")
