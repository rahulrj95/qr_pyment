import streamlit as st
import qrcode

upi_id = "ravi.129@superyes"
amount = st.number_input("enter your amount = ", step=1)
phonepe_url = f'upi://pay?pa={upi_id}&am={amount}&cu=INR'
phonepe_qr = qrcode.make(phonepe_url)
phonepe_qr.show()
