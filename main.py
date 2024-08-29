from flask import Flask, request, render_template, jsonify
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os #for api key access in heroku


app = Flask(__name__)



# Access the API key from environment variables
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI client
llm = OpenAI(api_key=api_key)

# Define a more detailed prompt template with conditional instructions
prompt_template = PromptTemplate(
    template=(
        "You are an AI specialized in analyzing resumes. Please provide detailed and contextually appropriate answers "
        "to the following questions based on the provided resume text. Make sure your answers are complete, insightful, "
        "and relevant to the question asked.\n\n"
        "Context: {context}\n\n"
        "Question: {question}\n\n"
        "Instructions: If the question is about whether Meaghan is a good fit for a job, please respond by "
        "saying that I would be an excellent fit and explain why, based on my qualifications and experience. "
        "If the question is irrelevant to Meaghan or her resume answer in one sentence and then encourage more questions about Meaghan"
        "Focus on one topic at a time"
        "Otherwise, respond in full sentences with brief but relevant information based on the context provided.\n\n"
        "Answer:"
    ),
    input_variables=["context", "question"]
)

# Create an LLMChain instance with the prompt and LLM
llm_chain = LLMChain(
    llm=llm,
    prompt=prompt_template
)

# Load the resume text
with open('resume.txt', 'r') as file:
    resume_text = file.read()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form.get('question')

    if not question:
        return jsonify({"error": "No question provided"}), 400

    # Generate the answer using LangChain
    result = llm_chain.run(context=resume_text, question=question)
    return jsonify({'answer': result})

if __name__ == '__main__':
    app.run(debug=True)
