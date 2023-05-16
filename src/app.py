import os
import streamlit as st
from model import create_model_and_agent
from chroma.vector_database import chroma_vectordb


st.title('🦜🔗 Power system Protection')

_, store = chroma_vectordb()

def set_api_key(api_key):
    os.environ["OPENAI_API_KEY"] = api_key

with st.sidebar:
    st.markdown("# PowerSystemsBot ")
    st.markdown(
        "**PowerSystemsBot** is an interactive Q & A bot that helps you quickly find answers and information on all programs  \n"
        "during your electrical engineering masters studies in KNUST..\n")

    st.markdown(
        "Currently, only Protection of Power Systems(EE 559) is available "
    )
    st.markdown("-------")
    st.markdown("👨🏾‍💻 Developer: Hyacinth Ampadu")
    st.markdown("-------")
    st.markdown("Follow this link to get your open-ai api key for free to use to use the App  --> \
                 https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/")
    st.markdown("PS: (API key doesnt get saved)")
    # Create a text input box for the user to enter the API key
    api_key = st.text_input("Enter your API key")
    
    # Set API key button
    if st.button("Set API Key"):
        set_api_key(api_key)
        st.success("API key set successfully!")

# Create a text input box for the user
instruction = "If context length is exceed, summarize the reponse to a level students can understand"
prompt = st.text_input("Input your prompt here")

# If the user hits enter
agent_executor = create_model_and_agent()
if prompt:
    response = agent_executor.run(instruction +"."+ prompt)
    # print response to screen
    st.write(response)

    # Add block to show the source the answer came from 
    with st.expander('Source Material'):
         # Find relevant pages
        search = store.similarity_search_with_score(prompt) 
        # Print to screen the most important one 
        st.write(search[0][0].page_content) 