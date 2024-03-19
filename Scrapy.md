---
tags:
  - CS
  - Python
  - Scrapy
---
by Hyr1sky

> Reference: 
> [Scrapy | A Fast and Powerful Scraping and Web Crawling Framework](https://scrapy.org/)
> [Scrapy Course – Python Web Scraping for Beginners (youtube.com)](https://www.youtube.com/watch?v=mBoX_JCKZTE)
> [The Python Scrapy Playbook | The Python Scrapy Playbook](https://thepythonscrapyplaybook.com/)

---
# Part 1: Intro

This is a note recording how to build a scrapy, and also a task of information searching course in BUPT 2024 spring.

In this note, we will follow the instructions of `Scrapy Course`, and every detailed lesson can be found on the website. Which you can look through by chapter.

## 1.1 What is scrapy

Developed by the co-founders of [Zyte](https://www.zyte.com/?rfsn=6335521.8097b3), Pablo Hoffman and Shane Evans, [Scrapy](https://scrapy.org/) is a Python framework specifically designed for web scraping.

Using Scrapy you can easily build highly scalable scrapers that will retrieve a pages HTML, parse and process the data, and store it the file format and location of your choice.

---
# Part 2: Setup Virtual Env & Scrapy
## 2.1 Env

**Install the Env:**
_Windows_:  `pip install virtualenv`
Virtualenv will enable you to have each thrid-party package seperately imported in your project.
It is actually a folder sits on top of python, managing to control your packages.

**Enter Part2:**  `python -m venv venv`
then, `venv` is set.

*MacOS:*  `source venv/bin/activate`
*Windows:*  `.\venv\Scripts\activate`
Activating the virtual environment, so the following packages we installed will be settled in this env.

**Install Scrapy in this folder:**
`pip install scrapy`
After downloading, run `scrapy` to check if it is working.
A list of command is supposed to be shown.

---
# Part 3: Creating A Scrapy Project
## 3.1 Creat Project

After activating the env, run `scrapy startproject <project_name>`.
Now we can see the following folder:

```
├── scrapy.cfg
└── bookscraper
    ├── __init__.py
    ├── items.py
    ├── middlewares.py
    ├── pipelines.py
    ├── settings.py
    └── spiders
        └── __init__.py
```

## 3.2 Building Blocks

Using these 5 building blocks you can create a scraper to do pretty much anything.

We won't be using all of these files in this beginners project, but we will give a quick explanation of each as each one has a special purpose:

- **settings.py** is where all your project settings are contained, like activating pipelines, middlewares etc. Here you can change the delays, concurrency, and lots more things.
- **items.py** is a model for the extracted data. You can define a custom model (like a ProductItem) that will inherit the Scrapy Item class and contain your scraped data.
- **pipelines.py** is where the item yielded by the spider gets passed, it’s mostly used to clean the text and connect to file outputs or databases (CSV, JSON SQL, etc).
- **middlewares.py** is useful when you want to modify how the request is made and scrapy handles the response.
- **scrapy.cfg** is a configuration file to change some deployment settings, etc. (ROBOTSTXT, REQUESTS...)

The most fundamental of which are **Spiders**.

## 3.3 Details About Each Blocks

Get access to this through [freeCodeCamp Scrapy Beginners Course Part 3 - Creating Scrapy Project | The Python Scrapy Playbook](https://thepythonscrapyplaybook.com/freecodecamp-beginner-course/freecodecamp-scrapy-beginners-course-part-3-scrapy-project/)

---
# Part 4: First Scrapy Spider
## 4.1 Generation

Enter the spiders folder, run `cd ./bookscraper/bookscraper/spiders`.
You will see `__init__.py` in it.

Then run `scrapy genspider bookspider books.toscrape.com`

```shell
 ⚡Hyr1sky ❯❯scrapy genspider bookspider books.toscrape.com
Created spider 'bookspider' using template 'basic' in module:
  bookscraper.spiders.bookspider
```

We have successfully created a basic template for scrapying task in `spiders`.

```python
class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        pass
```

- name: indicate the project name
- allowed_domains: specify the scope of the crawler's operation
- start_urls: target url
- def parse(): the part we need to modify for further functions

## 4.2 Using Scrapy Shell To Find Our CSS Selectors

Run `pip install ipython` to get a better shell that is easier to read,  then go to `scrapy.cfg` to implement ipython. After that, we are able to run shell in terminal by running `scrapy shell`.

```python
[settings]
default = bookscraper.settings
shell = ipython
```

**Give a stab at it:**
Run `fetch('https://books.toscrape.com/')`

```shell
2024-03-17 10:47:36 [scrapy.core.engine] INFO: Spider opened
2024-03-17 10:47:43 [scrapy.core.engine] DEBUG: Crawled (404) <GET https://books.toscrape.com/robots.txt> (referer: None)
2024-03-17 10:47:44 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://books.toscrape.com/> (referer: None)

2024-03-17 10:47:44 [asyncio] DEBUG: Using selector: SelectSelector
```

Run `response.css()` to extract certain info you want, the target should be included in the brackets with css, here we go with `response.css('article.product_pod')`. The scrapy return all the items in the page, if we just want the first one, run `response.css('article.product_pod').get()`.

```shell
In [3]: response.css('article.product_pod').get()
Out[3]: '<article class="product_pod">\n        \n            <div class="image_container">\n                \n                    \n                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>\n                    \n                \n            </div>\n        \n\n        \n            \n                <p 
class="star-rating Three">\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n                    <i class="icon-star"></i>\n     
               <i class="icon-star"></i>\n                </p>\n            \n        \n\n        \n            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>\n        \n\n        \n            <div class="product_price">\n                \n\n\n\n\n\n\n    \n        <p class="price_color">£51.77</p>\n    \n\n<p class="instock availability">\n    <i class="icon-ok"></i>\n    \n        In stock\n    \n</p>\n\n                \n                    \n\n\n\n\n\n\n    \n    <form>\n        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>\n    </form>\n\n\n                \n            </div>\n        \n    </article>'
```

What's more, we can put the info into a certain variale, by simply run `books = response.css('article.product_pod')`. And we can access the property of `books` just as the way as normal variable.

```shell
In [4]: books = response.css('article.product_pod')

In [5]: len(books)
Out[5]: 20
```

Check the target's property in DeveloperTools.

```shell
In [6]: book = books[0]

In [7]: book.css('h3 a::text').get()
Out[7]: 'A Light in the ...'
```

```shell
In [8]: book.css('.product_price .price_color::text').get()
Out[8]: '£51.77'
```

```shell
In [9]: book.css('h3 a').attrib['href']
Out[9]: 'catalogue/a-light-in-the-attic_1000/index.html'
```

After these steps, we already know how to get book names, prices and urls, so we are able to integrate them into the `parse` function and loop to get all the infos.

```python
def parse(self, response):
    books = response.css('article.product_pod')

    for book in books:
        yield {
            'name': book.css('h3 a::text').get(),
            'price': book.css('.product_price .price_color::text').get(),
            'url': book.css('h3 a').attrib['href'],
        }
```

`exit` to exit ipython shell, go back to `bookscraper` to run `scrapy crawl bookspider`.

```shell
2024-03-17 11:21:12 [scrapy.core.scraper] DEBUG: Scraped from <200 https://books.toscrape.com>
{'name': 'Set Me Free', 'price': '£17.46', 'url': 'catalogue/set-me-free_988/index.html'}
2024-03-17 11:21:12 [scrapy.core.scraper] DEBUG: Scraped from <200 https://books.toscrape.com>
{'name': "Scott Pilgrim's Precious Little ...", 'price': '£52.29', 'url': 'catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html'}
2024-03-17 11:21:12 [scrapy.core.scraper] DEBUG: Scraped from <200 https://books.toscrape.com>
{'name': 'Rip it Up and ...', 'price': '£35.02', 'url': 'catalogue/rip-it-up-and-start-again_986/index.html'}
2024-03-17 11:21:12 [scrapy.core.scraper] DEBUG: Scraped from <200 https://books.toscrape.com>
{'name': 'Our Band Could Be ...', 'price': '£57.25', 'url': 'catalogue/our-band-could-be-your-life-scenes-from-the-american-indie-underground-1981-1991_985/index.html'}
```

## 4.3 Navigating to the "Next Page"

Go back to scrapy shell, and find the route to next page.
`response.css('li.next a ::attr(href)').get()`
Then we will get `'catalogue/page-2.html'`.

So we loop the process until reaching the last page, corresponding with the `if next_page is not None`, then we use `.follow` and `callback` to repeat the whole function.

```python
def parse(self, response):
    books = response.css('article.product_pod')

    for book in books:
        yield {
            'name': book.css('h3 a::text').get(),
            'price': book.css('.product_price .price_color::text').get(),
            'url': book.css('h3 a').attrib['href'],
        }

    next_page = response.css('.next a::attr(href)').get()

    if next_page is not None:
        if next_page.startswith('catalogue'):
            next_page_url = 'https://books.toscrape.com/' + next_page
        else:
            next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
        yield response.follow(next_page_url, callback=self.parse)
```

Conc:

```shell
 'item_scraped_count': 1000,
 'log_count/DEBUG': 1054,
 'log_count/INFO': 10,
 'request_depth_max': 49,
 'response_received_count': 51,
 'robotstxt/request_count': 1,
 'robotstxt/response_count': 1,
 'robotstxt/response_status_count/404': 1,
 'scheduler/dequeued': 50,
 'scheduler/dequeued/memory': 50,
 'scheduler/enqueued': 50,
 'scheduler/enqueued/memory': 50,
```

---
# Part 5 Crawling With Scrapy
## 5.1 Requests For More Details

However, this data only contained summary data for each book. Whereas if we looked at an individual book page we can see there is a lot more information like:

- Number of books available
- UPC of each book
- Product type
- Product description
- Price including & excluding taxes
- Number of reviews

So we have to extract the detail page of a book and callback to `parse_book_page` where we will do the further steps.

```python
def parse(self, response):
    books = response.css('article.product_pod')
    for book in books:
        relative_url = book.css('h3 a').attrib['href']
        if 'catalogue/' in relative_url:
            book_url = 'https://books.toscrape.com/' + relative_url
        else:
            book_url = 'https://books.toscrape.com/catalogue/' + relative_url
        yield scrapy.Request(book_url, callback=self.parse_book_page)

    ## Next Page        
    next_page = response.css('li.next a ::attr(href)').get()
    if next_page is not None:
        if 'catalogue/' in next_page:
            next_page_url = 'https://books.toscrape.com/' + next_page
        else:
            next_page_url = 'https://books.toscrape.com/catalogue/' + next_page
        yield response.follow(next_page_url, callback=self.parse)

def parse_book_page(self, response):
    pass
```

## 5.2 Using Scrapy Shell To Find CSS & XPath Selectors

Our targets:

- Book URL
- Title
- UPC
- Product Type
- Price
- Price Excluding Tax
- Price Including Tax
- Tax
- Availability
- Number of Reviews
- Stars
- Category
- Description
### 5.2.1 Extracting Data Using Siblings

Next we want to extract the product **description** and **category** data from the page. ⭐However, there is no `id` or `class` variables we can use to extract these easily so we will use siblings to extract them.

it is contained in a generic `<p>` tag.

**Description:** The **description** is contained in a generic `<p>` tag. However, this `<p>` tag is always after the `<div id='product_description'>` so we can extract it using siblings functionality.

For this we will use an XPaths instead of CSS selectors as it has better support for this:

```shell
book.xpath("//div[@id='product_description']/following-sibling::p/text()").get()
```

**Category:** The **category** is contained in a `li` element at the top of the page in the 2nd last `li` element.

Again, for this we will use an XPaths instead of CSS selectors as it has better support for targeting siblings:

```shell
book.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get()
```
### 5.2.2 Extracting Data From Table

Another common scraping scenario is that you want to extract data from tables. In this case, we want to extract the **UPC**, **Product Type**, **Price**, **Price Excluding Tax**, **Price Including Tax**, **Tax**, **Availability** and **Number of Reviews** from the table at the bottom of the page.

To do this we will first retrieve the table rows themselves:

```shell
table_rows = response.css("table tr")
```

Now we can access to all the data using the `table_rows`.

## 5.3 Extracting Data From Attributes

Finally, we want to extract the **number of stars** each book recieved. This data is contained in the `class` attribute of the `star-rating` class. For example:

```css
<p class="star-rating Three">
	<i class="icon-star"></i>
	<i class="icon-star"></i>
	<i class="icon-star"></i>
	<i class="icon-star"></i>
	<i class="icon-star"></i>
</p>
```

To scrape the **number of stars** each book recieved, we need to extract the number from the `class` attribute.

We can do this like this:

```shell
book.css("p.star-rating").attrib['class']
```

Now, that we've found the correct XPath & CSS selectors we can exit Scrapy shell with the `exit()` command, and update our Spider.

## 5.4 Updating Spider

```python
def parse_book_page(self, response):
    book = response.css("div.product_main")[0]
    table_rows = response.css("table tr")
    
    yield {
        'url': response.url,
        'title': book.css("h1 ::text").get(),
        'upc': table_rows[0].css("td ::text").get(),
        'product_type': table_rows[1].css("td ::text").get(),
        'price_excl_tax': table_rows[2].css("td ::text").get(),
        'price_incl_tax': table_rows[3].css("td ::text").get(),
        'tax': table_rows[4].css("td ::text").get(),
        'availability': table_rows[5].css("td ::text").get(),
        'num_reviews': table_rows[6].css("td ::text").get(),
        'stars': book.css("p.star-rating").attrib['class'],
        'category': book.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
        'description': book.xpath("//div[@id='product_description']/following-sibling::p/text()").get(),
        'price': book.css('p.price_color ::text').get(),
        }
```

We can save files while running the program.
If we want to save the data to a JSON file we can use the `-O` option, followed by the name of the file.

```shell
scrapy crawl bookspider -O myscrapeddata.json
```

If we want to save the data to a CSV file we can do so too.

```shell
scrapy crawl bookspider -O myscrapeddata.csv
```

However, there does exist some issues that some data cannot be displayed correctly.

---
# Part 6