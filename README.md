# JAWS - Just Another (simple) Web Scraper (in Python)

Phil's Simple Web Scraping Client

## Requirements

```sh
pip install -r requirements.txt
```

## Usage

```sh
python main.py [flags]
```

flags:

main.py:
  -i,--id: DOM element ID of the element that contains the required text value
  -p,--interval: Polling interval in seconds
    (an integer)
  -u,--url: URL of the website to scrape

Try --helpfull to get a list of all flags.

## Example .env file

```env
# .env
LOG_LEVEL=DEBUG
WEBSITE_URL=http://wetter.com
ELEMENT_ID=cmp-btn-accept
POLL_INTERVAL=5
```

## Build

### Build with Bazel

```sh
bazel build :jaws
```

### Execute

#### Windows

```cmd
jaws.exe --helpshort
```
