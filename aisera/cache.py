from abc import ABC
from collections import OrderedDict
from typing import Any

SIZE = 100


class Cache(ABC):
    
    def get(self, key: str) -> Any:
        pass

    def put(self, key: str, value: Any) -> None:
        pass

    def remove(self, key: str) -> None:
        pass


ordered_dict = OrderedDict()
ordered_dict[1] = "one"
ordered_dict[2] = "two"

{1: "one", 2: "two"}

# If we were to iterate through ordered_dict, then the keys would be [2, 1]

print(ordered_dict[1])

# If we were to iterate through ordered_dict, then the keys should be [1, 2]

ordered_dict[3] = "three"

{1: "one", 3: "three"}

# If we were to iterate through ordered_dict, then the keys should be [3, 1]

OrderedDict.move_to_start(key)
	Moves key to start (most recently used).

OrderedDict.pop()
	Removes the least-recently-used key from OrderedDict and returns the key.

class LruCache(Cache):
    """Least-recently used cache."""

    def __init__(self, size: int = SIZE):
        self.size = size
        self.store = OrderedDict()
    
    def get(self, key: str): -> Any:
        # check the len of dict
       If (self.store == 0):
	print(“The cache is empty”)
       Else:
             If (self.store[key] != 0):
                       # TODO: Use move_to_end to update self.store
self.store.move_to_start(key)
		Return self.store[key]
             Else:
                   Return “key not found”

    def put(self, key: str, value: Any) -> None:
        # TODO Shifa: Implement put method
        if(self.store <= size):
if(self.store==size):
            	remove = self.store.pop() #returns the least used key
            Self.store[key] = value
            self.store.move_to_start(key)
 
            
            
		
	
	

    def remove(self, key: str) -> None:
        # TODO Shifa: If the key is in the cache, remove it. Else raise KeyNotFound exception.




