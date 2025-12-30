import subprocess
import os

def extract_audio(input_video, output_audio, audio_format='mp3'):
    cmd = [
        'ffmpeg',
        '-i', input_video,
        '-vn',
        '-acodec', 'libmp3lame' if audio_format == 'mp3' else 'aac',
        '-y',
        output_audio
    ]
    subprocess.run(cmd, check=True)
    print(f"Audio extracted: {output_audio}")

def compress_video(input_video, output_video, crf=28, preset='medium'):
    cmd = [
        'ffmpeg',
        '-i', input_video,
        '-vcodec', 'libx264',
        '-crf', str(crf),
        '-preset', preset,
        '-acodec', 'aac',
        '-y',
        output_video
    ]
    subprocess.run(cmd, check=True)
    print(f"Video compressed: {output_video}")

def convert_video(input_video, output_video, target_format='mp4'):
    cmd = [
        'ffmpeg',
        '-i', input_video,
        '-c:v', 'libx264',
        '-c:a', 'aac',
        '-y',
        output_video
    ]
    subprocess.run(cmd, check=True)
    print(f"Video converted to {target_format}: {output_video}")

def video_to_gif(input_video, output_gif, start_time=None, duration=None, scale_width=320):
    cmd = ['ffmpeg', '-i', input_video]
    if start_time:
        cmd.extend(['-ss', start_time])
    if duration:
        cmd.extend(['-t', str(duration)])
    cmd.extend([
        '-vf', f"fps=15,scale={scale_width}:-1:flags=lanczos",
        '-y',
        output_gif
    ])
    subprocess.run(cmd, check=True)
    print(f"GIF created: {output_gif}")

if __name__ == "__main__":
    input_file = "input.mp4"
    extract_audio(input_file, "output.mp3")
    compress_video(input_file, "compressed.mp4")
    convert_video(input_file, "converted.mov", target_format="mov")
    video_to_gif(input_file, "output.gif", start_time="00:00:02", duration=3)
