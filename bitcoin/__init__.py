class Address(object):
  def __init__(self,addr,port,services=1):
    self.addr = addr
    self.port = port
    self.services = services

class Block(object):
  def __init__(self,block_hash,prev_hash,merkle_root,timestamp,bits,nonce,version):
    self.hash = block_hash
    self.prev_hash = prev_hash
    self.merkle_root = merkle_root
    self.timestamp = timestamp
    self.bits = bits
    self.nonce = nonce
    self.version = version
    
class Transaction(object): 
  def __init__(self,tx_hash,version,lock_time):
    self.hash = tx_hash
    self.version = version
    self.lock_time = lock_time
    
    self.inputs = []
    self.outputs = []

class TransactionOutput(object): 
  def __init__(self,value,script):
    self.value = value
    self.script = script
  
class TransactionInput(object):  
  def __init__(self,out_hash,out_index,script,sequence):
    self.output_hash = out_hash
    self.output_index = out_index
    self.script = script
    self.sequence = sequence
