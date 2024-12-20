import os
import autogen
import streamlit as st
from stream_to_expand import StreamToExpander
import sys
from groq import Groq
from autogen import ConversableAgent


st.title("LLM Agent Platform")

# Sidebar Inputs
st.sidebar.header("Configuration")

# Model Selection
model_type = st.sidebar.selectbox("Choose the LLM provider:", ["OpenAI", "Groq"])

# OpenAI Configuration
if model_type == "OpenAI":
    OPENAI_API_KEY = st.sidebar.text_input("Enter your OpenAI API Key:", type="password")
    if not OPENAI_API_KEY:
        st.sidebar.warning("Please enter your OpenAI API Key to proceed.")
        st.stop()
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

    openai_model = st.sidebar.selectbox(
        "Choose the OpenAI model:",
        ["gpt-3.5-turbo", "gpt-4"]
    )
    llm_config = {"model": openai_model}

# Groq Configuration
elif model_type == "Groq":
    GROQ_API_KEY = st.sidebar.text_input("Enter your Groq API Key:", type="password")
    if not GROQ_API_KEY:
        st.sidebar.warning("Please enter your Groq API Key to proceed.")
        st.stop()
    os.environ["GROQ_API_KEY"] = GROQ_API_KEY

    groq_model = st.sidebar.selectbox(
        "Choose the Groq model:",
        [
            "llama-3.1-70b-versatile",
            "llama-3.1-8b-instant",
            "llama-3.2-11b-vision-preview",
            "llama-3.2-1b-preview",
            "llama-3.2-3b-preview",
            "llama-3.2-90b-vision-preview",
            "llama-3.3-70b-specdec",
            "llama-3.3-70b-versatile",
            "llama-guard-3-8b",
            "llama3-70b-8192",
            "llama3-8b-8192"
        ]
    )
    config_list = [
        {
            "model": groq_model,
            "api_key": os.environ.get("GROQ_API_KEY"),
            "api_type": "groq",
        }
    ]
    llm_config = {"config_list": config_list}

# User Input for Writer and Critic Instructions
writer_instruction = st.sidebar.text_area(
    "Enter Writer's System Instruction:",
    "You are an expert analyst who finds gender diversity in the given text. Only return animal and gender at the end."
)
critic_instruction = st.sidebar.text_area(
    "Enter Critic's System Instruction:",
    "You are a critic. You review the work of the writer and provide constructive feedback to help improve the quality of the content."
)

# Main Content Input
content = st.text_area("Enter the text content for analysis:")

# Button to Submit Content
if st.button("Submit"):
    if not content:
        st.warning("Please enter the content to proceed.")
        st.stop()

    if model_type == "OpenAI":
        # Writer Agent (OpenAI)
        writer = autogen.AssistantAgent(
            name="Writer",
            system_message=writer_instruction,
            llm_config=llm_config,
        )

        # Critic Agent (OpenAI)
        critic = autogen.AssistantAgent(
            name="Critic",
            is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0,
            llm_config=llm_config,
            system_message=critic_instruction,
        )

    elif model_type == "Groq":
        # Writer Agent (Groq)
        writer = ConversableAgent(
            name="Writer",
            llm_config=llm_config,
            human_input_mode="NEVER",
        )

        # Critic Agent (Groq)
        critic = ConversableAgent(
            name="Critic",
            llm_config=llm_config,
            human_input_mode="NEVER",
        )

    # Interaction Between Agents
    res = critic.initiate_chat(
        recipient=writer,
        message=content,
        max_turns=2,
        summary_method="last_msg"
    )

    reply = writer.generate_reply(messages=[{"content": content, "role": "user"}])

    # Display in Streamlit
    expander = st.expander("Agent Outputs", expanded=True)
    stream_to_expander = StreamToExpander(expander)
    sys.stdout = stream_to_expander  # Redirect stdout to capture agent outputs

    print(reply)

    # Reset stdout
    sys.stdout = sys.__stdout__
