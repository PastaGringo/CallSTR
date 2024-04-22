# CallSTR
CallSTR is python flask Web API with the goal to serve Nostr content over HTTP API

## Getting started

### Installation
```
git clone https://github.com/PastaGringo/CallSTR.git && cd CallSTR
pip install -r requirements.txt
```
### Usage
```
python3 main.py
```
Flask will listen on 0.0.0.0:3000 (including your external IP address). You can change the port into main.py file:
```
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
```

### Testing
```
python3 test.py
```
Output:
```
Sending: http://0.0.0.0:3000/convert_key_from/nsec_hex/9571a568a42b9e05646a349c783159b906b498119390df9a5a02667155128028
nsec1j4c6269y9w0q2er2xjw8sv2ehyrtfxq3jwgdlxj6qfn8z4gjsq5qfvfk99
Sending: http://0.0.0.0:3000/convert_key_from/nsec_bech32/nsec1j4c6269y9w0q2er2xjw8sv2ehyrtfxq3jwgdlxj6qfn8z4gjsq5qfvfk99
9571a568a42b9e05646a349c783159b906b498119390df9a5a02667155128028
Sending: http://0.0.0.0:3000/convert_key_from/npub_hex/aa4fc8665f5696e33db7e1a572e3b0f5b3d615837b0f362dcb1c8068b098c7b4
npub14f8usejl26twx0dhuxjh9cas7keav9vr0v8nvtwtrjqx3vycc76qqh9nsy
Sending: http://0.0.0.0:3000/convert_key_from/npub_bech32/npub14f8usejl26twx0dhuxjh9cas7keav9vr0v8nvtwtrjqx3vycc76qqh9nsy
aa4fc8665f5696e33db7e1a572e3b0f5b3d615837b0f362dcb1c8068b098c7b4
```
### Stopping Flask
```
sudo netstat -tulnp | grep :3000
tcp        0      0 0.0.0.0:3000            0.0.0.0:*               LISTEN      1248569/python3
```
```
kill 1248569
```
