# AI Prompt Generator

A sophisticated multi-agent system that transforms simple instructions into detailed, production-ready prompts. This tool leverages GPT-4 and a pydantic-ai agent architecture to generate structured prompts with XML tags, quality guidelines, and execution steps.

## 🌟 Features

- **Intelligent Prompt Generation**: Transforms simple intentions into comprehensive prompts
- **Structured Output**: Generates prompts with XML tags for clear input/output handling
- **Real-time Streaming**: Watch the prompt generation process in real-time
- **Multi-step Validation**: Ensures quality and completeness of generated prompts
- **Flexible Use Cases**: Works for content creation, analysis, and more
- **User-friendly Interface**: Built with Streamlit for easy interaction

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-prompt-generator.git
cd ai-prompt-generator
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
streamlit run app.py
```

## 💻 Requirements

- Python 3.9+
- OpenAI API key
- See requirements.txt for complete package list

## 🛠️ Technical Architecture

The system consists of several key components:

1. **Input Processing Agent**
   - Analyzes user intent
   - Determines required prompt structure
   - Validates input requirements

2. **Prompt Generation Agent**
   - Creates structured prompts
   - Implements XML tagging
   - Ensures format consistency

3. **Quality Control Agent**
   - Validates generated prompts
   - Checks for completeness
   - Ensures clarity and usability

## 📊 Usage Example

1. Enter your OpenAI API key in the sidebar
2. Input your prompt intention (e.g., "write an article")
3. Optionally add examples
4. Click "Generate Prompt"
5. Watch as the system generates a structured prompt
6. Download the generated prompt as needed

## 🔑 Configuration

Key configuration options are available through environment variables:

```env
OPENAI_API_KEY=your_api_key
MODEL_NAME=gpt-4
TEMPERATURE=0.7
```

## 📝 Output Format

Generated prompts follow this structure:
```
You are [role]

[task description]

Required Inputs:
[XML-tagged input structure]

Instructions:
[step-by-step process]

Output Format:
[expected output structure]

Quality Guidelines:
[quality checks]

Restrictions:
[constraints]
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request

## 📜 License

MIT License - feel free to use this project for any purpose.

## 🙏 Acknowledgments

- OpenAI for GPT-4
- Streamlit team for the amazing framework
- Pydantic team for robust data validation