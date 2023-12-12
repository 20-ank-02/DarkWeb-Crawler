# from stem.control import Controller

# with Controller.from_port(port = 9051) as controller:
#   controller.authenticate()  # provide the password here if you set one

#   bytes_read = controller.get_info("traffic/read")
#   bytes_written = controller.get_info("traffic/written")

#   print("My Tor relay has read %s bytes and written %s." % (bytes_read, bytes_written))
  
  
  # import torch
# from transformers import AutoTokenizer, RobertaForSequenceClassification

# tokenizer = AutoTokenizer.from_pretrained("cardiffnlp/twitter-roberta-base-emotion")
# model = RobertaForSequenceClassification.from_pretrained("cardiffnlp/twitter-roberta-base-emotion")


# inputs = tokenizer("I hate putin", return_tensors="pt")

# with torch.no_grad():
#     logits = model(**inputs).logits

# predicted_class_id = logits.argmax().item()
# # predicted_class_ids = torch.arange(0, logits.shape[-1])[torch.sigmoid(logits).squeeze(dim=0) > 0.5]
# print(model.config.id2label[predicted_class_id])

# with torch.no_grad():
#     logits = model(**inputs).logits

import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import base64

desired = 'ghj'
while True:
    rsa_key = rsa.generate_private_key(public_exponent = 0x10001, key_size = 0x400, backend = default_backend())
    public_key = rsa_key.public_key()
    public_bytes = public_key.public_bytes(encoding = serialization.Encoding.DER, format = serialization.PublicFormat.PKCS1)
    sha_1 = hashlib.sha1()
    sha_1.update(public_bytes)
    digest = sha_1.digest()
    half_digest = digest[:10]
    b32 = base64.b32encode(half_digest).decode('utf-8').lower()
    # we got what we desired
    if b32.startswith(desired):
        # print private key
        print(rsa_key.private_bytes(encoding = serialization.Encoding.PEM, format = serialization.PrivateFormat.TraditionalOpenSSL, encryption_algorithm=serialization.NoEncryption()).decode('utf-8'))
        # print onion address
        print(b32 + '.onion')
        break
