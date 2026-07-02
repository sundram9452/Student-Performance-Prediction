import streamlit as st
import pandas as pd
import pickle

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)
# -----------------------------
# Sidebar
# -----------------------------
# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("🎓 Student Performance")

st.sidebar.markdown("---")

st.sidebar.header("👨‍💻 Developer")
st.sidebar.write("**Sundram Pandey\n" \
"&\n"
"Swastik Shukla**")

st.sidebar.header("🎓 Internship")
st.sidebar.write("AIML Summer Internship 2026")

st.sidebar.header("🤖 Model")
st.sidebar.write("Linear Regression")

st.sidebar.metric("R² Score", "0.8633")

st.sidebar.markdown("---")

st.sidebar.info(
"""
This application predicts the
final student grade (G3)
using Machine Learning.
"""
)

# -----------------------------
# Load Model and Encoders
# -----------------------------
with open("student_performance_model.pkl", "rb") as file:
    saved_objects = pickle.load(file)

model = saved_objects["model"]
encoders = saved_objects["encoders"]

# -----------------------------
# App Title
# -----------------------------
st.title("🎓 Student Performance Prediction System")

st.markdown(
"""
Welcome!

This application predicts the **Final Grade (G3)** based on
important academic and personal factors using a trained
Machine Learning model.
"""
)

st.markdown("---")

st.header("📝 Student Details")
# -----------------------------
# User Inputs
# -----------------------------
# -----------------------------
# User Inputs
# -----------------------------

st.header("📝 Student Information")

left, right = st.columns(2)

with left:

    age = st.number_input(
        "Age",
        min_value=15,
        max_value=22,
        value=17
    )

    studytime = st.selectbox(
        "Weekly Study Time",
        [1, 2, 3, 4],
        help="1=<2 hrs, 2=2-5 hrs, 3=5-10 hrs, 4=>10 hrs"
    )

    failures = st.number_input(
        "Past Failures",
        min_value=0,
        max_value=4,
        value=0
    )

    absences = st.number_input(
        "Absences",
        min_value=0,
        max_value=100,
        value=4
    )

with right:

    g1 = st.number_input(
        "First Period Grade (G1)",
        min_value=0,
        max_value=20,
        value=10
    )

    g2 = st.number_input(
        "Second Period Grade (G2)",
        min_value=0,
        max_value=20,
        value=10
    )

    higher = st.selectbox(
        "Higher Education",
        ["yes", "no"]
    )

    internet = st.selectbox(
        "Internet Access at Home",
        ["yes", "no"]
    )
# -----------------------------
# Predict
# -----------------------------
if st.button("Predict Final Grade"):

    input_df = pd.DataFrame({
        "age": [age],
        "studytime": [studytime],
        "failures": [failures],
        "absences": [absences],
        "G1": [g1],
        "G2": [g2],
        "higher": [higher],
        "internet": [internet]
    })

    # Encode categorical columns
    for column, encoder in encoders.items():
        input_df[column] = encoder.transform(input_df[column])

    with st.spinner("Predicting..."):
        prediction = model.predict(input_df)[0]
    st.markdown("---")

    st.metric(
        label="🎯 Predicted Final Grade (G3)",
        value=f"{prediction:.2f} / 20"
    )

    st.progress(min(prediction / 20, 1.0))

    st.markdown("### 📊 Performance Analysis")

    if prediction >= 16:
        st.success("🏆 Excellent Performance")
        st.balloons()

        st.markdown("""
### 💡 Recommendations

✅ Continue your current study routine.

✅ Maintain regular attendance.

✅ Keep performing well in internal assessments.

✅ You are on track for excellent academic performance.
""")

    elif prediction >= 12:
        st.info("👍 Good Performance")

        st.markdown("""
### 💡 Recommendations

• Increase study time slightly.

• Revise difficult subjects regularly.

• Reduce unnecessary absences.

• Practice previous year questions.
""")

    elif prediction >= 8:
        st.warning("🙂 Average Performance")

        st.markdown("""
### 💡 Recommendations

• Increase weekly study hours.

• Improve G1 and G2 scores.

• Attend classes regularly.

• Ask teachers for help whenever required.
""")

    else:
        st.error("⚠ Needs Academic Support")

        st.markdown("""
### 💡 Recommendations

• Create a daily study schedule.

• Attend every class.

• Focus on understanding concepts.

• Seek guidance from teachers and parents.
""")

    st.markdown("---")
    st.caption(
        "Developed by Sundram Pandey and Swastik Shukla | AIML Summer Internship 2026 at MNNIT(IIHF)"
    )
   
