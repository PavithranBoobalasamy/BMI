import streamlit as st

def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)  # Convert height to meters

st.title("BMI Calculator")

# Change the hover effect of the selectbox
st.markdown(
    """
    <style>
    .stSelectbox>div:hover {
        border-color: #63ace5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

weight = st.number_input("Enter weight (kg)")
height = st.number_input("Enter height (cm)")

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)

    st.write(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        st.write("Underweight")
    elif bmi < 25:
        st.write("Normal weight")
    elif bmi < 30:
        st.write("Overweight")
    else:
        st.write("Obese")
