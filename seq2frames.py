import ffmpeg

(
    ffmpeg
    .probe('../storage/pictures/*.jpg')
    .input('../storage/pictures/*.jpg', pattern_type='glob', framerate=30) # 4.669
    .output('out.mp4')
    .run_async()
)
