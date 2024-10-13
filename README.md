Personal Portfolio with Chatbot

This is a personal portfolio website designed to showcase my skills, projects, and experience. The website also includes an interactive text-based chatbot that can hold basic conversations using natural language processing (NLP).

Features

    •    Portfolio Sections:
    •    About Me: Information about my background, skills, and experience.
    •    Projects: A list of the projects I’ve worked on, with brief descriptions.
    •    Contact: My email and phone number.
    •    Chatbot:
    •    The chatbot can respond to simple queries and provide information about me and my work.
    •    It is built using Python’s NLTK library and served via a Flask backend.

Technologies Used

    •    Frontend:
    •    HTML for the structure of the website.
    •    CSS for styling the website.
    •    JavaScript for handling chatbot interactions on the client side.
    •    Backend:
    •    Python with Flask for serving the chatbot responses.
    •    NLTK for implementing the chatbot logic using pattern matching and reflection techniques.

Getting Started

Prerequisites

Before running this project, ensure you have the following installed on your machine:

    •    Python 3.x
    •    Flask
    •    NLTK

Installation

    1.    Clone the Repository:
Clone this project to your local machine using:

git clone https://github.com/yourusername/portfolio-chatbot.git
cd portfolio-chatbot


    2.    Install Dependencies:
Install the required Python libraries using pip:

pip install -r requirements.txt


    3.    Download NLTK Data:
In case NLTK data is not installed, run the following in a Python environment:

import nltk
nltk.download('punkt')



Running the Chatbot Server

To run the chatbot server, navigate to the project directory and run the following command:

python chatbot.py

This will start a Flask server at http://127.0.0.1:5000/.

Accessing the Website

    1.    Open the index.html file in your browser.
    2.    You can now explore the portfolio sections and interact with the chatbot under the “Chat with Me” section.

Using the Chatbot

    •    You can type messages in the chatbot input box and click “Send” to receive responses.
    •    The chatbot can answer basic questions like:
    •    “What is your name?”
    •    “Tell me about your projects.”
    •    “Goodbye” to end the conversation.

Project Structure

    •    index.html: The main structure of the portfolio website.
    •    style.css: Styling for the website.
    •    script.js: Handles chatbot interaction logic on the frontend.
    •    chatbot.py: Backend server and chatbot logic using NLTK and Flask.
    •    requirements.txt: List of Python dependencies for the project.
    •    README.md: Instructions for setting up and running the project.

Future Enhancements

    •    Improve the chatbot’s conversational ability by integrating advanced NLP models like spaCy or GPT-based APIs.
    •    Add more projects and an interactive portfolio design.
    •    Deploy the website and chatbot to a live server.

License

This project is open-source and available under the MIT license.