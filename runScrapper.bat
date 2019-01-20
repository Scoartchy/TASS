: Parametrs
set /A maxNumberOfScientistsToSearch = 40
set /A maximumNumberOfPublicationsBySingleScientist = 5
set /A maximumNumberOfCitingPublications = 5
set /A maximumNumberOfAuthorsOfSinglePublication = 3

python Scrapper.py %maxNumberOfScientistsToSearch% %maximumNumberOfPublicationsBySingleScientist% %maximumNumberOfCitingPublications% %maximumNumberOfAuthorsOfSinglePublication%

pause