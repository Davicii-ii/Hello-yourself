import ffmpeg, sys, os

def use_lin():
    (
        ffmpeg
        .input('../storage/pictures/X/*.jpg', pattern_type='glob', framerate=1) # 4.669
        .output('out.mp4')
        .run_async()
    )

def use_win():
    (
        ffmpeg
        .input('../Pictures/X/*.jpg', pattern_type='glo\
b', framerate=1) # 4.669
        .output('out.mp4')
        .run_async()
    )
    
def loop():
    pass
