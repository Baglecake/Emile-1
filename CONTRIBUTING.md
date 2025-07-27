# Contributing to Émile-1

Thank you for your interest in contributing to Émile-1! We welcome all contributions that help democratize AI access and improve the user experience.

## 🎯 Project Goals

- **Democratize AI**: Make AI accessible to everyone without paywalls or privacy concerns
- **User-Friendly**: Maintain a simple, intuitive interface that anyone can use
- **Local-First**: Ensure everything runs locally with no external dependencies
- **Open Source**: Keep the project transparent and community-driven

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/Emile-1.git
   cd Emile-1
   ```
3. **Set up the development environment**:
   ```bash
   pip install -r requirements_txt.txt
   ```
4. **Run the app** to make sure everything works:
   ```bash
   streamlit run emile_complete_app.py
   ```

## 🛠 Development Guidelines

### Code Style
- Follow PEP 8 for Python code
- Use clear, descriptive variable names
- Add comments for complex logic
- Keep functions focused and small

### UI/UX Principles
- **Simplicity**: Keep the interface clean and uncluttered
- **Accessibility**: Ensure features are easy to discover and use
- **Responsiveness**: Test on different screen sizes
- **Feedback**: Provide clear status messages and error handling

### Testing
- Test with multiple Ollama models
- Verify file upload functionality with different file types
- Ensure chat saving/loading works correctly
- Test error scenarios (Ollama not running, invalid files, etc.)

## 🌟 Contribution Ideas

### High Priority
- **PDF Support**: Enable PDF file uploads for document analysis
- **Dark Mode**: Add theme toggle for better user experience
- **Better Error Handling**: More informative error messages
- **Performance Metrics**: Show response times and token counts

### Medium Priority
- **System Prompts**: Allow users to customize the AI's behavior
- **Conversation Search**: Search through saved chat history
- **Model Comparison**: Side-by-side comparison of different models
- **Export Options**: Export chats to different formats (PDF, Word, etc.)

### Nice to Have
- **Voice Input**: Speech-to-text integration
- **Plugin System**: Extensible architecture for custom features
- **Multi-language**: Support for non-English interfaces
- **Mobile App**: React Native or Flutter companion app

## 📝 Submitting Changes

### Pull Request Process

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** and commit with clear messages:
   ```bash
   git commit -m "Add: PDF upload support for document analysis"
   ```

3. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

4. **Open a Pull Request** with:
   - Clear title describing the change
   - Detailed description of what was added/fixed
   - Screenshots for UI changes
   - Testing instructions

### Commit Message Format
```
Type: Brief description (50 chars max)

Detailed explanation if needed
- Bullet points for multiple changes
- Reference issues with #123

Closes #123
```

**Types**: `Add`, `Fix`, `Update`, `Remove`, `Refactor`, `Doc`

## 🐛 Reporting Issues

### Bug Reports
Include:
- **Steps to reproduce** the issue
- **Expected behavior** vs actual behavior
- **Environment**: OS, Python version, Ollama version
- **Error messages** or screenshots
- **Installed models** (`ollama list` output)

### Feature Requests
Include:
- **Problem description**: What pain point does this solve?
- **Proposed solution**: How should it work?
- **Alternatives considered**: Other approaches you thought about
- **Use cases**: When would this be helpful?

## 🏷 Labels and Project Management

We use these labels to organize issues:
- `bug` - Something isn't working correctly
- `enhancement` - New feature or improvement
- `good first issue` - Perfect for new contributors
- `help wanted` - Looking for community input
- `documentation` - Improvements to docs
- `question` - General questions about Émile-1
- `ollama-related` - Issues with Ollama integration
- `ui-improvement` - Streamlit interface enhancements

## 🔒 Security

If you discover a security vulnerability in Émile-1, please email us privately instead of opening a public issue. We'll work with you to address it promptly.

## 📜 Code of Conduct

### Our Standards
- **Be respectful** and inclusive in all interactions
- **Focus on the project** and avoid personal attacks
- **Help others learn** - we're all here to grow
- **Assume good intentions** when reviewing contributions

### Unacceptable Behavior
- Harassment, discrimination, or offensive language
- Spam, trolling, or deliberate disruption
- Sharing private information without permission
- Any behavior that makes others feel unwelcome

## 🎉 Recognition

Contributors will be:
- Listed in the project README
- Mentioned in release notes for significant contributions
- Invited to join the core team for sustained contributions

## ❓ Questions?

- **General questions**: Open a [Discussion](https://github.com/yourusername/Emile-1/discussions)
- **Bug reports**: Create an [Issue](https://github.com/yourusername/Emile-1/issues)
- **Feature ideas**: Start with a Discussion, then create an Issue

Thank you for helping make AI more accessible to everyone! 🚀