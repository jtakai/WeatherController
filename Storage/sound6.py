import subprocess
player = subprocess.Popen(["mplayer", "Carnival3.wav", "-ss", "30"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

