from flask import Flask
from flask_restful import Api, Resource, reqparse
from datetime import timedelta
import time
from nostr_protocol import Keys, SecretKey, PublicKey

app = Flask(__name__)
api = Api(app)

def fn_Convert_from_nsec_hex(nsec_hex):
    print("Converting:", nsec_hex)
    secret_key = SecretKey.from_hex(nsec_hex)
    nsec_bech32 = secret_key.to_bech32()
    print("Returning nsec_bech32:", nsec_bech32)
    return nsec_bech32

def fn_Convert_from_nsec_bech32(nsec_bech32):
    print("Converting:", nsec_bech32)
    secret_key = SecretKey.from_bech32(nsec_bech32)
    nsec_hex = secret_key.to_hex()
    print("Returning nsec_hex:", nsec_hex)
    return nsec_hex

def fn_Convert_from_npub_hex(npub_hex):
    print("Converting:", npub_hex)
    public_key = PublicKey.from_hex(npub_hex)
    npub_bech32 = public_key.to_bech32()
    print("Returning npub_bech32:", npub_bech32)
    return npub_bech32

def fn_Convert_from_npub_bech32(npub_bech32):
    print("Converting:", npub_bech32)
    public_key = PublicKey.from_bech32(npub_bech32)
    npub_hex = public_key.to_hex()
    print("Returning npub_hex:", npub_hex)
    return npub_hex

class Convert_from_nsec_hex(Resource):
    def get(self, nsec_hex):
        print()
        print("nsec_hex key received:", nsec_hex)
        return fn_Convert_from_nsec_hex(nsec_hex)

class Convert_from_nsec_bech32(Resource):
    def get(self, nsec_bech32):
        print()
        print("nsec_bech32 key received:", nsec_bech32)
        return fn_Convert_from_nsec_bech32(nsec_bech32)

class Convert_from_npub_hex(Resource):
    def get(self, npub_hex):
        print()
        print("npub_hex key received:", npub_hex)
        return fn_Convert_from_npub_hex(npub_hex)

class Convert_from_npub_bech32(Resource):
    def get(self, npub_bech32):
        print()
        print("npub_bech32 key received:", npub_bech32)
        return fn_Convert_from_npub_bech32(npub_bech32)       

api.add_resource(Convert_from_nsec_hex, "/convert_key_from/nsec_hex/<string:nsec_hex>")
api.add_resource(Convert_from_nsec_bech32, "/convert_key_from/nsec_bech32/<string:nsec_bech32>")
api.add_resource(Convert_from_npub_hex, "/convert_key_from/npub_hex/<string:npub_hex>")
api.add_resource(Convert_from_npub_bech32, "/convert_key_from/npub_bech32/<string:npub_bech32>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)