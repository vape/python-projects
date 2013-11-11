### Python Projects

My attempt at implementing the projects [over here](http://www.dreamincode.net/forums/topic/78802-martyr2s-mega-project-ideas-list/) with Python 3.

### Numbers

- [Find PI to the Nth Digit](https://github.com/vape/python-projects/blob/master/Numbers/pi/pi.py): Enter a number and have the program generate PI up to that many decimal places. Keep a limit to how far the program will go.

- [Fibonacci Sequence](https://github.com/vape/python-projects/blob/master/Numbers/fibonacci/fibonacci.py): Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number. (I did it a little differently. See README of that solution for specifics.)

- [Prime Factorization](https://github.com/vape/python-projects/blob/master/Numbers/primefactorization/prime.py): Have the user enter a number and find all Prime Factors (if there are any) and display them.

- [Next Prime Number](https://github.com/vape/python-projects/blob/master/Numbers/nextprime/nextprime.py): Have the program find prime numbers until the user chooses to stop the asking for the next one.

- [Mortgage Calculator](https://github.com/vape/python-projects/blob/master/Numbers/mortgagecalculator/mortgage.py): Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. Also figure out how long it will take the user to pay back the loan. (I had no idea what these two sentences mean, so I just made a simple mortgage calculator.)

- [Change Return Program](https://github.com/vape/python-projects/blob/master/Numbers/changecalculator/change.py): The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

- [Calculator](https://github.com/vape/python-projects/blob/master/Numbers/calculator/calc.py): A simple calculator to do basic operators. Make it a scientific calculator for added complexity.

- [Unit Converter](https://github.com/vape/python-projects/blob/master/Numbers/unitconverter/converter.py) (temp, currency, volume, mass and more): Converts various units between one another. The user enters the type of unit being entered, the type of unit they want to convert to and then the value. The program will then make the conversion.

- [Alarm Clock](https://github.com/vape/python-projects/blob/master/Numbers/alarmclock/alarmclock.py): A simple clock where it plays a sound after X number of minutes/seconds or at a particular time.

- [Distance Between Two Cities](https://github.com/vape/python-projects/blob/master/Numbers/distancecalculator/distcalc.py): Calculates the distance between two cities and allows the user to specify a unit of distance. This program may require finding coordinates of the cities like latitude and longitude.

- [Credit Card Validator](https://github.com/vape/python-projects/blob/master/Numbers/creditcardvalidator/validate.py): Takes in a credit card number of a common credit card vendor (Visa, Master-Card, American Express, Discoverer) and validates it to make sure that it is a valid number (look into how credit cards use a checksum).

- [Dijkstra's Algorithm](https://github.com/vape/python-projects/blob/master/Numbers/dijkstrasalgorithm/shortestpath.py): Create a program that finds the shortest path through a graph using its edges.

- [Roman Numeral Converter](https://github.com/vape/python-projects/blob/master/Numbers/romannumerals/roman.py): Create a program that converts a roman numeral to an integer. (I made this one up myself.)

- [Number Names](https://github.com/vape/python-projects/blob/master/Numbers/numbernames/numbernames.py) - Show how to spell out a number in English. You can use a preexisting implementation or roll your own, but you should support inputs up to at least one million (or the maximum value of your language's default bounded integer type, if that's less)

### Text

- [Pig Latin](https://github.com/vape/python-projects/blob/master/Text/piglatin/piglatinize.py): Pig Latin is a game of alterations played on the English language game. To form the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed.

- [Count Vowels](https://github.com/vape/python-projects/blob/master/Text/countvowels/countvowels.py): Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.

- [Check if Palindrome](https://github.com/vape/python-projects/blob/master/Text/palindrome/palindrome.py): Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like racecar.

- [Ciphers](https://github.com/vape/python-projects/blob/master/Text/ciphers/cipher.py): Functions for encrypting and decrypting data messages using Vigenere, Vernam and Caesar ciphers.


### Networking

- [Port Scanner](https://github.com/vape/python-projects/blob/master/Networking/portscanner/portscanner.py): Enter an IP address and a port range where the program will then attempt to find open ports on the given computer by connecting to each of them. On any successful connections mark the port as open.


### Classes

- [Product Inventory](https://github.com/vape/python-projects/blob/master/Classes/productinventory/inventory.py): Create an application which manages an inventory of products. Create a product class which has a price, id, and quantity on hand. Then create an inventory class which keeps track of various products and can sum up the inventory value.

- [Movie Store](https://github.com/vape/python-projects/blob/master/Classes/moviestore/store.py): Manage video rentals and controls when videos are checked out, due to return, overdue fees and for added complexity create a summary of those accounts which are overdue for contact.

- [Josephus Problem](https://github.com/vape/python-projects/blob/master/Classes/josephusproblem/josephus.py): Create a program which links together various node objects and then every Nth object is removed until you have one object left. This last object is the sole survivor.


### Threading

- [Download Progress Bar](https://github.com/vape/python-projects/blob/master/Threading/dlprogress/progress.py): Create a progress bar for applications that can keep track of a download in progress. The progress bar will be on a separate thread and will communicate with the main thread using delegates.

- [Download Manager](https://github.com/vape/python-projects/blob/master/Threading/dlmanager/manager.py): Allow your program to download various files and each one is downloading in the background on a separate thread. The main thread will keep track of the other threads progress and notify the user when downloads are completed.

- [Bulk Thumbnail Creator](https://github.com/vape/python-projects/blob/master/Threading/thumbnailcreator/thumb.py): Create an image program which can take hundreds of images and convert them to a specifed size in the background thread while you do other things.


### Web

- [Page Scraper](https://github.com/vape/python-projects/blob/master/Web/pagescraper/scraper.py): Create an application which connects to a site and pulls out all links or images and saves them to a list. For added complexity, organize the indexed content and don't allow duplicates. Have it put the results into an easily searchable index file.


### Games

- [Hangman](https://github.com/vape/python-projects/blob/master/Games/hangman/hangman.py): Randomly select a word from a file, have the user guess characters in the word. For each character they guess that is not in the word, have it draw another part of a man hanging in a noose. If the picture is completed before they guess all the characters, they lose.


### Data Structures:

- [Inverted index](https://github.com/vape/python-projects/blob/master/DataStructures/invertedindex/invertedindex.py): An [Inverted Index](http://en.wikipedia.org/wiki/Inverted_index) is a data structure used to create full text search. Given a set of text files, implement a program to create an inverted index. Also create a user interface to do a search using that inverted index which returns a list of files that contain the query term / terms. The search index can be in memory.
