from rest_framework import viewsets
from rest_framework.response import Response
import requests
from rest_framework.decorators import api_view
import os
from django.conf import settings  

class JCDecauxViewSet(viewsets.ViewSet):
    ## test in postman http://127.0.0.1:8000/jcd/lyon
    def getAllData(self, request, api_key, contractName):
        url = f"https://api.jcdecaux.com/vls/v1/stations?contract={contractName}&apiKey={os.getenv('API_KEY')}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print('failed to fetch data')
            return []

    def list(self, request, contract_name):
        
        data = self.getAllData(request, os.getenv('API_KEY'), contract_name)
        return Response(data)
    
    ## http://127.0.0.1:8000/getStations
    @api_view(['GET'])
    def getStations(request):
        url = f"https://api.jcdecaux.com/vls/v1/stations?apiKey={os.getenv('API_KEY')}"
        response = requests.get(url)
        if response.status_code == 200:
            return Response(response.json())
        else:
            print("Error getting stations")
            return Response([])
        
    ## http://127.0.0.1:8000/getParks
    @api_view(['GET'])
    def getParks(request):
        contract_name = "lyon"
        station_number = "18"
        url = f"https://api.jcdecaux.com/vls/v1/stations/{station_number}?contract={contract_name}&apiKey={os.getenv('API_KEY')}"
        params = {"apiKey": os.getenv('API_KEY')}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return Response(response.json())
        else:
            print('Error in fetching parks')
            return Response([])
        

        
        
