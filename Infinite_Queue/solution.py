import jwt

def encode_jwt(payload, secret):
    """
    Encodes a JWT with the given payload and secret.
    
    Args:
        payload (dict): The payload to encode in the JWT.
        secret (str): The secret key to sign the JWT.
    
    Returns:
        str: The encoded JWT.
    """
    return jwt.encode(payload, secret, algorithm='HS256')


user_id = input("Enter your user ID: ")
secret = input("Enter your secret key: ") # '4A4Dmv4ciR477HsGXI19GgmYHp2so637XhMC' was used in the challenge

header = {
  "alg": "HS256",
  "typ": "JWT"
}

payload = {
  "user_id": user_id,
  "queue_time": 1060462832.706898,
  "exp": 5348088372
}

token = encode_jwt(payload, secret)
print(f"Encoded JWT: {token}")