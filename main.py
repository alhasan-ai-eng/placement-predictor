import streamlit as st
import pickle

st.header("***Know Your Chances Of Placement  💰***")

iq=st.number_input("Enter Your IQ:")
cgpa=st.number_input("Enter Your CGPA:")
btn=st.button("Predict!")

if btn:
    model=pickle.load(open("placement.pkl","rb"))
    pred=model.predict([[iq,cgpa]])[0]

    # st.markdown(f"Result: {pred}")

    if iq >= 100 and cgpa >= 5.5 :
        pred = 1
    else:
        pred = 0


    if pred == 1:
        st.markdown("*Congratulations! You are eligible for Placement 🎉*")
    else:
        st.markdown("*Sorry, you are currently not eligible for Placement.*")

