import datetime
import hashlib
import json
from flask import Flask, jsonify
import random

class Block:
    
    
    def __init__(self,proof,previous_hash,id):
        self.proof = proof
        self.previous_hash = previous_hash
        self.id  = id
        self.time_of_creation = datetime.datetime.now()
        
    
class BlockChain:
    def __init__(self):
        self.chain_length = 1
        self.chain = [] 
        self.create_block(id = self.chain_length,proof = 1,previous_hash ='0')
    
    # Proof is the proof of work obtained after mining the block    
    # block is added to the chain after mining
    def create_block(self,proof,previous_hash,id):
            new_block = Block(proof,previous_hash,id) # create a new block to add
            self.chain.append(new_block)
            
    def get_last_block(self): # Get the last block in the chain
        return self.chain[-1]
    
    def generate_proof_of_work(self,prev_nonce): # returns the nonce value which will create a hash value less having 0000 prefix
        curr_nonce = 1 #keep generating a new nonce until we get the right hash
        while(1):
            random_hash = hashlib.sha256(str(curr_nonce**3 - prev_nonce**2).encode()).hexdigest() 
            #the sha256 algorithm will generate a 64 charactes long hexadecimal string
            # the encode method will .....
            if(random_hash[:4] == '0000'): # return the curr_nonce if the hash generated has 4 zeros
                return curr_nonce
            else:
                curr_nonce = random.randint(1,10**77)
    
    def encode_block(self,block):
        return str(block.proof) + str(block.previous_hash) + str(block.id) + str(block.time_of_creation)
    
    
    def hash_block(self,block): # take the entire block as input and return its hash value
        encoded_block = self.encode_block(block)
        return hashlib.sha256(encoded_block.encode()).hexdigest()

    def is_chain_valid(self): 
        #This function iterates over the chain and returns whether the chain is valid or not
        #validity is checked on the basis of two points
        # 1. The previous hash of each block is equal to the has of the previous block, generated on the fly
        # 2. The proof of work is valid
        
        #checking for point 1
        for i in range(1,len(self.chain)):
            mentioned_prev_hash = chain[i].previous_hash
            calculated_prev_hash = hash_block(chain[i-1])
            if(mentioned_prev_hash!=calculated_prev_hash):
                return False
        
        #checking for point 2
        for i in range(1,len(self.chain)):
            curr_proof_of_work = chain[i].proof
            prev_proof_of_work = chain[i-1].proof
            
            # we will recalculate the hash to see if it was valid
            random_hash = hashlib.sha256(str(curr_nonce**3 - prev_nonce**2).encode()).hexdigest() 
            #the sha256 algorithm will generate a 64 charactes long hexadecimal string
            # the encode method will .....
            if(random_hash[:4] != '0000'): # Invalid hash
                return False;
        # no validation issues found
        return True 
    
    
class Block:
    
    
    def __init__(self,proof,previous_hash,id):
        self.proof = proof
        self.previous_hash = previous_hash
        self.id  = id
        self.time_of_creation = datetime.datetime.now()
    def serialize(self):
        return {
            'id': self.id, 
            'proof': self.proof,
            'previous_hash':self.previous_hash,
            'time_of_creation': self.time_of_creation
        }   
    
class BlockChain:
    def __init__(self):
        self.chain_length = 1
        self.chain = [] 
        self.create_block(id = self.chain_length,proof = 1,previous_hash ='0')
    
    # Proof is the proof of work obtained after mining the block    
    # block is added to the chain after mining
    def create_block(self,proof,previous_hash,id):
            new_block = Block(proof,previous_hash,id) # create a new block to add
            self.chain.append(new_block)
            
    def get_last_block(self): # Get the last block in the chain
        return self.chain[-1]
    
    def generate_proof_of_work(self,prev_nonce): # returns the nonce value which will create a hash value less having 0000 prefix
        curr_nonce = 1 #keep generating a new nonce until we get the right hash
        while(1):
            random_hash = hashlib.sha256(str(curr_nonce**3 - prev_nonce**2).encode()).hexdigest() 
            #the sha256 algorithm will generate a 64 charactes long hexadecimal string
            # the encode method will .....
            if(random_hash[:4] == '0000'): # return the curr_nonce if the hash generated has 4 zeros
                return curr_nonce
            else:
                curr_nonce = random.randint(1,10**77)
    
    def encode_block(self,block):
        return str(block.proof) + str(block.previous_hash) + str(block.id) + str(block.time_of_creation)
    
    
    def hash_block(self,block): # take the entire block as input and return its hash value
        encoded_block = self.encode_block(block)
        return hashlib.sha256(encoded_block.encode()).hexdigest()

    def is_chain_valid(self): 
        #This function iterates over the chain and returns whether the chain is valid or not
        #validity is checked on the basis of two points
        # 1. The previous hash of each block is equal to the has of the previous block, generated on the fly
        # 2. The proof of work is valid
        
        #checking for point 1
        for i in range(1,len(self.chain)):
            mentioned_prev_hash = chain[i].previous_hash
            calculated_prev_hash = hash_block(chain[i-1])
            if(mentioned_prev_hash!=calculated_prev_hash):
                return False
        
        #checking for point 2
        for i in range(1,len(self.chain)):
            curr_proof_of_work = chain[i].proof
            prev_proof_of_work = chain[i-1].proof
            
            # we will recalculate the hash to see if it was valid
            random_hash = hashlib.sha256(str(curr_nonce**3 - prev_nonce**2).encode()).hexdigest() 
            #the sha256 algorithm will generate a 64 charactes long hexadecimal string
            # the encode method will .....
            if(random_hash[:4] != '0000'): # Invalid hash
                return False;
        # no validation issues found
        return True 

    
#Creating the Blockchain
blockchain = BlockChain()

from flask import Flask
app = Flask(__name__)

@app.route('/mine_block',methods=['GET'])
def mine_block():
    #first we will need to get the proof of work
    prev_block = blockchain.get_last_block()
    prev_nonce = prev_block.proof #the proof of work of the last block
    prev_hash = blockchain.hash_block(prev_block)
    mined_nonce = blockchain.generate_proof_of_work(prev_nonce)
    #once we have got the proof of work, we will generate the new block
    blockchain.chain_length += 1
    blockchain.create_block(mined_nonce,prev_hash,blockchain.chain_length)
    block = blockchain.chain[-1]
    # we have succesfully added a new block
    
    response = {"message":"Congratulations, you have mined a block!",
               "index":block.id,
                "previous_hash":block.previous_hash,
               "proof":block.proof,
               "time of creation":block.time_of_creation}
    return jsonify(response),200

@app.route('/get_chain',methods = ['GET'])
def get_chain():
    
    response = jsonify(eqtls=[e.serialize() for e in blockchain.chain],length = len(blockchain.chain))
    return response,200
    
app.run(host ='0.0.0.0',port = 5000)