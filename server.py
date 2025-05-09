from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os

# Load ASCII frames from "frames" directory
frames = []
for filename in sorted(os.listdir("frames")):
    if filename.endswith(".txt"):
        with open(f"frames/{filename}", "r", encoding="utf-8") as f:
            frames.append(f.read())

class AsciiHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Only serve the animation for a specific path
        if self.path == "/my-project":
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()

            try:
                # Stream frames endlessly
                while True:
                    for frame in frames:
                        self.wfile.write(b"\x1b[2J\x1b[H")  # Clear terminal
                        self.wfile.write(frame.encode("utf-8"))
                        self.wfile.flush()
                        time.sleep(0.3)  # Change speed here
            except BrokenPipeError:
                # Happens when user cancels with Ctrl+C
                pass
        else:
            self.send_response(404)
            self.end_headers()

# Start HTTP server
if __name__ == "__main__":
    PORT = 8000
    print(f"Serving animation at http://localhost:{PORT}/my-project")
    server = HTTPServer(('', PORT), AsciiHandler)
    server.serve_forever()
