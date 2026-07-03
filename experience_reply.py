import random 
from collections import deque

class Replay_memory():
    def __init__(self , maxlen , seed = None ):         # creating FiFo queue : Experience reply
        self.memory = deque([] , maxlen = maxlen)
    
    def append(self , next_exp):
        self.memory.append(next_exp)

    def sample(self , sample_size):
        return random.sample(self.memory , sample_size)
    
    def __len__(self):
        return len(self.memory)  # current buffer size