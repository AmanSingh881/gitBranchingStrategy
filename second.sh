#transfering the files from one location to another

previous_minute=$(date -d '1 minute ago' +'%Y%m%d_%H%M')

file_name="$previous_minute.json"

file_path="/home/ispock/Desktop/data/aman/"

destination="/home/ispock/Documents/data"

mv "$file_path$file_name" $destination

ls $destination