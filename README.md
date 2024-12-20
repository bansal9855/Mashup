# Video Downloader, Audio Merger, and Email Sender

This project automates downloading videos of a specified singer from YouTube, merges them into a single audio file, compresses the result into a zip file, and sends it to a specified email address. The project is divided into separate scripts for downloading, zipping, and sending the file, all coordinated via the `main.py` script.

## Features
1. Downloads specified videos based on the singer's name.
2. Merges video audio into a single audio file.
3. Compresses the merged file into a zip.
4. Sends the zip file as an email attachment.

## Prerequisites
- Python 3.x
- Required Python packages (specified in `requirements.txt`):
  - `youtube_dl` for downloading videos.
  - `pydub` for audio merging.
  - `smtplib` for email functionality.
  - `dotenv` for environment variable management.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bansal9855/Mashup
   cd Mashup
   ```



2. **Set up environment variables**:
   - Create a `.env` file in the root directory:
     ```
     password=your_email_password
     ```
   - Replace `your_email_password` with your actual email password for authentication.

## Project Structure

- `main.py`: Coordinates all functions - downloading videos, zipping the output, and emailing.
- `102218034.py`: Downloads videos based on singer name and duration, and merges them.
- `zip.py`: Compresses the merged audio file.
- `sendToEmail.py`: Sends the compressed zip file via email.

## Usage

Execute the `main.py` script with the following parameters:
```bash
python main.py <singer_name> <num_videos> <duration_of_each_video> <output_directory> <email>
```

### Parameters
- `singer_name`: Name of the singer for video search.
- `num_videos`: Number of videos to download.
- `duration_of_each_video`: Duration in seconds for each video.
- `output_directory`: Directory where the files will be saved.
- `email`: Recipient email address for sending the merged audio file.

### Example Usage
```bash
python main.py "Taylor Swift" 2 30 "downloads" "example@example.com"
```

### Sample Output
```
Downloaded 2 videos for 'Taylor Swift' and created a mashup.
Zipped merged_output.mp3 into downloads\merged_output.zip.
Email sent successfully with attachment!
Zip file downloads\merged_output.zip sent to example@example.com.
```

## Example Input/Output

1. **Input**:
   ```bash
   python main.py "Ed Sheeran" 3 45 "downloads" "test@example.com"
   ```

2. **Output**:
   ```
   Downloaded 3 videos for 'Ed Sheeran' and created a mashup.
   Zipped merged_output.mp3 into downloads\merged_output.zip.
   Email sent successfully with attachment!
   Zip file downloads\merged_output.zip sent to test@example.com.
   ```

## Notes

- Make sure to enable **Less Secure App Access** for the sender's email to allow sending emails through Python.
- The merged file is saved as `merged_output.mp3` in the specified output folder and is zipped before being emailed.
- Ensure `ffmpeg` is installed for audio processing.

## Troubleshooting

- If you encounter issues with encoding, verify that your system and file paths support Unicode characters.
- Make sure environment variables are properly configured for secure email access.




