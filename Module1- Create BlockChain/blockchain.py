#Module- 1 Create a Blockchain 
# to be installed:
# Flask=0.12.2 pip install Flask=0.12.2
#PostMan HTTP client: http://getpostman.com

"""
@author: Tazbir
"""

# importing library
import datetime
import hashlib
import json
from flask import Flask, jsonify

# part 1 building block chain
class Blockchain:
    def __init__(self):
        self.chain=[]
        self.create_block(proof=1,previous_hash='0')# creating genesis block
        
    def create_block(self, proof,previous_hash):
        block= {'index': len(self.chain)+1,
                'timestamp': str(datetime.datetime.now()),
                'proof': proof,
                'previous_hash': previous_hash}# creating dictionary
        self.chain.append(block)
        return block
    
    def get_previous_block(self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        new_proof=1 #we are taking 1 because we need to iterate by 1
        check_proof= False
        
        while check_proof is False:
            #leading zero problem
            hash_operation= hashlib.sha256(str(new_proof**2 + previous_proof**2).encode()).hexdigest()# making it complex to proof
            if hash_operation[:4]=='0000':
                check_proof=True
            else:
                new_proof += 1
        return 
    
    def hash(self, block):
        encoded_block= json.dumps(block,sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest() # returns cryptographic block
    
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index=1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof= previous_block['proof'] #to be updated at the end of this loop
            proof= block['proof']
            hash_operation= hashlib.sha256(str(proof**2 + previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block # setting the new prev block
            block_index +=1
            
        return True
            
         
