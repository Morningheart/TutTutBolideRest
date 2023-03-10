from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import math

R = 6371

@api_view(['POST'])
def GetDistance(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        coords = request.data
        if not "coordinates" in coords:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        if not all(["lon" in c for c in coords["coordinates"]]):
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        if not all(["lat" in c for c in coords["coordinates"]]):
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        if not all([type(c["lon"]) is type(.1) for c in coords["coordinates"]]):
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        if not all([type(c["lat"]) is type(.1) for c in coords["coordinates"]]):
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        cp = [
            math.radians(coords["coordinates"][0]["lon"]),
            math.radians(coords["coordinates"][0]["lat"]),
            math.radians(coords["coordinates"][1]["lon"]),
            math.radians(coords["coordinates"][1]["lat"]),
        ]
        a = math.sin((cp[3]-cp[1])/2)**2 + math.cos(cp[1])*math.cos(cp[3])*math.sin((cp[2]-cp[0])/2)**2
        c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance = R*c
        return Response({"result":distance})