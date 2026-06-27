import streamlit as st
import pandas as pd
import joblib

# Page Configuration
st.set_page_config(
    page_title="Student Marks Prediction",
    page_icon="🎓",
    layout="wide"
)

# Load Trained Model and Scaler
model = joblib.load("models/linear_regression_model.pkl")
scaler = joblib.load("models/scaler.pkl")

    # --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.title("📘 About")

st.sidebar.info(
    """
    **Student Marks Prediction**

    This application predicts a student's exam score
    using a trained Machine Learning model.

    Model Used:
    - Linear Regression

    Developed using:
    - Python
    - Scikit-learn
    - Streamlit
    """
)

#App Title
st.title("🎓 Student Marks Prediction")
st.success("✅ Model Loaded Successfully")
st.write(
    "Predict a student's exam score using a trained Machine Learning model."
)

#Academic Information
col1, col2 = st.columns(2)

with col1:
    hours_studied = st.number_input(
        "Hours Studied",
        min_value=0,
        max_value=24,
        value=5
    )

    attendance = st.number_input(
        "Attendance (%)",
        min_value=0,
        max_value=100,
        value=75
    )

with col2:
    previous_scores = st.number_input(
        "Previous Scores",
        min_value=0,
        max_value=100,
        value=70
    )

    tutoring_sessions = st.number_input(
        "Tutoring Sessions",
        min_value=0,
        max_value=20,
        value=2
    )
   
# --------------------------------------------------
# Family & School Information
# --------------------------------------------------
st.subheader("🏠 Family & School Information")

# Ordinal Mappings
ordinal_mapping = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}

parental_education_mapping = {
    "High School": 0,
    "College": 1,
    "Postgraduate": 2
}

distance_mapping = {
    "Near": 0,
    "Moderate": 1,
    "Far": 2
}

col1, col2 = st.columns(2)

with col1:

    parental_involvement = st.selectbox(
        "Parental Involvement",
        ["Low", "Medium", "High"]
    )

    access_to_resources = st.selectbox(
        "Access to Resources",
        ["Low", "Medium", "High"]
    )

    family_income = st.selectbox(
        "Family Income",
        ["Low", "Medium", "High"]
    )

with col2:

    teacher_quality = st.selectbox(
        "Teacher Quality",
        ["Low", "Medium", "High"]
    )

    parental_education = st.selectbox(
        "Parental Education Level",
        ["High School", "College", "Postgraduate"]
    )

    distance_from_home = st.selectbox(
        "Distance from Home",
        ["Near", "Moderate", "Far"]
    )

# Convert to Numerical Values

parental_involvement = ordinal_mapping[parental_involvement]
access_to_resources = ordinal_mapping[access_to_resources]
family_income = ordinal_mapping[family_income]
teacher_quality = ordinal_mapping[teacher_quality]

parental_education = parental_education_mapping[parental_education]

distance_from_home = distance_mapping[distance_from_home]

# Lifestyle Information

st.subheader("💪 Lifestyle Information")

col1, col2 = st.columns(2)

with col1:

    sleep_hours = st.number_input(
        "Sleep Hours",
        min_value=0,
        max_value=24,
        value=8
    )

    physical_activity = st.number_input(
        "Physical Activity (Hours/Week)",
        min_value=0,
        max_value=20,
        value=5
    )

with col2:

    motivation_level = st.selectbox(
        "Motivation Level",
        ["Low", "Medium", "High"]
    )

# Convert Motivation Level
motivation_level = ordinal_mapping[motivation_level]


# Personal Information

st.subheader("🌐 Personal Information")

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    school_type = st.selectbox(
        "School Type",
        ["Private", "Public"]
    )

    internet_access = st.selectbox(
        "Internet Access",
        ["No", "Yes"]
    )

with col2:

    extracurricular = st.selectbox(
        "Extracurricular Activities",
        ["No", "Yes"]
    )

    peer_influence = st.selectbox(
        "Peer Influence",
        ["Negative", "Neutral", "Positive"]
    )

    learning_disabilities = st.selectbox(
        "Learning Disabilities",
        ["No", "Yes"]
    )



# Convert User Inputs to Model Format


gender_male = 1 if gender == "Male" else 0

school_type_public = 1 if school_type == "Public" else 0

internet_access_yes = 1 if internet_access == "Yes" else 0

extracurricular_yes = 1 if extracurricular == "Yes" else 0

learning_disabilities_yes = 1 if learning_disabilities == "Yes" else 0

peer_influence_neutral = 1 if peer_influence == "Neutral" else 0

peer_influence_positive = 1 if peer_influence == "Positive" else 0


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("Predict Exam Score"):

    input_data = pd.DataFrame({
        "Hours_Studied": [hours_studied],
        "Attendance": [attendance],
        "Parental_Involvement": [parental_involvement],
        "Access_to_Resources": [access_to_resources],
        "Sleep_Hours": [sleep_hours],
        "Previous_Scores": [previous_scores],
        "Motivation_Level": [motivation_level],
        "Tutoring_Sessions": [tutoring_sessions],
        "Family_Income": [family_income],
        "Teacher_Quality": [teacher_quality],
        "Physical_Activity": [physical_activity],
        "Parental_Education_Level": [parental_education],
        "Distance_from_Home": [distance_from_home],
        "Gender_Male": [gender_male],
        "School_Type_Public": [school_type_public],
        "Internet_Access_Yes": [internet_access_yes],
        "Extracurricular_Activities_Yes": [extracurricular_yes],
        "Peer_Influence_Neutral": [peer_influence_neutral],
        "Peer_Influence_Positive": [peer_influence_positive],
        "Learning_Disabilities_Yes": [learning_disabilities_yes]
    })

    scaled_data = scaler.transform(input_data)

    prediction = model.predict(scaled_data)
    st.markdown("---")
    st.subheader("📊 Prediction Result")
    st.metric(
        label="Predicted Exam Score",
        value=f"{prediction[0]:.2f}"
    )
    if prediction[0] >= 80:
        st.success("Excellent Performance 🎉")
    elif prediction[0] >= 70:
        st.info("Good Performance 👍")
    elif prediction[0] >= 60:
        st.warning("Average Performance 📚")
    else:
        st.error("Needs Improvement 💪")
    with st.expander("📄 View Input Data"):
        st.dataframe(input_data)

