: Libraray instalation
pip install selenium
pip install couchdb
pip install networkx
pip install matplotlib

: Parametrs
set /A maxNumberOfScientistsToSearch = 40
set /A maximumNumberOfPublicationsBySingleScientist = 5
set /A maximumNumberOfCitingPublications = 5
set /A maximumNumberOfAuthorsOfSinglePublication = 3
set inputScientist="Albert Einstein"
set driverPath="C:\Users\Jakub\Downloads\geckodriver.exe"

python Scrapper.py %maxNumberOfScientistsToSearch% %maximumNumberOfPublicationsBySingleScientist% %maximumNumberOfCitingPublications% %maximumNumberOfAuthorsOfSinglePublication% %inputScientist% %driverPath%

pause