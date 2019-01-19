#!/usr/bin/env python
# -*- coding: utf8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
import time
import hashlib
import random
from DatabaseManager import *

# Firefox driver loading
#driver = webdriver.Firefox(executable_path=r'C:\Users\Jakub\Downloads\geckodriver-v0.23.0-win64\geckodriver.exe') # Praca
#driver = webdriver.Firefox(executable_path=r'D:\Pobrane z Google Chrome\geckodriver-v0.23.0-win64\geckodriver.exe') # Dom (PC)
driver = webdriver.Firefox(executable_path=r'C:\Users\Jakub\Downloads\geckodriver.exe') # Dom (Laptop)

#The author from whom we start extracting information from Google Scholar
inputScientist = "Cezary Zielinski"
scientistName = inputScientist.encode('UTF8')
scientistHash = int(hashlib.sha1(scientistName).hexdigest(), 16) % (10 ** 8)
scientists = [(scientistHash, scientistName, set())]

# Constats
maxNumberOfScientistsToSearch = 10
maximumNumberOfPublicationsBySingleScientist = 10
maximumNumberOfCitingPublications = 10
maximumNumberOfAuthorsOfSinglePublication = 5

baseTimeSleep = 2

#Iterations over scientists
for scientistNumber in range(0, maxNumberOfScientistsToSearch):

    driver.get("https://scholar.google.pl/")

    print("-----------------------------------------------------------------------------------------------------------")
    print("Input scientist")
    enter = driver.find_element_by_css_selector('#gs_hdr_tsi')

    scientist = scientists[scientistNumber]
    inputToGoogleScholar = scientist[1]

    print(inputToGoogleScholar)

    print("!", scientist)

    enter.send_keys(inputToGoogleScholar.decode('UTF8'))
    enter.submit()
    time.sleep(baseTimeSleep + random.uniform(0, 2))

    print("His works")
    
    condition = False
    while not condition:
        try:
            enter = driver.find_element_by_xpath('/html/body/div/div[11]/div[2]/div[2]/div[2]/div[1]/table/tbody/tr/td[2]/h4/a')
            enter.click()
            time.sleep(baseTimeSleep + random.uniform(0, 2))
            condition = True
        except NoSuchElementException:
            time.sleep(60)

    #Authors that are not linked are omitted 
    for i in range(1, maximumNumberOfPublicationsBySingleScientist): 
        #print("i: ", i)
        s = "tr.gsc_a_tr:nth-child(" + str(i) + ") > td:nth-child(2) > a:nth-child(1)"
        enter = driver.find_element_by_css_selector(s)
        enter.click()
        time.sleep(baseTimeSleep + random.uniform(0, 2))  
        
        #Max 5 authors of one book or publication
        for j in range(1, maximumNumberOfCitingPublications): 
            for k in range(1, maximumNumberOfAuthorsOfSinglePublication): 
                #print("j: ", j, " k: ", k)       
                try:
                    s = "div.gs_or:nth-child(" + str(j) + ") > div:nth-child(2) > div:nth-child(2) > a:nth-child(" + str(k) + ")"
                    enter = driver.find_element_by_css_selector(s)
                    enter.click()

                    quoter  = driver.find_element_by_css_selector("#gsc_prf_in")
                    # print(author.text)
                    
                    # Add a new author (quoter) to scientists 
                    quoterScientistName = quoter .text.encode('UTF8')
                    quoterScientistHash = int(hashlib.sha1(quoterScientistName).hexdigest(), 16) % (10 ** 8)

                    # Checking if author (quoter) is in the list of authors
                    scientistIsInList = False
                    for s in scientists:
                        if s[0] == quoterScientistHash:
                            scientistIsInList = True
                            #print("TRUE")

                    if not scientistIsInList:
                        quoterScientistTuple = (quoterScientistHash, quoterScientistName, set())
                        scientists.append(quoterScientistTuple)
                        #print("FALSE, added: ", scientistTuple, "to list of scientists.")

                    # Add a new author (quoter) to the set of authors who quoted him
                    print("\n List of scientists:")
                    for s in scientists:
                        print(s)

                    scientistTuple = scientists[scientistNumber]
                    scientistName = scientistTuple[1]
                    scientistHash = scientistTuple[0]
                    scientistSet = scientistTuple[2].copy()
                    scientistSet.add(quoterScientistName)
                    newScientistTuple = (scientistHash, scientistName, scientistSet)
                    scientists[scientistNumber] = newScientistTuple

                    print("Updated tuple ", scientistNumber, " ", scientists[i], ", added: ", scientistName, " to set.")

                    #scientistsTuple = scientist[i]
                    #scientistsSet = scientistTuple[2]
                    #scientistsSet.Add(author.text)

                    time.sleep(baseTimeSleep + random.uniform(0, 2))
                    driver.back()
                    time.sleep(baseTimeSleep + random.uniform(0, 2))
                except (NoSuchElementException, WebDriverException) as error:
                    time.sleep(baseTimeSleep + random.uniform(0, 2))

    #Return to previous page    
        time.sleep(baseTimeSleep + random.uniform(0, 2))
        driver.back()
        time.sleep(baseTimeSleep + random.uniform(0, 2))

    i+=1

# Firefox driver closing       
driver.close()

# Printing all data
for scientist in scientists:
    print("Scientist ", scientist[1], " who is quoted by:", scientist[2])

# Create the CouchDB database 
CreateCouchDBDatabase(scientists)

