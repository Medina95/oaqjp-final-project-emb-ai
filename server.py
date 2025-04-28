''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")

def emotion_analyzer():
    """
    Analiza el texto recibido y devuelve las puntuaciones 
    de las emociones y la emoción dominante.
    Retorna:
        str: Resumen con las emociones y la emoción dominante.
    """
    # Recupera el texto a analizar de los argumentos de la solicitud
    text_to_analyze = request.args.get('textToAnalyze')

    # Pasa el texto a la función emotion_detector y almacena la respuesta
    response = emotion_detector(text_to_analyze)

    # Extraemos todos lo campos
    anger_score = response["anger"]
    disgust_score = response["disgust"]
    fear_score = response["fear"]
    joy_score = response["joy"]
    sadness_score = response["sadness"]

    # Encuentra la emoción dominante
    dominant_emotion = response["dominant_emotion"]

    result_text = (
    f"Para la declaración dada, la respuesta del sistema es 'anger': {anger_score}, "
    f"'disgust': {disgust_score}, 'fear': {fear_score}, 'joy': {joy_score} y "
    f"'sadness': {sadness_score}. La emoción dominante es {dominant_emotion}."
    )


    if dominant_emotion is None:
        return "¡Texto inválido! ¡Por favor, intenta de nuevo!"
    return result_text


@app.route("/")
def render_index_page():
    """
    Renderiza la página de inicio "index.html".
    Retorna:
        Response: La página HTML renderizada.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
