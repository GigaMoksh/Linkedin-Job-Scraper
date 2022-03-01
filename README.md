## LinkedIn Job Scraper

![python](https://img.shields.io/badge/language-Python-orange?style=for-the-badge)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=plasitc)](https://github.com/psf/black)

### About

A Python3 script to <b>scrap</b> best job fitted for you from [`LinkedIn`](https://www.linkedin.com/jobs/) according to the given input <br>and saves them in `.csv` file named `linkedin-job-scrapper.csv`

Note : Header of `.csv` file will look like this :

| id  | Job | Company | Details | Location | Upload Date | Link |
| --- | --- | ------- | ------- | -------- | ----------- | ---- |
|     |     |         |         |          |             |

### User Manual

You can search Jobs by 2 methods :

1. `Direct Search` (Using your IP Address)*
2. `Custom Search` (Recommended)*

If you have entered `2` previously then :

1. Enter : Your `City` \*
2. Enter : Your `Job Profile` \*
3. Enter :
   - `1` : To Enter Types of Job you want. (eg. Internship , Entry Level)
   - `2` : To Enter Job Type : Full-Time or Part-Time
   - `0` : To `esc` this step *

### Setup

To install the required libraries :
<br><b>Run:</b>

```
pip install -r requirements.txt
```
