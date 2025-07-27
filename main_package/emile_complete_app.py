import streamlit as st
import ollama
import json
import os
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Émile - Personal AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# Set the title of the web app
st.title("🤖 Émile - Your Personal Local AI Assistant")

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_model" not in st.session_state:
    st.session_state.selected_model = None

if "file_context" not in st.session_state:
    st.session_state.file_context = None

if "file_name" not in st.session_state:
    st.session_state.file_name = None

# Sidebar for controls
with st.sidebar:
    st.header("⚙️ Controls")
    
    # Model Selection
    st.subheader("🧠 Model Selection")
    try:
        # Get available models from Ollama
        models_response = ollama.list()
        
        # Parse the Pydantic ListResponse object correctly
        available_models = []
        
        # The response is a Pydantic object, not a dict
        if hasattr(models_response, 'models'):
            for model in models_response.models:
                # Each model should be a Pydantic Model object with a .model attribute
                if hasattr(model, 'model'):
                    available_models.append(model.model)
                else:
                    # Fallback: try to extract from string representation
                    model_str = str(model)
                    if "model='" in model_str:
                        start = model_str.find("model='") + 7
                        end = model_str.find("'", start)
                        if end > start:
                            available_models.append(model_str[start:end])
        
        if available_models:
            # Create selectbox for model selection
            selected_model = st.selectbox(
                "Choose your AI model:",
                available_models,
                index=0 if st.session_state.selected_model is None else available_models.index(st.session_state.selected_model) if st.session_state.selected_model in available_models else 0
            )
            
            # Check if model changed
            if st.session_state.selected_model != selected_model:
                if st.session_state.selected_model is not None:
                    st.session_state.messages = []  # Clear chat history when model changes
                    st.rerun()
                st.session_state.selected_model = selected_model
            
            st.success(f"✅ Using: {selected_model}")
        else:
            st.error("No Ollama models found. Please install a model first.")
            st.stop()
            
    except Exception as e:
        st.error(f"❌ Cannot connect to Ollama: {str(e)}")
        st.info("Make sure Ollama is running locally")
        st.stop()
    
    # File Upload & Context
    st.subheader("📁 File Context")
    uploaded_file = st.file_uploader(
        "Upload a text file for context:",
        type=['txt', 'md', 'py', 'js', 'html', 'css', 'json'],
        help="The content will be used as context for your conversations"
    )
    
    if uploaded_file is not None:
        try:
            # Read file content
            file_content = uploaded_file.read().decode("utf-8")
            st.session_state.file_context = file_content
            st.session_state.file_name = uploaded_file.name
            
            st.success(f"✅ Loaded: {uploaded_file.name}")
            st.info(f"📄 {len(file_content)} characters loaded as context")
            
        except Exception as e:
            st.error(f"❌ Error reading file: {str(e)}")
    
    # Show current file context status
    if st.session_state.file_context:
        st.info(f"📄 Using context from: {st.session_state.file_name}")
        if st.button("🗑️ Clear File Context"):
            st.session_state.file_context = None
            st.session_state.file_name = None
            st.rerun()
    
    # Chat History Management
    st.subheader("💾 Chat Management")
    
    # Save Chat button
    if st.button("💾 Save Chat"):
        if st.session_state.messages:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"emile_chat_{timestamp}.json"
            
            # Create chat data with metadata
            chat_data = {
                "timestamp": datetime.now().isoformat(),
                "model_used": st.session_state.selected_model,
                "file_context": st.session_state.file_name if st.session_state.file_context else None,
                "messages": st.session_state.messages
            }
            
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    json.dump(chat_data, f, indent=2, ensure_ascii=False)
                st.success(f"✅ Chat saved as: {filename}")
            except Exception as e:
                st.error(f"❌ Error saving chat: {str(e)}")
        else:
            st.warning("⚠️ No messages to save")
    
    # Clear Chat button
    if st.button("🗑️ Clear Conversation"):
        st.session_state.messages = []
        st.rerun()
    
    # Stats
    if st.session_state.messages:
        st.subheader("📊 Session Stats")
        user_msgs = len([m for m in st.session_state.messages if m["role"] == "user"])
        assistant_msgs = len([m for m in st.session_state.messages if m["role"] == "assistant"])
        st.metric("User Messages", user_msgs)
        st.metric("Émile Responses", assistant_msgs)

# Main chat interface
st.subheader("💬 Chat with Émile")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to ask Émile?"):
    
    # Add the user's message to the chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display the user's message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare the message for Ollama
    messages_for_ollama = []
    
    # Add file context as system message if available
    if st.session_state.file_context:
        context_message = {
            "role": "system", 
            "content": f"You are Émile, a helpful personal AI assistant. You have been provided with the following file context to help answer questions:\n\n{st.session_state.file_context}\n\nUse this context when relevant to the user's questions, but don't mention it unless directly relevant."
        }
        messages_for_ollama.append(context_message)
    else:
        # Add a system message to establish Émile's identity
        system_message = {
            "role": "system",
            "content": "You are Émile, a helpful personal AI assistant running locally. Be friendly, knowledgeable, and concise in your responses."
        }
        messages_for_ollama.append(system_message)
    
    # Add chat history
    messages_for_ollama.extend([
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages
    ])

    # Display the assistant's response
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            # Stream the response from the Ollama API
            for response_chunk in ollama.chat(
                model=st.session_state.selected_model,
                messages=messages_for_ollama,
                stream=True,
            ):
                # Append the new chunk to the full response
                full_response += response_chunk['message']['content']
                # Update the placeholder with the new, combined response
                response_placeholder.markdown(full_response + "▌")
            
            # Final update to the placeholder without the cursor
            response_placeholder.markdown(full_response)
            
        except Exception as e:
            error_msg = f"❌ Error communicating with Émile: {str(e)}"
            response_placeholder.markdown(error_msg)
            full_response = error_msg
        
    # Add the full assistant response to the chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666; font-size: 0.8em;'>"
    "🤖 Émile is powered by Ollama running locally on your machine"
    "</div>", 
    unsafe_allow_html=True
)