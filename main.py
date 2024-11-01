import subprocess
import sys

def main(singer_name, num_videos, duration_of_each_video, output_directory, email):
    try:
        download_command = [
            'python', '102218034.py', singer_name, str(num_videos), str(duration_of_each_video), output_directory
        ]
        subprocess.run(download_command, check=True)

        zip_file_name = "merged_output" if not output_directory.endswith(".zip") else output_directory.replace(".zip", "")
        zip_command = ['python', 'zip.py', output_directory, zip_file_name]
        subprocess.run(zip_command, check=True)

        email_command = ['python', 'sendToEmail.py', f"{output_directory}/{zip_file_name}.zip", email]
        subprocess.run(email_command, check=True)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 6:
        print("Usage: python main.py <singer_name> <num_videos> <duration_of_each_video> <output_directory> <email>")
        sys.exit(1)

    singer_name = sys.argv[1]
    num_videos = int(sys.argv[2])
    duration_of_each_video = int(sys.argv[3])
    output_directory = sys.argv[4]
    email = sys.argv[5]

    main(singer_name, num_videos, duration_of_each_video, output_directory, email)
