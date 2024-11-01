from flask import Flask, render_template, request, redirect, url_for, flash
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    print(f"Request method: {request.method}")  # Debug line to confirm request method
    singer_name = request.form['singer_name']
    num_videos = request.form['num_videos']
    duration = request.form['duration']
    email = request.form['email']

    if not singer_name or not num_videos.isdigit() or not duration.isdigit() or not email:
        flash("Please fill out all fields correctly.", "error")
        return redirect(url_for('form'))

    try:
        subprocess.run(['python', 'main.py', singer_name, num_videos, duration, 'output_folder', email], check=True)
        flash("Videos downloaded, zipped, and emailed successfully!", "success")
    except subprocess.CalledProcessError as e:
        flash(f"An error occurred during processing: {e}", "error")
    except Exception as e:
        flash(f"An unexpected error occurred: {e}", "error")

    return redirect(url_for('form'))

if __name__ == '__main__':
    app.run(debug=True)
