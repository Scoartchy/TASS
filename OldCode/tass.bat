::scholar.py -c 1 --author "albert einstein" --phrase "quantum theory"

::scholar.py -c 1 --author "albert einstein" --phrase "quantum theory" --citation bt

::scholar.py --txt-globals --author "albert einstein" | grep '\[G\]' | grep Results

::scholar.py -c 1 --author "Stephen Hawking" --phrase "quantum theory" 

::scholar.py -c 1 -C 17749203648027613321 --citation bt

::scholar.py --citations-only -c 1 --author "albert einstein" --phrase "quantum theory"



scholar.py --citations-only -c 1 --author "cezary zielinski" :: retrive the list of articles that cites the first article

pause

:: for each phrase == title
::scholar.py -c 1 --phrase "Robot control system design exemplified by multi-camera visual servoing" --citation bt


pause