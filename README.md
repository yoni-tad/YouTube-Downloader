# YouTube Video Downloader (GUI)

This is a simple Python desktop application with a GUI for downloading multiple YouTube videos at once.

It started as a personal project when my father asked me to download many videos for him. Instead of doing it manually one by one, I decided to build a small app that can handle a list of links at once.

---

## ✅ Features

- Easy-to-use desktop GUI (Tkinter)
- Paste multiple YouTube links at once (one per line)
- Choose download folder
- Downloads videos automatically in 360p MP4 (small file size)
- Shows real-time progress in the app
- Start/Stop buttons to control downloading

---

## 📸 Screenshot

![image](https://github.com/user-attachments/assets/574d45b1-d1d5-4ec1-96c8-569ebb7d97d3)


---

## ⚙️ How to Run the App (for Developers)

You can run it directly with Python if you want to test or improve it.

### 1. Clone the repo

```bash
git clone https://github.com/yoni-tad/YouTube-Downloader.git
cd YouTube-Downloader
```

### 2. Install requirements

```bash
pip install yt-dlp
pip install tkinter
pip install auto-py-to-exe
```

### 3. Run it

```bash
python index.py
```
---

## 💻 Building an .exe (for Windows)
If you want to make a standalone .exe so others can use it without installing Python:

```bash
auto-py-to-exe
```
- Choose your script (main.py)
- Select Onefile
- Add an icon if you want
- Click Convert .py to .exe

✅ The output .exe can be shared and run on any Windows machine (no need for Python).

---

## 🤝 Contributing
Feel free to fork and improve it. Pull requests welcome!

## 📜 License
MIT License (or whichever you choose)
