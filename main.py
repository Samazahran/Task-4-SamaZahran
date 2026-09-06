import os
from groq import Groq
from rich.console import Console
from rich.markdown import Markdown


# Load the Groq API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

client = Groq(api_key=api_key)
console = Console()


# Ask the user which code file they want to review
file_path = input("Enter the path of the code file you want to review: ")


# Supported file types
supported_extensions = [".py", ".js", ".java"]

file_extension = os.path.splitext(file_path)[1].lower()


if file_extension not in supported_extensions:
    print("\nUnsupported file type.")
    print("Please use a .py, .js, or .java file.")

else:
    try:
        # Read the source code as a string
        with open(file_path, "r", encoding="utf-8") as file:
            source_code = file.read()

        print("\nCode file loaded successfully!")
        print("File:", file_path)

        print("\n--- Source Code ---\n")
        print(source_code)

        # Send the source code to Groq for analysis
        print("\nAnalyzing code... Please wait.")

        system_instructions = """
You are an expert code reviewer.

Analyze the provided source code for bugs, errors, and possible improvements.

Your response must contain exactly these two sections:

## BUG_REPORT
Explain the bugs and problems clearly in plain language.

## REFACTORED_CODE
Provide a corrected and improved version of the code inside a Markdown code block.

Do not include conversational filler outside these sections.
"""


        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": system_instructions,
                },
                {
                    "role": "user",
                    "content": source_code,
                },
            ],
        )


        review = response.choices[0].message.content

        # Validate the AI response structure
        required_sections = [
            "## BUG_REPORT",
            "## REFACTORED_CODE",
        ]

        missing_sections = [
            section for section in required_sections
            if section not in review
        ]

        if missing_sections:
            raise ValueError(
                "AI response is missing required section(s): "
                + ", ".join(missing_sections)
            )

        print("\nAI response format validated successfully!")
        print("\n--- AI Code Review ---\n")

        console.print(Markdown(review))

    except FileNotFoundError:
        print("\nThe file could not be found.")
        print("Please check the file name or path.")

    except PermissionError:
        print("\nPermission denied.")
        print("The program does not have permission to read this file.")

    except UnicodeDecodeError:
        print("\nThe file could not be decoded as UTF-8 text.")

    except Exception as error:
        print("\nAn unexpected error occurred.")
        print("Reason:", error)