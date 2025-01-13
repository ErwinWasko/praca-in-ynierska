from flask import Flask, render_template, jsonify, request
import ollama

app = Flask(__name__)

# Tworzenie klienta Ollama poza funkcjami
client = ollama.Client()
model_name = "llama3.2"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask_chatbot', methods=['POST'])
def ask_chatbot():
    try:
        # Pobierz pytanie z frontendu
        data = request.json
        user_input = data.get('question')

        if not user_input:
            return jsonify({'error': 'Nie podano pytania'}), 400

        print(f"Pytanie od użytkownika: {user_input}")

        # Wysłanie zapytania do modelu Ollama
        response = client.generate(
            model=model_name, 
            prompt=user_input,
            stream=False  # Włączenie trybu pełnej odpowiedzi (bez strumienia)
        )

        # Wyciąganie konkretnej części odpowiedzi
        if 'response' in response:
            bot_response = response['response']
            print(f"Odpowiedź od modelu: {bot_response}")

            # Zwrócenie odpowiedzi w formie JSON
            return jsonify({'answer': bot_response})
        else:
            return jsonify({'error': 'Brak odpowiedzi od modelu'}), 500

    except Exception as e:
        # Debugowanie w razie błędu
        print(f"Błąd podczas przetwarzania zapytania: {str(e)}")
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
