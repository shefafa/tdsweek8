import streamlit as st

st.title('Finding largest of three numbers')
st.subheader('by shefa')
st.header('Enter three numbers')
x= st.number_input('Enter first number:')
y= st.number_input('Enter second number:')
z= st.number_input('Enter third number:')

if x>y and x>z:
  st.write(x,'is the largest number')
elif y>x and y>z:
  st.write(y, 'is the largest number')
else:
   st.write(z, 'is the largest number')
