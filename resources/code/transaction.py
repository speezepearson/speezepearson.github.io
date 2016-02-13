#!/usr/bin/python3

import os
import datetime as dt
import csv
import argparse

DATE_FORMAT = '%Y-%m-%d'
def date(s):
  return dt.datetime.strptime(s, DATE_FORMAT)

parser = argparse.ArgumentParser()
parser.add_argument('amount', type=float, help="always positive, whether expense or income")
parser.add_argument('category')
parser.add_argument('--date', default=dt.datetime.now(), type=date, help="in YYYY-MM-DD")
parser.add_argument('--note', default='')
parser.add_argument('--file', default=os.path.join(os.path.expanduser('~'), ".transactions.csv"))

args = parser.parse_args()

with open(args.file, 'a') as f:
  csv.DictWriter(f, ['Date', 'Amount', 'Category', 'Note']).writerow({
    'Date': args.date.strftime(DATE_FORMAT),
    'Amount': '{:0.2f}'.format(args.amount),
    'Category': args.category,
    'Note': args.note})
