from flask import Flask, send_from_directory

app = Flask(__name__)

# Directory where M3U8 files are stored
M3U8_DIRECTORY = 'm3u8_files'

@apap.route('/m3u8/<filename>', methods=['GET'])
def serve_m3u8_file(filename):
    return send_from_directory(M3U8_DIRECTORY, f"{filename}.m3u8")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)