from django.shortcuts import render
from .models import *
from rest_framework import status, views
from rest_framework.response import Response
from .serializer import *
from django.db.utils import DatabaseError
from django.http import HttpResponse, StreamingHttpResponse

class SearchWords(views.APIView):
    def get(self, request, **kwargs):
        try:
            word = kwargs.get('word')
        except KeyError as e:
            return Response({"Error" : str(e)}, status=status.HTTP_400_BAD_REQUEST)

        matches = Word.objects.filter(body__contains=word)[:25]
        rank_score = {}

        # Sorting on the basis of startswith requirement
        matches_startswith = sorted([match.body for match in matches], key = lambda x: x.startswith(word))
        matches_startswith = matches_startswith[::-1]

        # Sorting to place shorter lengths first
        matches_short = sorted([match.body for match in matches], key = lambda x: len(x))

        # Sorting to place high frequency matches first
        matches_freq = sorted([match for match in matches], key = lambda x: x.frequency)
        matches_freq = [match.body for match in matches_freq]

        for word in [match.body for match in matches]:
            rank_score[word] = 4*(25 - matches_startswith.index(word))
            rank_score[word] = rank_score[word] + 3*(25 - matches_short.index(word))
            rank_score[word] = rank_score[word] + (25 - matches_freq.index(word))/16

        result = sorted(rank_score.items(), key=lambda kv: kv[1], reverse=True)
        result = [x[0] for x in result]

        return Response(result, status=status.HTTP_200_OK)