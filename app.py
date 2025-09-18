import streamlit as st
import time


def main():
    st.title("TIMER")
    st.sidebar.title("Timer Details:")
    st.write("<--Open The SideBar")
    k =  st.sidebar.number_input("Enter the Timer Duration:",step=1,max_value=60)
    d = st.sidebar.text_input("Enter The Unit (sec/min/hour):")

    if k is not None and d is not None :
        try:
            st.success.write("Input Is Getting Proccessed")
            with st.spinner("Processing..."):
                st.write("Hi!")
            if d.lower() == "sec" :
                k = k
            elif d.lower() == "min" :
                k = k*60
            elif d.lower() == "hour" :
                k = k*60*60
            else :
                st.write("Please enter the Data!")

            i =1
            while i <= k:
                for m in range(i,i+1):
                    st.write(m,end=" "    )
                    time.sleep(1)
                i = i+1
            st.markdown(
                """
                <audio autoplay>
                D:\MyWork\Python_Learning\Timer\beep-329314.mp3
                </audio>
                """,unsafe_allow_html=True)
        except Exception as e :
            st.write(e)

if __name__ == "__main__":
    main()
