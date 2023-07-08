import urllib.request
import json

# this module needs to be installed separately
# in PyCharm you can install the package if its not found!
import var_dump as vd

# get internet data
url = "https://edu.frostbit.fi/api/events/en"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")

# the needed data from internet is now in the "data" -variable!
data = json.loads(raw_data)
vd.var_dump(data)

# first event in the list
first_event = data[0]
vd.var_dump(first_event)
