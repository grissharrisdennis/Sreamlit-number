import streamlit as st

def largest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

def main():
    st.title("The largest of three numbers")
    st.write("Enter the numbers below:")

    a=st.number_input()
    b = st.number_input()
    c = st.number_input()

    if st.button("Find largest number"):
        result = largest(a, b, c)
        st.write(f"The largest number is {result}")


if __name__ == '__main__':
    main()