import moviepy.editor as mp

clip = mp.VideoFileClip(r"Vid.mp4")
clip.audio.write_audiofile(r"Audio.wav")