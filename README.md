# 🤖 Émile-1: Your Personal Local AI Assistant

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF6B6B.svg)](https://streamlit.io)
[![Ollama](https://img.shields.io/badge/Powered%20by-Ollama-000000.svg)](https://ollama.ai)
[![University of Toronto](https://img.shields.io/badge/University%20of-Toronto-003F7F.svg)](https://www.utoronto.ca/)
[![Research](https://img.shields.io/badge/Type-Research-brightgreen.svg)](https://github.com)

**v1.0** - *Democratizing AI Access Through Local Computing*

---

A user-friendly Streamlit interface for running AI models locally via Ollama. Chat with AI models completely offline, upload files for context, and manage your conversations - all without any paywalls or privacy concerns!

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

### 📁 **Advanced File Context System**  
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
# Essential Base Model (Recommended for beginners)
ollama pull llama3

# Additional High-Performance Models
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
| `gemma7b` | 5.0GB | General conversation, reasoning, and more complex tasks | 8GB+ |
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

### 📝 Example Conversations

Want to see Émile in action? Check out some saved conversations with different models in our **[examples folder](./Chat_Examples/)**.

These examples showcase the performance trade-offs between larger models that excel at complex reasoning and smaller, more efficient models that are perfect for quick tasks.

## 🛠 Available Models

Émile works with any Ollama-compatible model. Popular choices:

| Model | Size | Best For |
|-------|------|----------|
| `llama3` | 4.7GB | General conversation, reasoning |
| `codellama` | 3.8GB | Code analysis, programming help |
| `mistral` | 4.1GB | Creative writing, analysis |
| `phi3` | 2.3GB | Lightweight, fast responses |

Install models with: `ollama pull <model-name>`

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
- **v1.1** - Planned: PDF support, conversation search, dark mode
- **v1.2** - Planned: Plugin system, custom system prompts, batch processing

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

**Version**: v1.0 | **Last Updated**: 2025-07-27 | **Compatibility**: Ollama 0.1+, Streamlit 1.28+
