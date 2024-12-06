from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def serve_polisen_xml(request):
    with open('polisen.xml', 'r') as f:
        xml_data = f.read()
        print(xml_data)
    return HttpResponse(xml_data, content_type='application/xml')