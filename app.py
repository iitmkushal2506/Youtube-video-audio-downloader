from flask import Flask, render_template, request, send_file
import yt_dlp
import os
import re

app = Flask(__name__)

DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


def get_video_id(url):
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, url)
    return match.group(1) if match else None


@app.route("/", methods=["GET", "POST"])
def home():

    url = None
    title = None
    video_id = None

    if request.method == "POST":

        url = request.form.get("url")

        ydl_opts = {
            'quiet': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            info = ydl.extract_info(url, download=False)

            title = info.get("title")
            video_id = get_video_id(url)

    return render_template(
        "index.html",
        url=url,
        title=title,
        video_id=video_id
    )


# MP4 Download (Best Quality)
@app.route("/download_mp4", methods=["POST"])
def download_mp4():

    url = request.form.get("url")

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
        'merge_output_format': 'mp4',
        'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

        filename = os.path.splitext(filename)[0] + ".mp4"

    return send_file(filename, as_attachment=True)


# MP3 Download
@app.route("/download_mp3", methods=["POST"])
def download_mp3():

    url = request.form.get("url")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{DOWNLOAD_FOLDER}/%(title)s.%(ext)s',
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:

        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)

        filename = os.path.splitext(filename)[0] + ".mp3"

    return send_file(filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)