# Agentic Prompt Rewriter

A sophisticated multi-agent system that transforms simple instructions into detailed, production-ready prompts. This tool leverages GPT-4 and a pydantic-ai agent architecture to generate structured prompts with XML tags, quality guidelines, and execution steps.

# DEMO 

https://github.com/user-attachments/assets/70cd590a-a08f-4a1d-aa63-ae26b7f60bce

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
git clone [https://github.com/yourusername/ai-prompt-generator.git](https://github.com/Croups/agentic-prompt-rewriter)
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
## CONTACT

Reach me out from linkedin : www.linkedin.com/in/enes-koşar

