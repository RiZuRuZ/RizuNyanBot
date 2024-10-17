from flask import Flask, render_template, jsonify, request
import asyncio
from RizuNyannewmeup import add_song_to_queue, skip_current_song

app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('RizuNyanweb.html')  # Ensure RizuNyanweb.html is in a 'templates' folder

# Function to run async functions from Flask routes
def run_async(coro):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(coro)
    loop.close()
    return result

# Route to add a song
@app.route('/add-song', methods=['POST'])
def add_song():
    data = request.get_json()
    print(data)
    url = data.get('url')
    try:
        run_async(add_song_to_queue(url))  # Run the async function synchronously
        return jsonify({'message': f'Song added to queue: {url}'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to skip the current song
@app.route('/skip-song', methods=['POST'])
def skip_song():
    try:
        run_async(skip_current_song())  # Run the async function synchronously
        return jsonify({'message': 'Skipped current song'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)
    print(app.url_map)
