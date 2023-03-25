<center>

cda video scraper
====

</center>

About
----

Basic video downloader from cda.pl video steam service. 

The project is based on static and dynamic scrapping concept. CDA webpage is parsed with BeautifulSoup Python module, executing necessary javascript is provided by Selenium.

It is possible to download multiple videos by passing search quote as parameter. User can select which video want to download from displayed list. 

---

Before first run
----
Fristly specify constant variables in [config.py](src/config.py):

- DOWNLOAD_PATH  - path where downloaded videos would be saved
- FIREFOX_DRIVER_PATH - path to firefox browser engine
- FIREFOX_TO_DEV_NULL - tmp directory for saving logs required to run script, files can be removed after execution 
  </br>


Project use selenium, which requires to specify brower engine.For proper runnig it is necessary to usue __Firefox GeckoDriver__ .</br>
You can download it [here](https://github.com/mozilla/geckodriver/releases).

How to run
----
Execute [main.py](src/main.py) file with arguments:
-  \<link\>/\<searchead quote\> &emsp;&emsp; 
- --pages / -p &emsp;&emsp;    (optional) for searching more pages than 1

 Example:

 ```
 python src/main.py <link>
 ```




