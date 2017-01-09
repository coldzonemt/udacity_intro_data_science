import json
import requests
import pprint

def api_get_request(url=None):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain. The grader will supply the URL as an argument to
    # the function; you do not need to construct the address or call this
    # function in your grader submission.
    # 
    # Once you've done this, return the name of the number 1 top artist in
    # Spain. 

    # see http://www.last.fm/api/rest for docs
    # example url for this assignment: JSON: /2.0/?method=geo.gettopartists&country=spain&api_key=YOUR_API_KEY&format=json
    # My attempt to pretty this didn't work. wah wah. 
    # api_key = '2461efb389623cad62525d4433326de5'
    # api_shared_secret = '03056a2131f01a306fcc01c93d218054'

    # last_fm_root_url = 'http://ws.audioscrobbler.com/2.0/'

    # method = 'geo.gettopartists'
    # country = 'spain'
    # format = 'format=json'

    # url_request = last_fm_root_url+'/?method='+method+'&country='+country+'&api_key='+api_key+'&format='+format

    url = 'http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key=2461efb389623cad62525d4433326de5&format=json'

    data = requests.get(url).text
    print type(data)
    data = json.loads(data)
    print type(data)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data)
    print data['topartists']['artist'][0]['name']

    return  data['topartists']['artist'][0]['name']

api_get_request()