import ffmpeg, sys, os

(
    ffmpeg
    .input('../storage/pictures/X/*.jpg', pattern_type='glob', framerate=1) # 4.669
    .filter('deflicker', mode='pm', size=10)
    .filter('scale', size='hd1080', force_original_aspect_ratio='increase')
    .output('out.mp4', crf=20, preset='slower', pix_fmt='yuv420p')
    .view(filename='filter_graph')
    .run_async()
)
