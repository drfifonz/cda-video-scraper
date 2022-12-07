<center>

cda video scraper
====

</center>

About
----

Basic video downloader from cda.pl video steam service. 

Project base on static and dynamic scrapping concept. Webpage is parsed with BeautifulSoup Python module, executing necessary javascript is provided by Selenium.

It is possible to download multiple videos by passing search quote as parameter. User can select which video want to download from displayed list. 

---

Before first run
----
Fristly specify constant variables at [config.py](src/config.py) like:

- DOWNLOAD_PATH
- FIREFOX_DRIVER_PATH
- FIREFOX_TO_DEV_NULL
  </br>



You can download firefox GeckoDriver [here](https://github.com/mozilla/geckodriver/releases).

How to run
----
Execute [main.py](src/main.py) file with arguments:
-  \<link\>/\<searchead quote\> &emsp;&emsp; 
- --pages / -p &emsp;&emsp;    (optional) for searching more pages than 1

 Example:

 ```
 python src/main.py <link>
 ```




