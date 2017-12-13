import requests
url='https://maps.googleapis.com/maps/api/geocode/json'
params={'sensor':'false','address':'Bangalore,India','key':'AIzaSyCLAcexA7mTT9vbLLwuMHJT0Zk6GbvLiMo'}
r=requests.get(url,params=params)
status=r.json()['status']
print(status)
if status == 'OK':
    d=dict(r.json())
    loc=d['results'][0]['geometry']['location']
    lat,lon=loc['lat'],loc['lng']
    print(lat,lon)
elif status == 'OVER_QUERY_LIMIT':
    print('Quota exceeded for API key')
elif status == 'ZERO_RESULTS':
    print('No results found, please verify input')
else:
    print('UNKNOWN_ERROR')

