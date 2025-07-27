#!/bin/bash

# Émile Local AI Assistant Setup Script
# This script automates the setup process for new users

set -e

echo "🤖 Setting up Émile - Your Personal Local AI Assistant"
echo "=================================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3.8+ from https://python.org"
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Check if Ollama is installed
if ! command -v ollama &> /dev/null; then
    echo "🔄 Ollama not found. Installing Ollama..."
    
    # Detect OS and install accordingly
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        echo "Installing Ollama for macOS..."
        curl -fsSL https://ollama.ai/install.sh | sh
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        echo "Installing Ollama for Linux..."
        curl -fsSL https://ollama.ai/install.sh | sh
    else
        echo "⚠️  Please install Ollama manually from https://ollama.ai"
        echo "Then run this script again."
        exit 1
    fi
else
    echo "✅ Ollama found: $(ollama --version)"
fi

# Install Python dependencies
echo "🔄 Installing Python dependencies..."
pip3 install -r requirements.txt

# Start Ollama service (if not running)
echo "🔄 Starting Ollama service..."
ollama serve &
sleep 3

# Download default model
echo "🔄 Downloading Llama 3 model (this may take a few minutes)..."
ollama pull llama3

echo ""
echo "🎉 Setup complete!"
echo ""
echo "To start Émile:"
echo "  streamlit run emile_complete_app.py"
echo ""
echo "Then open your browser to: http://localhost:8501"
echo ""
echo "Available commands:"
echo "  ollama list          - See installed models"
echo "  ollama pull <model>  - Download new models"
echo ""
echo "Happy chatting! 🚀"