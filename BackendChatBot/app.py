from flask import Flask, request, jsonify
import langchain_google_genai
import google.generativeai as genai
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")
chat = model.start_chat(history=[])

app = Flask(__name__)
CORS(app)


@app.route('/chat', methods=['POST'])
def chat_bot():
    data = request.json
    user_message = data.get('messages')

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    response = chat.send_message(content=user_message[0]['content'])
    return jsonify({"response": response.candidates[0].content.parts[0].text}), 200


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
