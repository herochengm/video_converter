import subprocess
import os

def extract_audio(input_video, output_audio, audio_format='mp3'):
    """
    从视频中提取音频
    """
    cmd = [
        'ffmpeg',
        '-i', input_video,
        '-vn',  # 不处理视频
        '-acodec', 'libmp3lame' if audio_format == 'mp3' else 'aac',
        '-y',  # 覆盖输出
        output_audio
    ]
    subprocess.run(cmd, check=True)
    print(f"Audio extracted: {output_audio}")

def compress_video(input_video, output_video, crf=28, preset='medium'):
    """
    压缩视频
    crf: 视频质量参数，值越小质量越高，文件越大（18-28之间常用）
    preset: 压缩速度，越慢压缩比越高
    """
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
    """
    视频格式转换
    """
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
    """
    视频转 GIF
    start_time: 开始时间，如 "00:00:05"
    duration: 时长，如 "3" 秒
    scale_width: GIF 宽度，按比例缩放
    """
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
    
    # 提取 MP3
    extract_audio(input_file, "output.mp3")
    
    # 压缩视频
    compress_video(input_file, "compressed.mp4")
    
    # 转码视频
    convert_video(input_file, "converted.mov", target_format="mov")
    
    # 转 GIF
    video_to_gif(input_file, "output.gif", start_time="00:00:02", duration=3)
