from flask import Flask, request, jsonify
import langchain_google_genai
import google.generativeai as genai
from flask_cors import CORS
from dotenv import load_dotenv
import os
from embedding import DocumentEmbedding
from pathlib import Path


class ChatBotApp:
    def __init__(self):
        load_dotenv()
        self.GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key=self.GOOGLE_API_KEY)
        self.model = genai.GenerativeModel("gemini-1.5-pro")
        self.chat = self.model.start_chat(history=[])
        self.chromadb = DocumentEmbedding(persist_directory=Path('chroma/'))
        self.app = Flask(__name__)
        CORS(self.app)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/chat', methods=['POST'])
        def chat_bot():
            data = request.json
            user_message = data.get('messages')

            if not user_message:
                return jsonify({"error": "No message provided"}), 400

            response = self.chat.send_message(content=user_message[0]['content'])
            return jsonify({"response": response.candidates[0].content.parts[0].text}), 200


def create_app():
    chat_bot_app = ChatBotApp()
    return chat_bot_app.app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='127.0.0.1', port=5000)
