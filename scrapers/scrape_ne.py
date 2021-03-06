#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import scrape_common as sc

xls_url = 'https://www.ne.ch/autorites/DFS/SCSP/medecin-cantonal/maladies-vaccinations/Documents/Covid-19-Statistiques/COVID19_PublicationInternet.xlsx'
xls = sc.xlsdownload(xls_url, silent=True)
rows = sc.parse_xls(xls)
for i, row in enumerate(rows):
    dd = sc.DayData(canton='NE', url=xls_url)
    dd.datetime = row['A'].date().isoformat()
    dd.cases = row['Cumul']
    dd.hospitalized = row['Total des cas hospitalisés']
    if row['Soins intensifs (intubés)'] is not None and row['Soins intensifs (non intubés)'] is not None:
        ICU = row['Soins intensifs (intubés)']
        ICU2 = row['Soins intensifs (non intubés)']
        dd.icu = int(ICU)+int(ICU2)
    dd.vent = row['Soins intensifs (intubés)']
    dd.deaths = row['Cumul des décès']
    print(dd)
    # do not print record delimiter for last record
    # this is an indicator for the next script to check
    # for expected values.
    if len(rows) - 1 > i:
        print('-' * 10)
