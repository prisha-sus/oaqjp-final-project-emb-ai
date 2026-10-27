"""
Emotion Detector Server Application.

This module exposes a Flask web application that provides emotion detection
services using the Watson NLP library package.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/")
def render_index_page():
    """
    Renders the home page of the web application.

    Returns:
        rendered HTML template for the index page.
    """
    return render_template('index.html')


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the input text for emotions and returns a formatted string.

    Returns:
        str: Formatted emotion scores and dominant emotion, or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    