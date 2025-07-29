# 🤖 Émile-1: Your Personal Local AI Assistant

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF6B6B.svg)](https://streamlit.io)
[![Ollama](https://img.shields.io/badge/Powered%20by-Ollama-000000.svg)](https://ollama.ai)
[![University of Toronto](https://img.shields.io/badge/University%20of-Toronto-003F7F.svg)](https://www.utoronto.ca/)
[![Research](https://img.shields.io/badge/Type-Research-brightgreen.svg)](https://github.com)

**v1.1** - *Democratizing AI Access Through Local Computing*
---

This project presents a user-friendly Streamlit interface for running AI models locally via Ollama. Chat with AI models completely offline, upload files for context, and manage your conversations - all without any paywalls or privacy concerns! 

Émile-1 allows for consumer level engagement with models typically associated with research and proprietary testing. With a focus on user experience, this simple app encourages the democratization of AI development by empowering the user to engage with LLMs and gain an understanding of how different models operate and process information.

<img width="2940" height="1663" alt="image" src="https://github.com/user-attachments/assets/3cba87be-5300-4c84-ab88-0c0bed911be1" />
> Expert Mode: On  

<img width="2940" height="1664" alt="image" src="https://github.com/user-attachments/assets/571409d2-e980-465c-b352-a3b7bc0293bc" />
> Expert Mode: Off  

- **Version Features:**

  –> Config presets for easy tuning. Adjust model parameters for different tasks.

  –> "Expert Mode": Allows full, dynamic user control over temperature, top-p, and max tokens. Configuration can be changed dynamically and/or reset during chat while maintaining conversation context.

  –> Model hot-swapping: Change models dynamically during chats while preserving conversation. See how different models behave with a shared context!
  
> python3 -m streamlit run emile_v1_1.py

## Version History

**v1.0** - Basic and simple. Load models, upload files, and save chats!

<img width="2940" height="1595" alt="image" src="https://github.com/user-attachments/assets/95cd32d7-5a1c-4794-8766-07c73182421e" />

---

## 🏗️ System Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Streamlit     │────│   Émile Core     │────│     Ollama      │
│   Frontend      │    │   (Chat Logic)   │    │   (LLM Engine)  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                        │                        │
         │                        ▼                        │
         │              ┌──────────────────┐               │
         │              │  File Context    │               │
         │              │   Management     │               │
         │              └──────────────────┘               │
         │                        │                        │
         ▼                        ▼                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│ Chat History    │────│ Model Selection  │────│ Local Storage   │
│ Management      │    │ & Switching      │    │ (Private Data)  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

---

---

## ✨ Core Features

### 🧠 **Intelligent Model Management**
- Dynamic detection of locally installed Ollama models
- Seamless switching between models during conversations
- Automatic chat history clearing on model changes for clean contexts

### 📁 **File Context System**  
- Support for multiple file types: `.txt`, `.md`, `.py`, `.js`, `.html`, `.css`, `.json`
- Intelligent context integration using system-level prompting
- Real-time file status indicators and context management

### 💾 **Professional Chat Management**
- Timestamped conversation exports with full metadata
- JSON format preserving model information and file context
- Session statistics and conversation analytics

### 🎨 **User Experience**
- Clean, intuitive Streamlit interface with emoji-enhanced navigation
- Real-time streaming responses for natural conversation flow
- Responsive design with sidebar controls and main chat area

### 🔒 **Privacy & Performance**
- **100% Local Processing**: No data transmission to external servers
- **Zero Cost Operation**: No API keys, subscriptions, or usage limits
- **Offline Capable**: Works completely without internet connection
- **Memory Efficient**: Optimized for local hardware resources

---

---

## 🚀 Installation & Setup

### **System Requirements**
- **Operating System**: macOS, Linux, or Windows
- **Python**: 3.8 or higher
- **Memory**: 8GB+ RAM recommended (16GB+ for larger models)
- **Storage**: 5-50GB depending on models (each model typically 2-8GB)

### **Quick Start Guide**

#### 1. **Ollama Installation**
```bash
# macOS/Linux (Recommended)
curl -fsSL https://ollama.ai/install.sh | sh

# Windows: Download from https://ollama.ai
# Manual installation with GUI installer
```

#### 2. **Model Acquisition**
```bash
ollama pull llama3        # Base Model (Recommended for beginners)
ollama pull mistral       # Fast general-purpose model
ollama pull codellama     # Code analysis specialist  
ollama pull gemma:7b      # Google's research model
ollama pull phi3          # Microsoft's efficient model
```

#### 3. **Émile Deployment**
```bash
# Repository Setup
git clone https://github.com/Baglecake/Emile-1.git
cd Emile-1

# Dependency Installation
pip install -r requirements_txt.txt

# Launch Application
streamlit run emile_complete_app.py
```

#### 4. **Access Interface**
Navigate to `http://localhost:8501` in your web browser

---

## 📊 Model Compatibility Matrix

| Model | Size | Best For | Memory Req. |
|-------|------|----------|-------------|
| `gemma2` | 5.0GB | General conversation, reasoning, and more complex tasks | 8GB+ |
| `qwen2.5` | 4.7GB | General conversation, reasoning, better at producing structured responses | 8GB+ |
| `llama3` | 4.7GB | General conversation, reasoning | 8GB+ |
| `codellama` | 3.8GB | Code analysis, programming help | 8GB+ |
| `mistral` | 4.1GB | Creative writing, analysis | 8GB+ |
| `phi3` | 2.3GB | Punches higher than its weight, fast responses | 4GB+ |
| `gemma2b` | 1.7GB | Lightweight, fast responses | 4GB+ |

Install models with: `ollama pull <model-name>`

---

## 📖 Usage Guide

### Model Selection
- Use the sidebar dropdown to switch between installed Ollama models
- Changing models automatically clears the chat history for a fresh start

### File Upload
- Upload text-based files in the sidebar for context
- Émile will use the file content to answer questions about your code, documents, or data
- Clear file context anytime with the "Clear File Context" button

### Chat Management
- **Save Chat**: Exports your conversation as a timestamped JSON file with metadata
- **Clear Conversation**: Starts a fresh chat session
- **Session Stats**: Track your message counts in real-time

### Example Workflows
- Upload a Python file and ask "How can I improve this code?"
- Load a Markdown document and ask "Summarize the key points"
- Share a JSON file and ask "Explain this data structure"
  
### Example: Émile analyzing uploaded sensor data and detecting a temperature trend - Llama3
<img width="2940" height="1595" alt="image" src="https://github.com/user-attachments/assets/70273347-2863-4264-8e24-a68f4eaff21c" />

### Example: Émile analyzing uploaded monthly sales data and delivering a product report - Llama3
<img width="2940" height="1596" alt="image" src="https://github.com/user-attachments/assets/d71698d3-dbbe-45b0-b4a8-4ab10fcd2e32" />

### Example: Émile explaining the architecture of a machine learning model and its training data - Mistral
<img width="2940" height="1596" alt="image" src="https://github.com/user-attachments/assets/b1ce4c32-00d6-406e-9e1e-dc2d059ba593" />

> See **[tests folder](./test_context/)** for test files to upload for context.

### 📝 More Example Conversations

Want to see more of Émile in action? Check out some saved conversations with different models in our **[examples folder](./Chat_Examples/)**.

These examples showcase the performance trade-offs between larger models that excel at complex reasoning and smaller, more efficient models that are perfect for quick tasks.

## 🔧 Configuration

### Custom Model Settings
Émile automatically detects installed models. To install specific models:

```bash
# List available models
ollama list

# Pull specific versions
ollama pull llama3:8b
ollama pull llama3:70b
```

### File Type Support
Currently supported file types:
- `.txt` - Plain text
- `.md` - Markdown
- `.py` - Python code
- `.js` - JavaScript
- `.html` - HTML markup
- `.css` - Stylesheets
- `.json` - JSON data

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Ideas for Contributions
- Support for more file types (PDF, DOCX, etc.)
- Dark/light theme toggle
- System prompt customization
- Export conversations to different formats
- Model performance metrics
- Voice input/output
- Multi-language support

## 📋 Requirements

- Python 3.8+
- Streamlit ≥ 1.28.0
- Ollama Python client ≥ 0.1.0
- Ollama server running locally

---

## 🐛 Troubleshooting & Diagnostics

### **Common Issues & Solutions**

#### **Connection Errors**
```bash
# Error: "Cannot connect to Ollama"
# Solution: Verify Ollama service status
ollama serve          # Start Ollama manually
ollama list           # Verify models are installed
curl http://localhost:11434    # Test API connectivity
```

#### **Model Detection Issues**  
```bash
# Error: "No models found"
# Solution: Install and verify models
ollama pull llama3    # Install base model
ollama list           # Confirm installation
# Restart Streamlit application
```

#### **Performance Optimization**
```bash
# For systems with limited RAM:
ollama pull phi3      # Use lightweight model
ollama pull gemma:2b  # Use smaller variant

# Monitor system resources:
htop                  # Linux/macOS
Activity Monitor      # macOS GUI
Task Manager          # Windows
```

#### **File Upload Issues**
- **Supported formats**: `.txt`, `.md`, `.py`, `.js`, `.html`, `.css`, `.json`
- **File size limit**: 10MB maximum per file
- **Encoding**: UTF-8 text encoding required

### **Support Channels**
- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/Baglecake/Emile-1/issues)
- **Discussions**: Join the conversation in [GitHub Discussions](https://github.com/Baglecake/Emile-1/discussions)

---

## 🔧 Advanced Configuration

### **Environment Variables**
```bash
# Optional: Custom Ollama host
export OLLAMA_HOST="http://localhost:11434"

# Optional: Model storage location  
export OLLAMA_MODELS="/custom/path/to/models"
```

### **Performance Tuning**
```python
# In emile_complete_app.py, adjust these parameters:
# For faster responses (lower quality):
temperature = 0.3
max_tokens = 512

# For higher quality (slower responses):
temperature = 0.7  
max_tokens = 2048
```

---

---

## 🎯 Project Roadmap

### **Version History**
- **v1.0** - Initial release with core chat functionality, model selection, and file context
- **v1.1** - Planned: Live model hotswapping (no chat reset)
- **v1.2** - Planned: In-app configuration settings (ie - temperature, max_tokens)
- **v1.3** - Planned: PDF support, conversation search, dark mode
- **v1.4** - Planned: Plugin system, custom system prompts, batch processing

### **Upcoming Features**
- [ ] **Document Processing**: PDF and DOCX file support with text extraction
- [ ] **Enhanced UI**: Dark/light theme toggle, responsive mobile design
- [ ] **Advanced Context**: Multi-file context management, context summarization
- [ ] **System Customization**: Custom system prompts, personality configuration
- [ ] **Export Options**: Multiple export formats (PDF, Word, plain text)
- [ ] **Performance Analytics**: Response time metrics, token usage tracking

---

## 🤝 Contributing to Émile

We welcome contributions from the community! See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

### **Research & Academic Use**
Émile-1 is designed to support research into local AI deployment and democratization of AI access. If you're using Émile in academic research, please consider:

- Citing the project in academic publications
- Sharing usage statistics and performance metrics
- Contributing improvements back to the community
- Documenting novel use cases and applications

---

## 📄 License & Attribution

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for complete details.

### **Citation Information**
```bibtex
@software{emile_local_ai,
  author = {Del Coburn},
  title = {Émile-1: Personal Local AI Assistant},
  year = {2025},
  institution = {University of Toronto},
  url = {https://github.com/Baglecake/Emile-1}
}
```

---

## 👨‍💻 Author

**Del Coburn**  
University of Toronto  
📧 del.coburn@mail.utoronto.ca  

*For project-related questions, please use GitHub Issues or Discussions. For other inquiries, feel free to reach out via email.*

### **Acknowledgments**
- [Ollama](https://ollama.ai) for democratizing local AI model deployment
- [Streamlit](https://streamlit.io) for the excellent web application framework  
- The open-source AI community for inspiration and foundational models
- University of Toronto for supporting open research initiatives

---

**Made with ❤️ for democratizing AI access**

*Émile runs completely locally - your conversations and files never leave your machine.*

**Version**: v1.1 | **Last Updated**: 2025-07-29 | **Compatibility**: Ollama 0.1+, Streamlit 1.28+
