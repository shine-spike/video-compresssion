ffmpeg -i "$1" -s 480x360 -c:v libx264 -crf 23 -c:a aac -strict -2 "$2"
