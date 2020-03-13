import pytest
import requests

## To get all emp details

res_obj = requests.get('http://127.0.0.1:5000/get')
print('\n response code is :', res_obj.status_code)
print('\n EMP details are  :', res_obj.json())


## To create new emp record
r = requests.post('http://127.0.0.1:5000/create', json={"DID":555})
print('\n response code is :', r.status_code)
print('\n POST DATA is :', r.json())
assert r.json()['DID'] == 555, ' DID not created '

## To Update emp 
r = requests.put('http://127.0.0.1:5000/update', json={"DID":999})
print('\n update is :', r.text)


## To Delete emp
r = requests.delete('http://127.0.0.1:5000/delete', json={"DID":"50000"})
print('\n response code is :', r.status_code)
print('\n Deleted is :', r.text)

