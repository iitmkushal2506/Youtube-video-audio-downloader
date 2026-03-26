# 🎬 YouTube Video Downloader (Flask)

A clean and simple **YouTube Video & Audio Downloader** built using **Python Flask** that allows users to fetch and download videos in **MP4 (Best Quality)** or **MP3 (Audio Only)** format.

---

# 👨‍💻 Author

**Kushal Batra**
🎓 IIT Madras BS in Data Science & Applications
🌐 GitHub: [https://github.com/iitmkushal2506](https://github.com/iitmkushal2506)

---

# 🚀 Features

* Fetch YouTube video preview
* Download video in **Best Quality MP4**
* Download **Audio (MP3)**
* Clean and responsive UI
* Fast backend processing using **yt-dlp**
* Automatic file handling
* Local execution support

---

# 🧠 Concepts Used (Detailed Explanation)

## 1. Flask Backend

Flask is a lightweight Python web framework used to create backend servers. In this project, Flask is used to:

* Handle user requests
* Process YouTube URLs
* Fetch video metadata
* Download files
* Serve downloadable content

Key Concepts Used:

### Routing

Flask routes are used to connect URLs with Python functions.

Example:

* `/` → Home Page
* `/download_mp4` → MP4 Download
* `/download_mp3` → MP3 Download

This allows the application to perform different tasks based on user interaction.

---

## 2. yt-dlp Library

`yt-dlp` is a powerful Python library used for downloading videos from YouTube and other platforms.

This project uses yt-dlp to:

* Extract video information
* Download video
* Download audio
* Convert audio to MP3

Why yt-dlp?

* Faster than youtube-dl
* Supports more formats
* Regular updates
* Better quality downloads

---

## 3. Jinja2 Template Rendering

Flask uses **Jinja2 template engine** to dynamically render HTML.

This allows:

* Display video title dynamically
* Display preview dynamically
* Pass backend data to frontend

Example:

```
{{title}}
{{video_id}}
```

These variables come from Flask backend.

---

## 4. Form Handling

HTML form is used to accept user input (YouTube URL).

Steps:

1. User enters URL
2. Form sends POST request
3. Flask receives request
4. Backend processes URL
5. Result shown on page

---

## 5. Video Metadata Extraction

The backend extracts:

* Video title
* Video ID
* Video preview

This is done using **yt-dlp extract_info()** method.

---

## 6. File Handling

Downloaded files are:

* Stored temporarily
* Sent to user
* Downloaded in browser

Flask function used:

```
send_file()
```

---

## 7. Responsive UI Design

Frontend built using:

* HTML
* CSS

Features:

* Responsive layout
* Modern UI
* Clean design

---

# 📁 Project Structure

```
project-folder/
│
├── app.py
├── templates/
│   └── index.html
├── downloads/
└── README.md
```

---

# ⚙️ Requirements

Make sure you have:

* Python 3.8+
* pip installed
* Internet connection

---

# 🖥️ Run Locally (Step-by-Step)

## Step 1: Clone Repository

```
git clone https://github.com/iitmkushal2506/your-repo-name.git
```

---

## Step 2: Go to Project Folder

```
cd your-repo-name
```

---

## Step 3: Install Dependencies

```
pip install flask yt-dlp
```

---

## Step 4: Run Application

```
python app.py
```

---

## Step 5: Open Browser

Go to:

```
http://127.0.0.1:5000
```

---

# ⚠️ Important Note

This project is designed to run **locally only**.

Some hosting platforms block YouTube downloading features due to policy restrictions.

If video preview does not load after fetching:

* Don't worry
* Some videos block embedding
* You can still download video/audio

---

# 🔧 Technologies Used

* Python
* Flask
* yt-dlp
* HTML
* CSS
* Jinja2

---

# 🎯 Learning Outcomes

From this project you will learn:

* Flask backend development
* API handling
* File downloading
* Template rendering
* Python backend logic
* UI design

---

# ⭐ Future Improvements

* Add download progress bar
* Add multiple resolution options
* Add playlist downloader
* Add dark/light mode

---

# 📜 Disclaimer

This project is built for **educational purposes only**.
Users are responsible for complying with YouTube's Terms of Service.

---
