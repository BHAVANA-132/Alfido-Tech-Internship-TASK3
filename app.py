from flask import Flask, request, jsonify
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Create Flask app
app = Flask(__name__)

# Load trained model
model = tf.keras.models.load_model("sentiment_model.keras")

# Load tokenizer
with open("tokenizer.pkl", "rb") as file:
    tokenizer = pickle.load(file)

# Maximum sequence length used during training
MAX_LEN = 200


@app.route("/")
def home():
    return jsonify({
        "message": "Sentiment Analysis API is running!",
        "endpoint": "/predict"
    })


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get JSON data
        data = request.get_json()

        # Check if review is provided
        if not data or "review" not in data:
            return jsonify({
                "error": "Please provide a 'review' field."
            }), 400

        review = data["review"]

        # Convert text to sequence
        sequence = tokenizer.texts_to_sequences([review])

        # Pad sequence
        padded_sequence = pad_sequences(
            sequence,
            maxlen=MAX_LEN,
            padding="post",
            truncating="post"
        )

        # Make prediction
        prediction = model.predict(padded_sequence, verbose=0)[0][0]

        # Determine sentiment
        if prediction >= 0.5:
            sentiment = "Positive"
            confidence = prediction
        else:
            sentiment = "Negative"
            confidence = 1 - prediction

        return jsonify({
            "review": review,
            "sentiment": sentiment,
            "confidence": round(float(confidence) * 100, 2)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)