SPATH=$SPATH
FILE_NAME="AMAM"
DPATH="/home/ispock/Documents/"

if [ ! -d "$SPATH" ]; then
    echo "Error: Source directory not found."
    exit 1
fi
echo $FILE_NAME
# Create a compressed file of the source directory
tar -czf "$FILE_NAME" -C "$(dirname "$SPATH")" "$(basename "$SPATH")"
ls