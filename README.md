# BrokenLinkFinder

## Introduction

BrokenLinkFinder is an enhanced Python script capable of identifying broken hyperlinks across multiple webpages. This tool first reads a sitemap, extracts all URLs, and then scans each URL for broken links. It reports back any links that lead to a page with a 404 error or other client/server error status codes, making it an invaluable resource for webmasters and SEO specialists.

## Features

* Scans multiple webpages for broken links by reading a sitemap.
* Efficiently identifies links with client or server errors (e.g., 404 Not Found).
* Outputs results in a CSV file with columns for the original URL, broken link, and the link text.
* Easy to use and integrate into existing workflows.

## Installation

### Prerequisites

* Python 3.x
* requests library
* beautifulsoup4 library

### Setup
* Clone this repository:
```git clone https://github.com/yourusername/BrokenLinkFinder.git```

* Install the required Python libraries:
```pip install requests beautifulsoup4```

## Usage
To use the script, simply run it with the URL of the webpage you want to check as an argument:

```python broken_link_finder.py 'https://www.example.com'```

## Contributing

Contributions to improve BrokenLinkFinder are welcome. Please feel free to fork the repository and submit pull requests.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.

