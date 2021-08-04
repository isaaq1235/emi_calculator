# Write the code for creating the EMI calculator app
import streamlit as st

def calculate_emi(p,n,r):
  emi = p * (r/100) * (1 + (r/100)) * n / 1 + (r/100) * n - 1
  return round(emi,3) 

def calculate_outstanding_balance(p,n,r,m):
	ob = p * 1 + (r/100)*n - 1 + (r/100)*m / 1 + (r/100)*n - 1
	return round(ob,3)

st.title('EMI Calculator App\n')

st.sidebar.markdown('Please select the Principal, Tenure and ROI for calculating EMI and Also M for calculating OLB\n')

p = st.sidebar.slider('Principal',1000,1000000)
n = st.sidebar.slider('Tenure',1)
r = st.sidebar.slider('ROI',1)
m = st.sidebar.slider('M',1)



if st.sidebar.button('Calculate EMI'):
	emi = calculate_emi(p,n/12,r/12)
	st.subheader(f'Calculated EMI = {emi}')

if st.sidebar.button('Calculate OLB'):
	OLB = calculate_outstanding_balance(p,n,r,m)
	st.subheader(f'Calculated OLB = {OLB}')


