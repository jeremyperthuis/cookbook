# ffmpeg bash
---

```bash
# Encode to x264
ffmpeg -i input.flv -vcodec libx264 -acodec aac output.mp4

# Convert to gif
ffmpeg -t 3 -i input.mp4 -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif

# Convert to mp3
ffmpeg -i input.wav -b:a 320k output.mp3
```
