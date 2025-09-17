import streamlit as st
import time


def main():
    st.title("TIMER")
    st.sidebar.title("Timer Details:")
    k = st.sidebar.number_input("Enter the Timer Duration:")
    d = st.sidebar.text_input("Enter The Unit (sec/min/hour):")

    if k is not None and d is not None :
        try:
            if d.lower() == "sec" :
                k = k
            elif d.lower() == "min" :
                k = k*60
            elif d.lower() == "hour" :
                k = k*60*60

            i =1
            fs = time.time()
            while i <= k:
                for m in range(i,i+1):
                    st.write(m,end=" ")
                    time.sleep(1)
                i = i+1
            fd = time.time()
            st.write(fs-fd)
            sound_file = "https://www.soundjay.com/button/beep-07.wav"
            st.audio(sound_file, format="audio/wav")
        except Exception as e :
            st.write(e)

if __name__ == "__main__":
    main()
