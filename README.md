# Auto DJ Crossfade 🎧

Auto DJ Crossfade is a Python-based desktop application that automatically plays and mixes music files from a selected directory. It features a seamless crossfade effect between tracks, mimicking a real DJ experience.

## ✨ Features

- **Automated Crossfading**: Smoothly transitions between songs by fading out the current track while fading in the next one.
- **Randomized Playlist**: Automatically shuffles songs to create a random playback queue.
- **Simple GUI**: Built with Tkinter for an easy-to-use interface.
- **Support for Common Formats**: Plays `.mp3` and `.wav` files.
- **Real-time Status**: Displays the currently playing song and status.

## 🛠️ Prerequisites

To run this application, you need to have Python installed along with the `pygame` library.

- Python 3.x
- `pygame`

## 📦 Installation

1.  **Clone the repository** (or download the source code):
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install dependencies**:
    ```bash
    pip install pygame
    ```

## 🚀 Usage

1.  **Run the application**:
    ```bash
    python djmixer.py
    ```

2.  **Load Music**:
    - Click on the **"Select Folder"** button.
    - Choose a directory containing your music files (`.mp3` or `.wav`).

3.  **Start Playback**:
    - Click **"▶ Play DJ"** to start the auto-mixing.

4.  **Control**:
    - The DJ loop will automatically handle song transitions.
    - Click **"⏹ Stop"** to halt playback.

## 🏗️ Building Executable

This project includes a `djmixer.spec` file, which means it can be packaged into a standalone executable using `PyInstaller`.

To build the executable yourself:

1.  **Install PyInstaller**:
    ```bash
    pip install pyinstaller
    ```

2.  **Run the build command**:
    ```bash
    pyinstaller djmixer.spec
    ```

3.  **Locate the executable**:
    The generated executable will be found in the `dist` folder.

## 📝 License

This project is open-source and free to use.
