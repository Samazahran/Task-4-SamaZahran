# Intelligent Code Reviewer & Explainer

An AI-powered code review tool that analyzes source code, identifies bugs and potential improvements, and generates a cleaner refactored version.

The project uses the Groq API to perform code analysis and Rich to display structured Markdown output directly in the terminal.

## Features

- Reviews Python, JavaScript, and Java files
- Detects bugs, logical issues, and possible improvements
- Generates a clear bug report in plain language
- Produces corrected and refactored code
- Validates the structure of the AI response
- Displays Markdown and code blocks with terminal syntax highlighting
- Handles unsupported files and common file-reading errors

## Technologies Used

- Python
- Groq API
- Rich
- Large Language Models (LLMs)

## Installation

Install the required dependencies:

```bash
pip3 install -r requirements.txt
```

## API Key Setup

Create a Groq API key and store it as an environment variable:

```bash
export GROQ_API_KEY="your_api_key_here"
```

Do not place your API key directly inside the Python source code.

## Usage

Run the application:

```bash
python3 main.py
```

When prompted, enter the path of the source code file you want to review:

```text
Enter the path of the code file you want to review: sample_code.py
```

The application supports:

- `.py`
- `.js`
- `.java`

## Example Output

The AI response is organized into two main sections:

```text
BUG_REPORT
Identifies bugs, errors, and possible improvements.

REFACTORED_CODE
Provides an improved version of the submitted source code.
```

A sample buggy source file is included in the repository for testing the reviewer.

## Project Structure

```text
main.py
sample_code.py
README.md
requirements.txt
```

## Notes

A valid Groq API key and internet connection are required to generate AI code reviews.
