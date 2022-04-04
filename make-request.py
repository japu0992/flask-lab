# ~~~ make-request.py ~~~
import requests

# route 1 -- ping
def call_ping_route():
  '''this gets the route to the ping page'''
  r = requests.get('http://localhost:5555/ping')# make the request
  return r

# route 2 -- random word
def call_random_word_route():
  '''this gets the route to the word page'''
  r = requests.get('http://localhost:5555/word') # make the request
  return r

# route 3 -- string count
def call_string_count():
   '''this gets the post route to the string_count page'''
   r = requests.post('http://localhost:5555/string-count') # make the request
   return r

route_callers = [
  call_ping_route,
  call_random_word_route,
  call_string_count
 ]

for call_route in route_callers:
    '''calls all above'''
 r = call_route()
 r.status_code # first, check r for errors
 data = r.json()
 print(data) # print the response
