from keybeat import analyze_audio

bpm, key, mode = analyze_audio("sua_musica.wav")
print(f"BPM: {bpm}")
print(f"Tom: {key} ({mode})")
