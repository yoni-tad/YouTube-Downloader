# Build by https://github.com/yoni-tad

import os
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox
import yt_dlp

# ---------- CONFIG -----------
DOWNLOAD_FOLDER = "./videos"
VIDEO_FORMAT = 'best[ext=mp4][height<=360]'

# ---------- Ensure download folder exists ----------
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# ---------- GUI App Class ----------
class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Bulk Downloader")

        # Input area
        tk.Label(root, text="Enter YouTube Links (line separated): ").pack()
        self.text_links = tk.Text(root, height=8, width=80)
        self.text_links.pack(padx=10, pady=5)

        # controllers
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        self.start_btn = tk.Button(btn_frame, text="Start Download", command=self.start_download)
        self.start_btn.pack(side=tk.LEFT, padx=5)

        self.stop_btn = tk.Button(btn_frame, text="Stop", command=self.stop_download)
        self.stop_btn.pack(side=tk.LEFT, padx=5)

        # Logs
        tk.Label(root, text="Status / Logs: ").pack()
        self.log_area = scrolledtext.ScrolledText(root, height=15, width=80, state=tk.DISABLED)
        self.log_area.pack(padx=10, pady=5)

        self.stop_flag = False
        self.thread = None

    def log(self, message):
        self.log_area.config(state=tk.NORMAL)
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.see(tk.END)
        self.log_area.config(state=tk.DISABLED)
    
    def start_download(self):
        links_input = self.text_links.get("1.0", tk.END).strip()
        if not links_input:
            messagebox.showwarning("Warning", "Please enter at least one link!")
            return
        
        links = links_input.split()
        if not links:
            messagebox.showwarning("Warning", "No valid links found!")
            return

        self.stop_flag = False
        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.log_area.config(state=tk.NORMAL)
        self.log_area.delete("1.0", tk.END)
        self.log_area.config(state=tk.DISABLED)

        self.thread = threading.Thread(target=self.download_videos, args=(links,))
        self.thread.start()

    def stop_download(self):
        self.stop_flag = True
        self.log("❗️ Stop requested. Will halt after current download.")

    def download_videos(self, links):
        ydl_opts = {
            'format': VIDEO_FORMAT,
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'quiet': True,
        }

        self.log("✅ Download started...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            for idx, link in enumerate(links, 1):
                if self.stop_flag:
                    self.log("🛑 Stopped by user.")
                    break
                self.log(f"🔗 ({idx}/{len(links)}) Downloading: {link}")
                try:
                    ydl.download([link])
                    self.log(f"✅ Finished: {link}")
                except Exception as e:
                    self.log(f"❌ Error with {link}: {e}")
        
        self.log("🎯 All done (or stopped).")
        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()


