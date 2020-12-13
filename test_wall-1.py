import blocksmith
import json
import datetime as date
import hashlib
import ecdsa
from ecdsa import SigningKey, VerifyingKey
from ecdsa.util import sigencode_der, sigdecode_der
from ecdsa import BadSignatureError
import codecs
import datetime as date
from ellipticcurve.ecdsa import Ecdsa
from ellipticcurve.privateKey import PrivateKey
from ellipticcurve.publicKey import PublicKey
#import OpenSSl

print('start')

# Random Private Key 
kg = blocksmith.KeyGenerator()
kg.seed_input('the cybereum.io platform by ProBloCh')
key = kg.generate_key()
print('key')
print(key)


# Public key (ECDSA)
private_key_bytes = codecs.decode(key, 'hex')

public_key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1).verifying_key
# Get ECDSA public key
public_key_bytes = public_key.to_string()
public_key = codecs.encode(public_key_bytes, 'hex')

print('public_key_hex')
print(public_key)


sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) 
vk = sk.get_verifying_key()
#vkk = ecdsa.verifying_key()
print('private_key_sk')
print(sk)
print('public_key_vk')
print(vk)
#print(vkk)
sk_string = sk.to_string()
sk2 = SigningKey.from_string(sk_string, curve=ecdsa.SECP256k1)
sk_pem = sk.to_pem()
sk3 = SigningKey.from_pem(sk_pem)
#vk = sk.verifying_key
vk_string = vk.to_string()
vk_pem = vk.to_pem()
vk2 = VerifyingKey.from_pem(vk_pem)
# vk and vk2 are the same key

print('------')
print(sk)
print(sk_string.hex())
print(sk2.to_string().hex())
print(sk3.to_string().hex())
#print(len(sk_string.hex()))
print('------')

print(vk_string.hex())
print('------')

print("uncompressed: {0}".format(vk.to_string("uncompressed").hex()))
print("compressed: {0}".format(vk.to_string("compressed").hex()))

with open("user_private.pem", "wb") as f:
    f.write(sk_pem)
with open("user_public.pem", "wb") as f:
    f.write(vk_pem)

print('------PEM')
print(sk_pem)
print('------PEM')


#####SIGN######
with open("user_private.pem") as f:
    sk = SigningKey.from_pem(f.read())
with open("message.rtf", "rb") as f:
    message = f.read()
sig = sk.sign(message)
with open("signature", "wb") as f:
    f.write(sig)
#####SIGN######

#####VERIFY######
vk = VerifyingKey.from_pem(open("user_public.pem").read())
with open("message.rtf", "rb") as f:
    message = f.read()
with open("signature", "rb") as f:
    sig = f.read()
try:
    vk.verify(sig, message)
    print('good signature')
    x1 = vk.verify(sig, message)
    print(x1)
except BadSignatureError:
    print('BAD SIGNATURE')
#####VERIFY######

#####SIGN######
with open("user_private.pem") as f:
    sk = SigningKey.from_pem(f.read())
with open("ProBloCh1.json", "rb") as f:
    message = f.read()
sig = sk.sign(message)
with open("signature", "wb") as f:
    f.write(sig)
#####SIGN######

#####VERIFY######
vk = VerifyingKey.from_pem(open("user_public.pem").read())
with open("ProBloCh1.json", "rb") as f:
    message = f.read()
with open("signature", "rb") as f:
    sig = f.read()
try:
    vk.verify(sig, message)
    print('good signature')
    x1 = vk.verify(sig, message)
    print(x1)
except BadSignatureError:
    print('BAD SIGNATURE')
#####VERIFY######


#public_key = blocksmith.EthereumWallet._private_to_public(key)

# Wallet address (Ethereum style)
address = blocksmith.EthereumWallet.generate_address(sk_string.hex())
#address = blocksmith.EthereumWallet.generate_address(key)
print('address')
print(address)
# 0x1269645a46a3e86c1a3c3de8447092d90f6f04ed

checksum_address = blocksmith.EthereumWallet.checksum_address(address)
print('checksum_address')
print(checksum_address)
# 0x1269645a46A3e86c1a3C3De8447092D90f6F04ED


privateKey = PrivateKey()
print('private_key_sb')
print(privateKey)

publicKey = privateKey.publicKey()
print('public_key_sb')
print(publicKey)
print(PublicKey)
print(PublicKey.fromString)
#print(PublicKey.p)


message = "My test message"

# Generate Signature
signature = Ecdsa.sign(message, privateKey)
#signature = Ecdsa.sign(message, key)

# Verify if signature is valid
print(Ecdsa.verify(message, signature, publicKey))
#print(Ecdsa.verify(message, signature, public_key))

d = date.datetime.today()
part_key = {}
part_key['Key'] = []
part_key['Key'].append({
    'Bits': key,
#    'Hex': key,
    'Date': d.strftime("%d-%B-%Y %H:%M:%S")
})
part_key['Key'].append({
    'Bytes': str(public_key),
#    'Hex': public_key_hex,
    'Date': d.strftime("%d-%B-%Y %H:%M:%S")
})
part_key['Key'].append({
    'address': address,
    'style': 'Ethereum',
    'function': 'Keccak-256'
})

with open('part_key.json', 'w') as outfile:
    json.dump(part_key, outfile)