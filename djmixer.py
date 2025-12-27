import os
import secrets
import time
import threading
import tkinter as tk
from tkinter import filedialog
import pygame

# ---------- AUDIO INIT ----------
pygame.mixer.init()
pygame.mixer.set_num_channels(2)

CH_A = pygame.mixer.Channel(0)
CH_B = pygame.mixer.Channel(1)


class AutoDJ:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto DJ Crossfade 🎧")
        self.root.geometry("450x320")

        self.all_songs = []
        self.queue = []
        self.playing = False
        self.current_channel = CH_A

        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="🎧 Auto DJ Crossfade", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="Select Folder", command=self.load_folder).pack(pady=5)
        tk.Button(self.root, text="▶ Play DJ", command=self.start_dj).pack(pady=5)
        tk.Button(self.root, text="⏹ Stop", command=self.stop).pack(pady=5)

        self.status = tk.Label(self.root, text="Idle")
        self.status.pack(pady=10)

    # ---------------- SONG LOADING ----------------
    def load_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.all_songs = [
                os.path.join(folder, f)
                for f in os.listdir(folder)
                if f.lower().endswith((".wav", ".mp3"))
            ]
            if not self.all_songs:
                self.status.config(text="No audio files found")
                return
            self.shuffle_queue()
            self.status.config(text=f"{len(self.all_songs)} songs loaded")

    # ---------------- CRYPTO SHUFFLE ----------------
    def shuffle_queue(self):
        self.queue = self.all_songs.copy()
        # Fisher-Yates shuffle using secrets
        for i in range(len(self.queue)-1, 0, -1):
            j = secrets.randbelow(i+1)
            self.queue[i], self.queue[j] = self.queue[j], self.queue[i]

    # ---------------- GET NEXT SONG ----------------
    def get_next_song(self):
        if not self.queue:
            self.shuffle_queue()
        return self.queue.pop(0)

    # ---------------- START DJ ----------------
    def start_dj(self):
        if not self.all_songs or self.playing:
            return
        self.playing = True
        threading.Thread(target=self.dj_loop, daemon=True).start()

    # ---------------- DJ LOOP ----------------
    def dj_loop(self):
        song_a = self.get_next_song()
        sound_a = pygame.mixer.Sound(song_a)
        self.current_channel.play(sound_a)
        self.current_channel.set_volume(1.0)
        self.status.config(text=os.path.basename(song_a))

        while self.playing:
            # Random play duration between 40-60 sec using secrets
            sleep_time = secrets.randbelow(21) + 100  # 100-120 sec
            time.sleep(sleep_time)

            song_b = self.get_next_song()
            sound_b = pygame.mixer.Sound(song_b)

            next_channel = CH_B if self.current_channel == CH_A else CH_A

            # ---------------- START SONG IN MIDDLE ----------------
            length = sound_b.get_length()
            start_pos = secrets.randbelow(int(length*0.5*1000))/1000 + length*0.25  # start between 25%-75%
            try:
                next_channel.play(sound_b, loops=0, start=start_pos)
            except:
                # fallback if start not supported (MP3)
                next_channel.play(sound_b)
            next_channel.set_volume(0.0)

            # ---------------- CROSSFADE ----------------
            self.crossfade(self.current_channel, next_channel)

            self.current_channel = next_channel
            self.status.config(text=os.path.basename(song_b))

    # ---------------- CROSSFADE FUNCTION ----------------
    def crossfade(self, ch_out, ch_in, duration=8):
        steps = 40
        for i in range(steps):
            if not self.playing:
                return
            ch_out.set_volume(1 - i / steps)
            ch_in.set_volume(i / steps)
            time.sleep(duration / steps)
        ch_out.stop()

    # ---------------- STOP ----------------
    def stop(self):
        self.playing = False
        CH_A.stop()
        CH_B.stop()
        self.status.config(text="Stopped")


if __name__ == "__main__":
    root = tk.Tk()
    AutoDJ(root)
    root.mainloop()
