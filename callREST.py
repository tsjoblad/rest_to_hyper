from getTokens import *
import json, requests, argparse

# Parameter customizaiton here
manualapicall = "https://slack.com/api/"
manualrequest = "users.list"
manualparams = "&pretty=1"
manualresttoken = get_REST_token()

def getArguments():
    '''
    parser = argparse.ArgumentParser(description='Input your API information')
    parser.add_argument('--apicall', '-a', required=True, help='base url for rest calls (e.g. https://slack.com/api/ + specific request here')
    parser.add_argument('--request', '-r', required=True, help='the specific call to try')
    parser.add_argument('--params', '-p', required=True, help='additional parameters for request (e.g. &lim=10&pretty=1')
    parser.add_argument('--token', '-t', required=True, help='access token with connection string (e.g. ?token=foorbar0000key')
    args = parser.parse_args()

    url = args.apicall + args.request + args.token + args.params
    print('Thank you kindly...)
    '''

    url = manualapicall + manualrequest + manualresttoken + manualparams
    print('Using manually set arguments...')

    return url

def getREST(url, apikeys):
    '''This function pings a REST API and returns hardcoded fields as a flat, specifically ordered, nested list with values and no keys.'''
    #api call setup
    print("Call: " + url)
    rawjson = requests.get(url)
    forhyper = []

    # parse response
    index = 0
    jsondict = json.loads(rawjson.text)
    baseobject = apikeys['baseobject']
    data = jsondict[baseobject]

    fieldlist = apikeys['fields']
    nestedfieldlist = apikeys['nestedfields']
    nestedkey = apikeys['nestedkey']
    
    fields = []
    nestedfields = []

    for i in fieldlist:
        fields.append(i[0])
        
    for j in nestedfieldlist:
        nestedfields.append(j[0])

    for response in data:
        forhyper.append([])
        for i in fields:
            try:
                vari = response[i]
            except:
                vari = None
            forhyper[index].append(vari)
        for j in nestedfields:
            try:
                varj = response[nestedkey][j]
            except:
                varj = None
            forhyper[index].append(varj)
        index += 1

    return forhyper