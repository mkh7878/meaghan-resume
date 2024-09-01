# Resume Chatbot

This repository contains a Flask-based application that serves as a chatbot for answering questions about my resume. The application utilizes the OpenAI API, integrated through the LangChain framework, to provide contextually appropriate responses to user queries based on the resume content.

## Features

- **Resume-based Question Answering**: The chatbot can answer specific questions related to Meaghan's resume, providing detailed and relevant information.
- **Customizable Prompt Template**: The prompt template used for generating responses is tailored to ensure that answers are insightful and aligned with the context provided by the resume.
- **Error Handling**: The application handles cases where no question is provided, ensuring a smooth user experience.

## Getting Started

### Prerequisites

- Python 3.7+
- [Flask](https://flask.palletsprojects.com/)
- [LangChain](https://github.com/hwchase17/langchain)
- An OpenAI API key

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/resume-chatbot.git
    cd resume-chatbot
    ```

2. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your OpenAI API key:**

    Ensure that your OpenAI API key is stored in an environment variable named `OPENAI_API_KEY`.

    ```bash
    export OPENAI_API_KEY='your-api-key-here'
    ```

4. **Add your resume:**

    Place your resume text in a file named `resume.txt` in the root directory of the project.

### Running the Application

To start the Flask application, run the following command:

```bash
python main.py
