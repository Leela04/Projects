import tkinter as tk
from tkinter import messagebox
from pytube import YouTube
import os

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("400x200")
        
        # URL Entry
        self.url_label = tk.Label(root, text="YouTube URL:", font=("Helvetica", 12))
        self.url_label.pack(pady=10)
        
        self.url_entry = tk.Entry(root, width=50, font=("Helvetica", 12))
        self.url_entry.pack(pady=5)
        
        # Download Button
        self.download_button = tk.Button(root, text="Download", command=self.download_video, font=("Helvetica", 12))
        self.download_button.pack(pady=10)
        
        # Status Label
        self.status_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.status_label.pack(pady=10)
        
    def download_video(self):
        url = self.url_entry.get()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL.")
            return

        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            self.status_label.config(text="Downloading...")
            stream.download()  # Downloads to the current working directory
            self.status_label.config(text="Download completed!")
            messagebox.showinfo("Success", "Download completed!")
        except Exception as e:
            self.status_label.config(text="Failed to download.")
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()
