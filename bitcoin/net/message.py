import hashlib
import struct
import socket
import time

magic = b'\xF9\xBE\xB4\xD9'

class reader:
  def __init__(self,s):
    self.buffer = b''
    self.socket = s
  
  def buffered_read(self,length):
    while len(self.buffer) < length:
      buffer = self.socket.recv(4096)
      if buffer == b'':# this signals the other end has hung up
        raise socket.error
      self.buffer += buffer
    ret = self.buffer[:length]
    self.buffer = self.buffer[length:]
    return ret
  
  def read(self):
    m = self.buffered_read(4)
    if m != magic:
      raise Exception("Magic value wrong "+str(m))
    
    command = self.buffered_read(12).decode('ascii').strip('\x00')
    length = struct.unpack('<I',self.buffered_read(struct.calcsize('<I')))[0]
    
    if command == 'version' or command == 'verack':
      checksum = None
    else:
      checksum = self.buffered_read(4)
    
    p = self.buffered_read(length)
    
    if checksum:
      if hashlib.sha256(hashlib.sha256(p).digest()).digest()[:4] != checksum:
        raise Exception("checksum failure")
    
    return (command,p)
    
def send(s,command,p):
  if len(command) > 12:
    raise Exception("command too long")
    
  if command == b'version' or command == b'verack':
    checksum = None
  else:
    checksum = hashlib.sha256(hashlib.sha256(p).digest()).digest()[:4]
  
  b = b''
  b += magic
  
  b += command
  b += b'\x00'*(12-len(command))
  
  b += struct.pack('<I',len(p))
  
  if checksum:
    b += checksum
  
  b += p
  s.sendall(b)

    
    
    
