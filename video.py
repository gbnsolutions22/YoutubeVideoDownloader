from flask import Flask, render_template, request, send_file
from pytube import YouTube

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['video_url']
    yt = YouTube(video_url)
    stream = yt.streams.get_highest_resolution()
    filename = f'{yt.title}.mp4'
    stream.download('./downloads/', filename)
    return send_file('./downloads/' + filename, as_attachment=True)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
