# ffmpeg batch
---

######  Encode all .wav and .flac file to .mp3

CLI
```batch
for /r %i  in (*.flac, *.wav) do ffmpeg -i "%%i" -b:a 320k "%~ni.mp3"
```

.bat file
```bat
pushd "\\root\to\distant\folder"
for /r %%i  in (*.flac, *.wav) do ffmpeg -i "%%i" -b:a 320k "%%~ni.mp3"
popd

```
>`pushd` and `popd` allow to mount/umount  distant directory and avoid error
---
