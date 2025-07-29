import streamlit as st
import ollama
import json
import os
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Émile - Your Local AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables
if "messages" not in st.session_state:
    st.session_state.messages = []
if "selected_model" not in st.session_state:
    st.session_state.selected_model = None
if "file_context" not in st.session_state:
    st.session_state.file_context = None
if "file_name" not in st.session_state:
    st.session_state.file_name = None
if "temperature" not in st.session_state:
    st.session_state.temperature = 0.7
if "top_p" not in st.session_state:
    st.session_state.top_p = 0.9
if "max_tokens" not in st.session_state:
    st.session_state.max_tokens = 2048
if "model_configs" not in st.session_state:
    st.session_state.model_configs = {}
if "expert_mode" not in st.session_state:
    st.session_state.expert_mode = False

# SIDEBAR
st.sidebar.title("⚙️ Controls")

# Model Selection
st.sidebar.subheader("🧠 Model Selection")
try:
    response = ollama.list()
    available_models = []
    
    # Parse the ListResponse object
    if hasattr(response, 'models'):
        for model in response.models:
            if hasattr(model, 'model'):
                available_models.append(model.model)
    
    if available_models:
        if st.session_state.selected_model is None or st.session_state.selected_model not in available_models:
            st.session_state.selected_model = available_models[0]

        current_index = available_models.index(st.session_state.selected_model)
        
        selected_model = st.sidebar.selectbox(
            "Choose your AI model:",
            available_models,
            index=current_index,
            key="model_selector"
        )

        if selected_model != st.session_state.selected_model:
            if st.session_state.selected_model:
                st.session_state.model_configs[st.session_state.selected_model] = {
                    "temperature": st.session_state.temperature,
                    "top_p": st.session_state.top_p,
                    "max_tokens": st.session_state.max_tokens
                }
            
            st.session_state.selected_model = selected_model
            
            if selected_model in st.session_state.model_configs:
                config = st.session_state.model_configs[selected_model]
                st.session_state.temperature = config["temperature"]
                st.session_state.top_p = config["top_p"]
                st.session_state.max_tokens = config["max_tokens"]
            
            st.sidebar.success(f"🔄 Switched to: {selected_model}")
        else:
            st.sidebar.success(f"✅ Active: {st.session_state.selected_model}")
    else:
        st.sidebar.error("No Ollama models found.")
        
except Exception as e:
    st.sidebar.error(f"❌ Cannot connect to Ollama: {str(e)}")

# Quick Presets
st.sidebar.subheader("🎯 Quick Presets")
col1, col2, col3 = st.sidebar.columns(3)

with col1:
    if st.button("🎯 Focused"):
        st.session_state.temperature = 0.2
        st.session_state.top_p = 0.8
        st.sidebar.success("Applied!")

with col2:
    if st.button("⚖️ Balanced"):
        st.session_state.temperature = 0.7
        st.session_state.top_p = 0.9
        st.sidebar.success("Applied!")

with col3:
    if st.button("🎨 Creative"):
        st.session_state.temperature = 1.2
        st.session_state.top_p = 0.95
        st.sidebar.success("Applied!")

# Generation Settings
st.sidebar.subheader("🎛️ Generation Settings")
st.session_state.expert_mode = st.sidebar.toggle("🔧 Expert Mode", st.session_state.expert_mode)

if st.session_state.expert_mode:
    st.session_state.temperature = st.sidebar.slider(
        "🌡️ Temperature",
        min_value=0.0,
        max_value=2.0,
        value=st.session_state.temperature,
        step=0.1,
        help="Controls creativity"
    )
    
    st.session_state.top_p = st.sidebar.slider(
        "🎯 Top-p",
        min_value=0.1,
        max_value=1.0,
        value=st.session_state.top_p,
        step=0.05,
        help="Controls diversity"
    )
    
    st.session_state.max_tokens = st.sidebar.slider(
        "📏 Max Tokens",
        min_value=128,
        max_value=4096,
        value=st.session_state.max_tokens,
        step=128,
        help="Maximum response length"
    )

# Configuration Management
st.sidebar.subheader("💾 Configuration")
col1, col2 = st.sidebar.columns(2)

with col1:
    if st.button("💾 Save Config"):
        if st.session_state.selected_model:
            st.session_state.model_configs[st.session_state.selected_model] = {
                "temperature": st.session_state.temperature,
                "top_p": st.session_state.top_p,
                "max_tokens": st.session_state.max_tokens
            }
            st.sidebar.success("✅ Saved!")

with col2:
    if st.button("🔄 Reset"):
        st.session_state.temperature = 0.7
        st.session_state.top_p = 0.9
        st.session_state.max_tokens = 2048
        st.sidebar.success("✅ Reset!")
        st.rerun()

# File Context
st.sidebar.subheader("📁 File Context")
uploaded_file = st.sidebar.file_uploader(
    "Upload a text file:",
    type=['txt', 'md', 'py', 'js', 'html', 'css', 'json', 'csv'],
    help="File content will be used as context"
)

if uploaded_file is not None:
    try:
        file_content = uploaded_file.read().decode("utf-8")
        st.session_state.file_context = file_content
        st.session_state.file_name = uploaded_file.name
        
        st.sidebar.success(f"✅ Loaded: {uploaded_file.name}")
        st.sidebar.info(f"📄 {len(file_content):,} characters")
        
    except Exception as e:
        st.sidebar.error(f"❌ Error: {str(e)}")

if st.session_state.file_context:
    st.sidebar.info(f"📄 Using: {st.session_state.file_name}")
    if st.sidebar.button("🗑️ Clear File Context"):
        st.session_state.file_context = None
        st.session_state.file_name = None
        st.rerun()

# Chat Management
st.sidebar.subheader("💾 Chat Management")
if st.sidebar.button("💾 Save Chat"):
    if st.session_state.messages:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"emile_chat_{timestamp}.json"
        
        chat_data = {
            "timestamp": datetime.now().isoformat(),
            "model_used": st.session_state.selected_model,
            "generation_config": {
                "temperature": st.session_state.temperature,
                "top_p": st.session_state.top_p,
                "max_tokens": st.session_state.max_tokens
            },
            "file_context": st.session_state.file_name if st.session_state.file_context else None,
            "messages": st.session_state.messages
        }
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(chat_data, f, indent=2, ensure_ascii=False)
            st.sidebar.success(f"✅ Saved: {filename}")
        except Exception as e:
            st.sidebar.error(f"❌ Error: {str(e)}")
    else:
        st.sidebar.warning("⚠️ No messages to save")

if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.sidebar.success("✅ Cleared!")
    st.rerun()

# Session Stats
if st.session_state.messages:
    st.sidebar.subheader("📊 Session Stats")
    user_msgs = len([m for m in st.session_state.messages if m["role"] == "user"])
    assistant_msgs = len([m for m in st.session_state.messages if m["role"] == "assistant"])
    total_chars = sum(len(m["content"]) for m in st.session_state.messages)
    
    st.sidebar.metric("User Messages", user_msgs)
    st.sidebar.metric("Émile Responses", assistant_msgs)
    st.sidebar.metric("Total Characters", f"{total_chars:,}")

# MAIN CONTENT
st.title("🤖 Émile - Your Local AI Assistant")
st.subheader("💬 Chat with Émile")

# Current settings display
with st.expander("⚙️ Current Generation Settings"):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Model", st.session_state.selected_model or "None")
    with col2:
        st.metric("Temperature", f"{st.session_state.temperature:.1f}")
    with col3:
        st.metric("Top-p", f"{st.session_state.top_p:.2f}")
    with col4:
        st.metric("Max Tokens", st.session_state.max_tokens)

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
            # Prepare generation options
            generation_options = {
                "model": st.session_state.selected_model,
                "messages": messages_for_ollama,
                "stream": True,
                "options": {
                    "temperature": st.session_state.temperature,
                    "top_p": st.session_state.top_p,
                    "num_predict": st.session_state.max_tokens
                }
            }
            
            # Stream the response from the Ollama API
            for response_chunk in ollama.chat(**generation_options):
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
st.markdown(f"""
---
**🤖 Émile powered by Ollama** | {st.session_state.selected_model or "No model"} • Temp: {st.session_state.temperature} • Top-p: {st.session_state.top_p} • Expert: {'On' if st.session_state.expert_mode else 'Off'}
""")