# Reader
I decided to move away from Pocket for saving articles to read later, and instead build my own little app. This is by no means top quality coding, it was thrown together to solve a problem.
This requires PHP and python to run.
**Source code:** [https://github.com/0xdstn/reader](https://github.com/0xdstn/reader)
## Setup
Place the contents of the repo in a directory called **reader** inside your root web directory (such as **/var/www/html/reader**).
Create a `key.txt` file one directory up from your root web directory (such as **/var/www**). [i:This should not be accessible via a browser.]
Create a `data.txt` file in the reader directory.
Set up a cron job for the scraper. I have it set up to run every hour like so:
```
0 * * * * cd /var/www/html/reader && ./scrape.py >/dev/null 2>&1
```
The cron job takes any URL that hasn't been scraped in `data.txt`, pulls the title and the contents for it via web scraping, updates `data.txt` with the title, and generates an HTML file of the contents in the `articles` directory.
## Pocket import
I transitioned from Pocket to this, so I made a pocket import script. 
To use it, go to Pocket and export your links as an HTML file. Place that in the reader directory. It should be called `ril_export.html`.
You then should just need to run the `pocket-import.py` file and it will convert the HTML export into entries in `data.txt`.
## Usage
Navigating to the **/reader?key=YOURKEY** directory on your webserver will display a list of articles from `data.txt`. Replace **YOURKEY** with the contents of the `key.txt` file. If the title has been scraped it will display that and link to the local HTML file for it. If it has not yet been scraped, it will display the URL and link out to that.
You can click **Add article**, which will give you a box to fill in a URL and a submit button. This adds the provided URL to `data.txt`.
When reading a local HTML article, there is a **mark read** link at the top and bottom which you can click to mark it as read, removing it from the list on the index page.
This app is really light weight, so it works well in the web browser of a kindle.
