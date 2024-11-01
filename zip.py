import os
import sys
import zipfile

def zip_videos(input_folder, output_file):
    merged_filename = "merged_output.mp3"  
    merged_video_path = os.path.join(input_folder, merged_filename)

    try:
        if os.path.isfile(merged_video_path):
            output_zip_file = os.path.join(input_folder, f"{output_file}.zip")
            with zipfile.ZipFile(output_zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(merged_video_path, arcname=merged_filename)
                print(f"Zipped {merged_filename} into {output_zip_file}.")
        else:
            print(f"The merged video file '{merged_filename}' does not exist in the input folder.")

    except Exception as e:
        print(f"An error occurred while zipping the video: {e}")

if len(sys.argv) < 3:
    print("Usage: python script_name.py <input_folder> <output_file>")
    sys.exit(1)

input_folder = sys.argv[1]
output_file = sys.argv[2]

zip_videos(input_folder, output_file)
