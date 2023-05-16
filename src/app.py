import os
import streamlit as st
from model import create_model_and_agent
from chroma.vector_database import chroma_vectordb


st.title('🦜🔗 Power system Protection')

_, store = chroma_vectordb()
# Create a text input box for the user to enter their API key
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


# If the user clicks a button to set the API key


# Create a text input box for the user
instruction = "If context length is exceed, summarize the reponse to a level students can understand"
prompt = st.text_input("Input your prompt here")

# If the user hits enter
agent_executor = create_model_and_agent()
if prompt:
    # Then pass the prompt to the LLM
    response = agent_executor.run(instruction +"."+ prompt)
    # ...and write it out to the screen
    st.write(response)

    #With a streamlit expander  
    with st.expander('Source Material'):
         #Find the relevant pages
        search = store.similarity_search_with_score(prompt) 
        # Write out the first 
        st.write(search[0][0].page_content) 