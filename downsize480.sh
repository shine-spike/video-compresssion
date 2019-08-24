ffmpeg -i "$1" -s hd480 -c:v libx264 -crf 23 -c:a aac -strict -2 "$2"
