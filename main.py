import streamlit as st
import qrcode
from PIL import Image
import io

# Title
st.title("PhonePe Payment QR Code Generator")

# UPI ID
upi_id = "ravi.129@superyes"

# User input for amount
amount = st.number_input("Enter your amount:", step=1, min_value=1)

# Generate UPI Payment URL
phonepe_url = f"upi://pay?pa={upi_id}&am={amount}&cu=INR"

# Generate QR Code
qr = qrcode.QRCode(box_size=10, border=5)
qr.add_data(phonepe_url)
qr.make(fit=True)
img = qr.make_image(fill="black", back_color="white")

# Convert QR Code to Streamlit Image format
buf = io.BytesIO()
img.save(buf, format="PNG")

# Show QR Code in Streamlit
st.image(buf, caption="Scan to Pay", use_column_width=False)

# Download Button
st.download_button(
    label="Download QR Code",
    data=buf.getvalue(),
    file_name="phonepe_qr.png",
    mime="image/png"
)
