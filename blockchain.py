class Blockchain(object):
    def __init__(self):
        self.chain = [] #For Storing the blockchain
        self.current_transactions = [] #For storing the transcations

    def new_block(self):
        # Will create a new block and add it to the chain
        pass
    
    def new_transcation(self):
        # Adds a new transcation to the list of transcations
        pass

    @staticmethod #declared as static because its going to be used as a utility function
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # returns the last block in the chain
        pass