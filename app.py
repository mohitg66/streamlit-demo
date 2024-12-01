import streamlit as st

# Initialize font size in session state if not already present
if 'font_size' not in st.session_state:
    st.session_state.font_size = 16  # Default font size

# Create buttons to increase and decrease font size
if st.button("Increase Font Size"):
    st.session_state.font_size += 2
if st.button("Decrease Font Size"):
    st.session_state.font_size -= 2

# Apply custom CSS to change the font size
st.markdown(f"""
    <style>
    body {{
        font-size: {st.session_state.font_size}px;
    }}
    </style>
    """, unsafe_allow_html=True)

# Your app content goes here
st.write("This text will change size when you click the buttons.")


from streamlit_geolocation import streamlit_geolocation

location = streamlit_geolocation()

if location["latitude"] is not None:
    st.write(location)
    # display on map
    st.map(data=[location])
else:
    st.write("Location data is not available.")
