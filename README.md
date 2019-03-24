# Scraping College Application Network Data

## Data Source

[新鮮人查榜](https://freshman.tw/cross)


## Crawl Command

Remember to delete the output JSON files if they exist.

```bash
cd college_network
```

```bash
scrapy crawl ntuNetwork -s CLOSESPIDER_ITEMCOUNT=1000 -s DOWNLOAD_DELAY=0.7 -s CONCURRENT_REQUESTS=4 -o ntuNetwork.json
scrapy crawl egoNetwork -s CLOSESPIDER_ITEMCOUNT=1000 -s DOWNLOAD_DELAY=0.7 -s CONCURRENT_REQUESTS=4 -o egoNetwork.json
```

## Data Cleaning

- [Jupyter Notebook](https://liao961120.github.io/collegeSNA/ntuNetwork)
