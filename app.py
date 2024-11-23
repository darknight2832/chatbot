import openai
import os
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv("AIzaSyD2twuzUQBL5RCd9JsIgiBEhPaoDo5NB7M")

if not openai_api_key:
    st.error("OpenAI API key is missing. Please set it in a .env file.")
else:
    openai.api_key = openai_api_key

# Streamlit app title and description
st.title("Chatbot with Gemini Model")
st.subheader("Ask me anything!")

# User input for the query
user_query = st.text_input("Enter your query:", placeholder="Type something...")

# Submit button
if st.button("Get Reply"):
    if not user_query.strip():
        st.warning("Please enter a valid query.")
    else:
        try:
            # Call OpenAI's Gemini model (or GPT-3.5-Turbo if Gemini is unavailable)
            response = openai.ChatCompletion.create(
                model="gemini",  # Replace "gemini" with "gpt-3.5-turbo" if needed
                messages=[{"role": "user", "content": user_query}],
                max_tokens=200,
                temperature=0.7,
                top_p=1.0,
                n=1,
            )
            # Extract and display the chatbot's reply
            reply = response['choices'][0]['message']['content'].strip()
            st.success(f"Chatbot: {reply}")
        except openai.error.OpenAIError as oe:
            st.error(f"OpenAI API Error: {str(oe)}")
        except Exception as e:
            st.error(f"Unexpected Error: {str(e)}")
