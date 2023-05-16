# Project Objective
PowerSystem Bot is a web application aimed at assisting electrical engineering master's students in their studies. With the complexity of power system protection concepts, it's crucial to provide an interactive platform that facilitates quick access to relevant information.

Using cutting-edge large language model(LLM) techniques, PowerSystem Bot offers a question and answering interface that allows students to effortlessly find answers to their queries. The bot leverages a database of electrical engineering knowledge in the form of the lecture notes, to provide accurate and detailed responses.

By utilizing this platform, students can save time and effort by typing their questions directly, eliminating the need to search through lengthy PDF documents. PowerSystem Bot serves as a valuable educational tool, empowering students to enhance their understanding and excel in their power system protection studies.

With PowerSystem Bot, students can efficiently navigate the complexities of electrical engineering, receive immediate responses to their inquiries, and foster a productive and engaging learning experience in the field of power system protection.

# Tools and Tech
- Backend development : Python for building the whole backend application
- LLM model :  OpenAI's GPT 3.5 model
- Framework for developing the LLM : Langchain
- Vector Database : Chroma Vector Database
- Frontend UI : Streamlit web application framework

# Technical details

The PowerSystemBot application is built using a combination of powerful tools and technologies. The backend development is done in Python, providing a robust foundation for the entire application. OpenAI's GPT 3.5 model is employed as the language model, enabling the generation of accurate and context-aware responses. To streamline the development process of the language model, Langchain framework is utilized, with its agent to decide which steps to take, or in this case, which lecture notes or documents to look at. 

The application leverages Chroma Vector Database, a reliable storage system to store the embeddings to enable fast retrieval. On the frontend, the user interface is developed using Streamlit web application framework, offering a seamless and intuitive experience for users. Together, these tools and technologies form the backbone of PowerSystemBot, enabling efficient and effective interactions between users and the AI-powered question and answering system.
