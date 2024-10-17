from flask import Flask, render_template, jsonify, request
import asyncio
from RizuNyannewmeup import add_song_to_queue, skip_current_song

app = Flask(__name__)

# Route to serve the HTML page
@app.route('/')
def index():
    return render_template('RizuNyanweb.html')  # Ensure RizuNyanweb.html is in a 'templates' folder

# Route to add a song
@app.route('/add-song', methods=['POST'])
async def add_song():
    data = request.get_json()
    url = data.get('url')
    await add_song_to_queue(url)  # Assuming you have this function in RizuNyannewme.py
    return jsonify({'message': f'Song added to queue: {url}'}), 200

# Route to skip the current song
@app.route('/skip-song', methods=['POST'])
async def skip_song():
    await skip_current_song()  # Assuming you have this function in RizuNyannewme.py
    return jsonify({'message': 'Skipped current song'}), 200

if __name__ == "__main__":
    app.run(debug=True)
