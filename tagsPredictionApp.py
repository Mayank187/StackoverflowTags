# Streamlit dependencies
import streamlit as st
import requests


# Define the main function that will encapsulate the application
def main():
    # Set the title of the application
    st.title('Stack Overflow Tag Predictor')
    url = 'http://localhost:5000/predict'
    # Get input from the user
    title = st.text_input('Title:')
    body = st.text_area('Body:', height=200)

    # Create a predict button and on clicking, run the model
    if st.button('Predict'):
        question = title+' '+ body
        data = {
            'question': question,
        }
        response = requests.post(url, json = data)
        if response.status_code == 200:
            tags = response.json()[0]
            t = ""
            for i in tags:
                t += i+" "
            st.write('Predicted Tags:', t)
        else:
            st.write("Error submitting form.")
        

# Call the main function to run the app when the script is executed
if __name__ == '__main__':
    main()
