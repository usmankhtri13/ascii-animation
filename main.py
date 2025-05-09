import os
import time

# Path to the frames directory
frame_dir = "frames"
frames = []

# Read the frames (assumes each frame is a .txt file)
for filename in sorted(os.listdir(frame_dir)):
    if filename.endswith(".txt"):
        with open(os.path.join(frame_dir, filename), "r") as f:
            frames.append(f.read())

def clear_terminal():
    # Clear the terminal screen
    os.system("cls" if os.name == "nt" else "clear")

def display_ascii_animation():
    i = 0
    while True:
        clear_terminal()
        print(frames[i % len(frames)])
        i += 1
        time.sleep(0.3)  # Display the next frame every 300ms

if __name__ == "__main__":
    display_ascii_animation()
