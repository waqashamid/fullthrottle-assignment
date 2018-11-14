from django.core.management.base import BaseCommand
from search.models import *
import logging
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('word_search.tsv') as tsvfile:
            reader = csv.reader(tsvfile, delimiter='\t')
            for row in reader:
                Word.objects.get_or_create(body=row[0], frequency=int(row[1]))
        print("Words add to the database!")
