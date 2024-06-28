#!/bin/bash

scrapy crawl top_movies -o movies.json &

python3 app/main.py