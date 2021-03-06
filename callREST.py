import json, requests, argparse

# Parameter customizaiton here
def getArguments():
    '''Returns the URL of the GET request, through hardcoded parameters or CL argparse.'''

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

    url = "https://swapi.co/api/people/"
    print('Using harcoded URL...')

    return url

def getREST(url, apikeys):
    '''This function pings a REST API and returns hardcoded fields as a flat, specifically ordered, nested list with values and no keys.'''

    #api call setup
    print("Call: " + url)
    fieldlist = apikeys['fields']
    forhyper = []
    all_data = []
    fields = []
    index = 0

    # loop through paginated results and combine
    while url:
        per_request = requests.get(url)
        per_request_json = per_request.json()
        num_entries = len(per_request_json['results'])
        for i in range(0,num_entries):
            all_data.append(per_request_json['results'][i])
        url = per_request_json['next']
    
    # create list of fields from apikey
    for i in fieldlist:
        fields.append(i[0])

    # append results to nested list
    for record in all_data:
        forhyper.append([])
        for i in fields:
            try:
                vari = record[i]
            except:
                vari = None
            forhyper[index].append(vari)
        index += 1

    return forhyper

'''

note:
the list forhyper is set up as nested lists of values only.
the order is important, but will be automatically matched with the columns in the hyper table.
for reference, it should look like this:
    [[Value 1-A, Value 1-B], [Value 2-A, Value 2-B]]
where each of the nested lists is equivilant to a row of data.

'''