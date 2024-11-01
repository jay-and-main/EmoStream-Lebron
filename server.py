from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for the data (use a database for production)
emoji_data = []

@app.route('/api/emoji', methods=['POST'])
def receive_emoji():
    data = request.get_json()

    # Check if required fields are present
    if not all(key in data for key in ("user_id", "emoji_type", "timestamp")):
        return jsonify({"error": "Missing required fields"}), 400

    # Extract data
    user_id = data["user_id"]
    emoji_type = data["emoji_type"]
    timestamp = data["timestamp"]

    # Save the data
    emoji_data.append({
        "user_id": user_id,
        "emoji_type": emoji_type,
        "timestamp": timestamp
    })
    print(emoji_data)

    return jsonify({"message": "Emoji data received", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=True)
