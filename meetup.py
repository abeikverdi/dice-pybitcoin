import json
import os
import random
import unittest

import bitcoin.ripemd as ripemd
from bitcoin import *


#Your private key in base 6 using dice (It should have 99 characters)
priv = '130112525115535035111251342335241405104544024334003003345341045154510344125350551514550223411534145'
priv = int(str(priv), 6)

#Your public key
pub = privkey_to_pubkey(priv)

#Your address
addr = pubkey_to_address(pub)
print addr