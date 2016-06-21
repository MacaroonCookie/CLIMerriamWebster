#!/usr/bin/env python

import requests
import xmltodict

class DictionaryApiRequest(object):

  def __init__(self, reference, key):
    self.reference = reference

    self.url = 'http://dictionaryapi.com/api/%[version]s/references/%[reference]s/%[format]/%[term]'
    self.version = 'v1'
    self.response_format = 'xml'
    self.parameters = {
        'key': key
    }

  def getResponse(self, term):
    url = self.url % {
        'version': self.version,
        'reference': self.reference,
        'format': self.response_format,
        'term': term,
    }

    response = requests.request('GET', url, self.parameters)

    if( not response.status_code == 200 ):
      raise Exception('Failed to retreive response from DictionaryAPI.com')

    return xmltodict.parse(response.text)


class DictionaryRequest(object):

  def __init__(self, api_key):
    self.key = api_key
    self.request = DictionaryApiRequest('dictionary', api_key)

  def define(self, term):
    result = self.request.getResponse(term)
    definitions = result['entry']['dt']

    return definitions

