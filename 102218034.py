import yt_dlp
import sys
import os
import subprocess
import ffmpeg
def download_videos(singer_name, num_videos, save_path='./downloads'):
    if not os.path.exists(save_path):
        try:
            os.makedirs(save_path)
            print(f"Directory '{save_path}' created.")
        except OSError as e:
            print(f"Error creating directory {save_path}: {e}")
            sys.exit(1)

    search_url = f"ytsearch{num_videos}:{singer_name}"

    ydl_opts = {
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',  
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  
        'noplaylist': True,                          
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_url]) 
        
def convert_to_audio(video_path,audio_format='mp3'):
    audio_output=f"{os.path.splitext(video_path)[0]}.{audio_format}"
    try:
        subprocess.run(['ffmpeg','-i',video_path,'-q:a','0','-map','a',audio_output],check=True)
        print(f"converted '{video_path}' to '{audio_output}'")
        return audio_output
    except subprocess.CalledProcessError as e:
        print(f"Error converting {video_path} : {e}")    

def trim_audio(input_audio, output_audio, duration):
    try:
        (
            ffmpeg
            .input(input_audio, t=duration)  
            .output(output_audio)            
            .run(overwrite_output=True)      
        )
        print(f"Trimmed audio to {duration} seconds: '{output_audio}'")
    except ffmpeg.Error as e:
        print(f"Error trimming audio {input_audio}: {e}")
        
def merge_audios(audio_files, output_file):
    with open("filelist.txt", 'w',encoding='utf-8') as f:
        for audio in audio_files:
            f.write(f"file '{audio}'\n")

    try:
        subprocess.run(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'filelist.txt', '-c', 'copy', output_file], check=True)
        print(f"Merged audio files into '{output_file}'")
    except subprocess.CalledProcessError as e:
        print(f"Error merging audio files: {e}")       

if len(sys.argv) < 5:
    print("Usage: python script_name.py <singer_name> <num_videos> <duration_of_each_video> <output_directory>")
    sys.exit(1)

if __name__ == "__main__":
    singer_name = sys.argv[1]
    num_videos = int(sys.argv[2])
    Y=int(sys.argv[3])
    output_directory = sys.argv[4]
   
    download_videos(singer_name, num_videos, output_directory)

    audio_files=[]
    
    for video_file in os.listdir(output_directory):
        if video_file.endswith(('.mp4','.mpv','.webm')):
            video_path=os.path.join(output_directory,video_file)
            audio_path=convert_to_audio(video_path,'mp3')
            
            if audio_path:
                trimmed_audio_path = os.path.join(output_directory, f"trimmed_{os.path.basename(audio_path)}")
                trim_audio(audio_path, trimmed_audio_path, Y)
                audio_files.append(trimmed_audio_path)
        
        
    merge_audio_file=os.path.join(output_directory,'merged_output.mp3')
    merge_audios(audio_files,merge_audio_file)        