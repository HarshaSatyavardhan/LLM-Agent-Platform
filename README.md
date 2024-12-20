# LLM-Agent-Platform

## Overview
The **LLM-Agent-Platform** is a sophisticated system that leverages advanced Large Language Models (LLMs) to create a feedback loop between two agents: 
a *Writer Agent* and a *Critic Agent*. 

This dynamic interaction enables iterative refinement of text, ensuring high-quality outputs through collaborative analysis and improvement.

## Features
- **Seamless Integration**: Quickly set up the platform by connecting API keys from both [Groq](https://groq.com) and OpenAI.
- **Dual-Agent Architecture**:
  - **Writer Agent**: Processes the input text and performs an initial analysis or transformation based on a given prompt.
  - **Critic Agent**: Evaluates the Writer Agent's output, providing constructive feedback for improvement.
  - Feedback loop: The Writer Agent iteratively improves its output based on the Critic Agent's feedback.
- **Final Output Refinement**: The system ensures that the final output is of the highest quality, combining the strengths of both agents.

## How It Works
1. **Setup**:
   - Obtain your API keys:
     - Get a free API key from [Groq](https://groq.com) by navigating to their **Developers** section and selecting **Free API Key**.
     - Acquire an OpenAI API key from [OpenAI](https://openai.com/api/).
   - Attach the API keys to the application to enable functionality.

2. **Agents in Action**:
   - **Writer Agent**:
     - Takes an input text and processes it according to a predefined system prompt.
     - Generates an initial output based on the task.
   - **Critic Agent**:
     - Analyzes the Writer Agent’s output.
     - Provides detailed constructive feedback for refinement.
   - **Feedback Loop**:
     - The Writer Agent incorporates the feedback to improve the output iteratively.
   - **Final Output**:
     - After completing the feedback loop, the Writer Agent delivers the final polished result.

3. **Agent Workflow**:
   - Input text → Writer Agent → Critic Agent → Writer Agent → Final Output

## Example Use Cases
- **Content Creation**: Drafting and refining articles, blog posts, or creative writing.
- **Code Analysis**: Reviewing and refining code snippets or programming logic.
- **Data Summarization**: Generating and iteratively improving summaries for large datasets or documents.
- **Language Translation**: Ensuring accurate and contextually relevant translations through iterative improvement.

## Benefits
- **Improved Output Quality**: The feedback loop ensures continuous refinement of the text.
- **Customizable Prompts**: Tailor system prompts for both Writer and Critic Agents to suit specific tasks or domains.
- **Collaboration Simulated**: Mimics human collaboration to enhance the quality of work.

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/LLM-Agent-Platform.git
   cd LLM-Agent-Platform
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the API keys:
   - Add your Groq API key and OpenAI API key to the configuration file or environment variables.
4. Run the application:
   ```bash
   python main.py
   ```
5. Input your text and watch the Writer and Critic Agents in action!

## Contributing
We welcome contributions to the LLM-Agent-Platform! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For questions or support, please contact [mail](mailto:vasamsettiharsha@gmail.com).

---

Unlock the potential of collaborative LLM agents with the LLM-Agent-Platform. Perfect for refining any form of text through iterative analysis and constructive feedback. Try it today and see the difference!

