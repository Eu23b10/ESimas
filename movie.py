from moviepy.editor import *

mp4_file = "adele_someone_like_you_lyrics._h264_41674.mp4" #caminho do video

mp3_file = "adele_someone_like_you.mp3" #declrando caminho pro audio

videoclip = VideoFileClip(mp4_file) #mostrando que e video
audioclip = videoclip.audio #passar o video pra audio
audioclip.write_audiofile(mp3_file) #completando a passagem e mostrando o caminho pro aruivo

audioclip.close() #fechando o video

videoclip.close() #fechando o audio