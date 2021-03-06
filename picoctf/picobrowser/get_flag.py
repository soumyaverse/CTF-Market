import requests

header={'User-Agent':'picobrowser'}
resp = requests.get('http://jupiter.challenges.picoctf.org:26704/flag',headers=header)
print(resp.text)