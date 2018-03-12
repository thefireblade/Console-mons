import json
import urllib2

def reqData(strTag):
    pokeApi = 'http://pokeapi.co/api/v2/' + strTag + '/'
    try:
        req = urllib2.Request(pokeApi, headers = {'User-Agent' : "PokeHelper", 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' })
        json_object = urllib2.urlopen(req)
        data = json.load(json_object)
    except:
        print('Something went wrong when obtaining data')
    
    return data
def reqMoveData(strTag):
    pokeApi = strTag
    try:
        req = urllib2.Request(pokeApi, headers = {'User-Agent' : "PokeHelper", 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' })
        json_object = urllib2.urlopen(req)
        data = json.load(json_object)
    except:
        print('Something went wrong when obtaining data')
    
    return data

def getPoke(num):
    return reqData('pokemon/' + str(num))
    