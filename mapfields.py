def createdict():
    '''This function takes manually mapped parameters to define table structure for extract'''

    # name your extract table
    tablename = 'star_wars_characters'

    fields = [
        #['api key name', 'hyper column name', 'hyper column type']
        ['birth_year', 'Birth Year', 'text'],
        ['eye_color', 'Eye Color', 'text'],
        ['gender', 'Gender', 'text'],
        ['hair_color', 'Hair Color', 'text'],
        ['height', 'Hieght', 'text'],
        ['homeworld', 'Homeworld', 'text'],
        ['mass', 'Mass (kg)', 'text'],
        ['name', 'Name', 'text']
    ]

    apikeys = {
        'tablename' : tablename,
        'fields' : fields,
    }

    print("Field dictionary created...")
    return apikeys


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


'''
EXAMPLE NESTED API RESPONSE WITH SAMPLE CODE

Sample Nested JSON Response
{
    "ok": true,
    "offset": "UHS20KECU",
    "members": [                        <--------- baseobject = 'members'
        {
            "id": "USLACKBOT",              <--------- fields = 'id', 'team_id', etc.
            "team_id": "THC4XFL9Z",
            "name": "slackbot",
            "deleted": false,
            "color": "757575",
            "real_name": "Slackbot",
            "tz": null,
            "tz_label": "Pacific Standard Time",
            "tz_offset": -28800,
            "profile": {                <--------- nestedkey = 'profile'
                "title": "",                <--------- nestedfields = 'title', 'phone', etc.
                "phone": "",
                "skype": "",
                "real_name": "Slackbot",
            },
            "is_admin": false,
            "updated": 0
        },
        {

            ...more responses here...

        },
    ],
    "cache_ts": 1583189671,
    "response_metadata": {
        "next_cursor": "dXNlcjpVSFMyMEtFQ1U="
    }
}


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


Sample Nested Setup:

    tablename = 'slackusers'

    # use this to denote what member of the json response payload to interate through
    baseobject = 'members'
    nestedkey = 'profile'
    
    fields = [
        #['api key name', 'hyper column name', 'hyper column type']
        ['name', 'username', 'text'],
        ['id', 'id', 'text'],
        ['team_id', 'team_id', 'text'],
        ['deleted', 'deleted', 'bool'],
        ['tz_label', 'tz_label', 'text'],
        ['is_admin', 'is_admin', 'bool'],
        ['is_owner', 'is_owner', 'bool'],
        ['updated', 'updated', 'int']
    ]

    # when a field exists in a nested structure (like 'profile' above) use this logic
    # you may need to introduce a second-level nesting or implement this twice
    nestedfields = [
        #['[nestedkey][api key name]', 'hyper column name', 'hyper column type']
        ['email', 'email', 'text'],
        ['display_name', 'display_name', 'text'],
        ['title', 'title', 'text'],
    ]


    apikeys = {
        'tablename' : tablename,
        'baseobject' : baseobject,
        'nestedkey' : nestedkey,
        'fields' : fields,
        'nestedfields' : nestedfields
    }


'''