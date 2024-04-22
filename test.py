import requests
#####################################################################################################
BASE = "http://89.33.85.88:3000/"
URL = BASE + "convert_key_from/nsec_hex/9571a568a42b9e05646a349c783159b906b498119390df9a5a02667155128028"
response = requests.get(URL)
print("Sending:", URL)
print(response.json())
#####################################################################################################
#####################################################################################################
BASE = "http://89.33.85.88:3000/"
URL = BASE + "convert_key_from/nsec_bech32/nsec1j4c6269y9w0q2er2xjw8sv2ehyrtfxq3jwgdlxj6qfn8z4gjsq5qfvfk99"
response = requests.get(URL)
print("Sending:", URL)
print(response.json())
#####################################################################################################
#####################################################################################################
BASE = "http://89.33.85.88:3000/"
URL = BASE + "convert_key_from/npub_hex/aa4fc8665f5696e33db7e1a572e3b0f5b3d615837b0f362dcb1c8068b098c7b4"
response = requests.get(URL)
print("Sending:", URL)
print(response.json())
#####################################################################################################
#####################################################################################################
BASE = "http://89.33.85.88:3000/"
URL = BASE + "convert_key_from/npub_bech32/npub14f8usejl26twx0dhuxjh9cas7keav9vr0v8nvtwtrjqx3vycc76qqh9nsy"
response = requests.get(URL)
print("Sending:", URL)
print(response.json())
#####################################################################################################