import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess, threading, os, sys

BASE=os.path.dirname(os.path.abspath(sys.argv[0]))
LOCAL=os.path.join(BASE,"ffmpeg.exe")
FFMPEG=LOCAL if os.path.exists(LOCAL) else "ffmpeg"

def download():
    url=entry.get().strip()
    if not url:
        messagebox.showerror("خطا","لینک m3u8 را وارد کنید."); return
    out=filedialog.asksaveasfilename(defaultextension=".mp4",filetypes=[("MP4","*.mp4")])
    if not out: return
    def run():
        try:
            subprocess.run([FFMPEG,"-i",url,"-c","copy","-y",out],check=True)
            messagebox.showinfo("پایان","دانلود با موفقیت انجام شد.")
        except FileNotFoundError:
            messagebox.showerror("خطا","ffmpeg.exe پیدا نشد.\nآن را کنار برنامه قرار دهید.")
        except Exception as e:
            messagebox.showerror("خطا",str(e))
    threading.Thread(target=run,daemon=True).start()

root=tk.Tk()
root.title("Telewebion Downloader")
tk.Label(root,text="لینک m3u8").pack()
entry=tk.Entry(root,width=80); entry.pack(padx=8,pady=8)
tk.Button(root,text="دانلود",command=download).pack()
root.mainloop()
