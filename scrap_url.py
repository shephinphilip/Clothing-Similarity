# -*- coding: utf-8 -*-
"""Scrap_Url.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a42neltsebjB9pPKkKcpWiisx10cBUV-
"""
#scrap 
import pandas as pd
import random
import re
import urllib.parse

# Read the CSV file from Kaggle
df = pd.read_csv('Clothing_datasets.csv')


df['product_url_website1'] = df.apply(lambda row: f'https://www.myntra.com/dkny?rawQuery={urllib.parse.quote(row["ProductName"])}', axis=1)
df['product_url_website2'] = df.apply(lambda row: f'https://www.limeroad.com/search/{urllib.parse.quote(row["ProductName"])}', axis=1)
df['product_url_website3'] = df.apply(lambda row: f'https://www.tatacliq.com/search/?searchCategory=all&text={urllib.parse.quote(row["ProductName"])}', axis=1)


# Save the updated CSV file
df.to_csv('Fashion_clothing.csv', index=False)
