from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Specify the absolute path to the folder containing your external images
external_folder_path = "/Users/coder/saves"  # Replace with your actual path

@app.route("/")
def home():
	return "parked"

@app.route("/images/<filename>")
def serve_image(filename):
    # Construct the absolute path to the image file
    image_path = os.path.join(external_folder_path, filename)

    # Check if the file exists
    if not os.path.exists(image_path):
        return "Image not found."

    # Serve the image file
    return send_from_directory(external_folder_path, filename)


@app.route("/image_gallery")
def image_gallery():
    # List of image filenames in the external folder
    image_files = [
        f
        for f in os.listdir(external_folder_path)
        if f.endswith((".jpg", ".png", ".gif"))
    ]

    return render_template("image_gallery.html", image_files=image_files)


@app.route("/read/<text>")
def nanny(text):
    return f"""lemme read you a bed time story kid
  once upon a time,
  {escape(text)}"""


@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory("static", filename)


if __name__ == "__main__":
    app.run(debug=True)
