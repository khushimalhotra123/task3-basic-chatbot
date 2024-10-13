from flask import Flask, render_template, request, jsonify
import spacy

app = Flask(__name__)

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

@app.route('/')
def index():
    return render_template('index4')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    doc = nlp(user_message)

    # Basic intent recognition based on keywords
    if "projects" in user_message.lower():
        response = "I have worked on several projects, including Neural Style Transfer and Diabetes Analysis using Python."
    elif "skills" in user_message.lower():
        response = "I am skilled in Python, AI, Machine Learning, and Cloud technologies like AWS."
    elif "resume" in user_message.lower():
        response = "You can view my resume in the Resume section of this site."
    elif "contact" in user_message.lower():
        response = "You can reach me at example@example.com."
    else:
        response = "I am still learning! You can ask me about my projects, skills, or how to contact me."

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
