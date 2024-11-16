import streamlit as st
import requests

# Webhook URL from your Make scenario
WEBHOOK_URL = "https://hook.integromat.com/your-unique-webhook-url"

# Streamlit app UI
st.title("Trigger Make Scenario from Streamlit")
st.write("Select an option or input data to trigger a Make scenario.")

# Example user input
user_text = st.text_input("Enter some text:", "")
user_selection = st.selectbox("Choose an option:", ["Option A", "Option B", "Option C"])

# Button to trigger the scenario
if st.button("Send Data to Make"):
    # Data to send to the webhook
    payload = {
        "text": user_text,
        "selection": user_selection
    }

    try:
        # Sending POST request to the webhook
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code == 200:
            st.success("Data successfully sent to Make!")
        else:
            st.error(f"Failed to send data. Status code: {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
