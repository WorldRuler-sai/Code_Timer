import streamlit as st

def main():
    st.title("TIMER")
    st.sidebar.title("Timer Details:")
    k = st.sidebar.number_input("Enter the Timer Duration:")
    d = st.sidebar.text_input("Enter The Unit (sec/min/hour):")

    if k is not None and d is not None :
        st.write(d,k)

if __name__ == "__main__":
    main()