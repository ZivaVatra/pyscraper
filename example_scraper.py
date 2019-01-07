#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: ts=4 expandtab ai
#
# File Created: Thu 31 May 19:57:43 CEST 2018
# Copyright 2018
#
# All rights reserved
#
# ============================================================|

__VERSION__ = (0, 0, 1)

import sys
sys.path.append("./site-packages")

import scraper_core


scraper = scraper_core.scraper(
    "https://www2.oxfordshire.gov.uk",
    cache_html="/tmp/cache"
)

page = scraper.fetch_page("cms/public-site/recycling-z")

views = page.find_all("div", {"class": "views-row"})

result = []
for view in views:
    title = view.h3.getText()
    print title
    data = view.find_all("div", {"class": "jquery-ui-filter-container"})
#    assert len(data) == 1, "Error, more than one filter-container. Check?"
    if len(data) != 1:
        continue
    description = ' '.join(data[0].stripped_strings)
    result.append([title, description.encode("utf-8")])

import csv
with open('result.csv', 'wb') as csvfile:
    cwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for entry in result:
        cwriter.writerow(entry)
