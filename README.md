## dlvi
archive my likes

#### download/archive all my likes from vimeo
* get to your likes page vimeo.com/user/likes
* load all video, right click on fo them and hit inspect, then copy all the div to clipboard

#### run python script to extract all the video links to a .txt file

#### run youtube-dl one liner 

`youtube-dl -f worst -o 'LIKES/%(title)s_%(id)s.%(ext)s' --write-description  --write-info-json  -a links.txt` 

* `-f worst` = worst/smallest format possible
* you can remove `--write-description  --write-info-json ` if you dont want to archive thier info
