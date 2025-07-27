# 🤖 Émile-1: Your Personal Local AI Assistant

A user-friendly Streamlit interface for running AI models locally via Ollama. Chat with AI models completely offline, upload files for context, and manage your conversations - all without any paywalls or privacy concerns!

<img width="2940" height="1592" alt="image" src="https://github.com/user-attachments/assets/dcfeeb48-a1ee-42cf-9206-e3e9ae9ed239" />

## ✨ Features

- 🧠 **Model Selection**: Switch between any locally installed Ollama models
- 📁 **File Context**: Upload text files (`.txt`, `.md`, `.py`, `.js`, `.html`, `.css`, `.json`) for contextual conversations
- 💾 **Chat Management**: Save conversations as timestamped JSON files
- 🔄 **Streaming Responses**: Real-time streaming responses for natural conversation flow
- 🎨 **Clean UI**: Beautiful, intuitive interface built with Streamlit
- 🔒 **Completely Private**: Everything runs locally - no data leaves your machine
- 💰 **Zero Cost**: No API keys, subscriptions, or usage limits

## 🚀 Quick Setup

### Prerequisites
- Python 3.8+
- Ollama installed and running

### 1. Install Ollama
```bash
# macOS/Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows: Download from https://ollama.ai
```

### 2. Download a Model
```bash
# Start with Llama 3 (recommended)
ollama pull llama3

# Or try other models:
ollama pull mistral
ollama pull codellama
ollama pull phi3
```

### 3. Clone and Run Émile
```bash
# Clone the repository
git clone https://github.com/yourusername/Emile-1.git
cd Emile-1

# Install Python dependencies
pip install -r requirements_txt.txt

# Launch Émile
streamlit run emile_complete_app.py
```

### 4. Open Your Browser
Navigate to `http://localhost:8501` and start chatting with Émile!

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

## 🐛 Troubleshooting

### "Cannot connect to Ollama"
- Ensure Ollama is running: `ollama serve`
- Check if models are installed: `ollama list`
- Verify Ollama is accessible on default port (11434)

### "No models found"
- Install at least one model: `ollama pull llama3`
- Restart the Streamlit app after installing new models

### Performance Issues
- Larger models (70B+) require significant RAM
- Try smaller models like `phi3` for faster responses
- Close other applications to free up system resources

## 🎯 Roadmap

- [ ] PDF and document upload support
- [ ] Custom system prompts
- [ ] Conversation search and filtering
- [ ] Model comparison interface
- [ ] Plugin system for extensions
- [ ] Mobile-responsive design
- [ ] Batch file processing

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai) for making local AI accessible
- [Streamlit](https://streamlit.io) for the excellent web framework
- The open-source AI community for inspiration and models

## 💬 Support

- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/yourusername/emile-local-ai/issues)
- **Discussions**: Join the conversation in [GitHub Discussions](https://github.com/yourusername/emile-local-ai/discussions)
  
---

## 👨‍💻 Author
Del Coburn  
University of Toronto  
📧 del.coburn@mail.utoronto.ca  
For project-related questions, please use GitHub Issues or Discussions. For other inquiries, feel free to reach out via email.

---

**Made with ❤️ for democratizing AI access**

*Émile runs completely locally - your conversations and files never leave your machine.*
