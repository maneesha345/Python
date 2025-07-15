import streamlit as st

st.title("Calculator App")
st.write("Welcome to Calculator App. Use the form below to perform operations.")

a = st.number_input("Enter value of a:", format="%.2f")
b = st.number_input("Enter value of b:", format="%.2f")

operation = st.radio("Choose Operation", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operation == "Add":
        result = a + b
    elif operation == "Subtract":
        result = a - b
    elif operation == "Multiply":
        result = a * b
    elif operation == "Divide":
        if b == 0:
            result = "Cannot divide by zero"
        else:
            result = a / b
    st.write("Result:", result)