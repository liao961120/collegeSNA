# Scraping College Application Network Data



### Crawl Command

Remember to delete the output JSON files if they exist.

```
scrapy crawl ntuNetwork -s CLOSESPIDER_ITEMCOUNT=1000 -s DOWNLOAD_DELAY=0.7 -s CONCURRENT_REQUESTS=4 -o ntuNetwork.json
scrapy crawl egoNetwork -s CLOSESPIDER_ITEMCOUNT=1000 -s DOWNLOAD_DELAY=0.7 -s CONCURRENT_REQUESTS=4 -o egoNetwork.json
```

