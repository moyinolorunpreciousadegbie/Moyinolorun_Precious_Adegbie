#!/usr/bin/env python3

## Leetcode 460. LFU Cache


class ListNode: 
	
	def __init__(self, key=0, val=0, freq = 0, prev=None, next=None): 
		self.key = key
		self.val = val
		self.freq = freq
		self.prev = prev
		self.next = next 
		
		
class LFUCache:
	
	def __init__(self, capacity: int):
		self.cap = capacity 
		self.lo = 0
		self.mp = {} 
		self.freq = []
		
	def _remove(self, node): 
		if self.lo == node.freq and self.freq[node.freq] == (node.prev, node.next): self.lo += 1
		node.next.prev = node.prev
		node.prev.next = node.next
		self.mp.pop(node.key)
		
	def _insert(self, node): 
		if node.freq == len(self.freq): 
			head = ListNode()
			tail = ListNode()
			head.next = tail
			tail.prev = head 
			self.freq.append((head, tail))
		head = self.freq[node.freq][0]
		
		
		"""
		# METHOD 1
		node.next = head.next
		node.prev = head
		head.next.prev = head.next = node 
		"""
		
		#self.mp[node.key] = node 
		
##################################################################
		"""
		# METHOD 2
		temp = head.next    ## or tail
		head.next = node
		node.prev = head
		node.next = temp 
		temp.prev = node
		""" 
		# METHOD 3
		tail = head.next  ###  REVERSE
		node.prev = tail.prev
		node.next = tail
		tail.prev.next = tail.prev = node
		
		"""
		# METHOD 4
		tail = head.next  ###  REVERSE
		temp = tail.prev  ## or head
		tail.prev = node
		node.next = tail
		node.prev = temp
		temp.next = node
        """
		
		
		self.mp[node.key] = node 
		
	def get(self, key: int) -> int:
		if key not in self.mp: return -1 
		node = self.mp[key] 
		self._remove(node)
		node.freq += 1
		self._insert(node)
		return node.val
	
	def put(self, key: int, value: int) -> None:
		if self.get(key) == -1: 
			if self.cap == 0 and self.freq: 
				self.cap += 1
				node = self.freq[self.lo][1].prev 
				self._remove(node)
			if self.cap: 
				self.cap -= 1
				node = ListNode(key, value)
				self._insert(node)
				self.lo = 0  
		else: 
			node = self.mp[key]
			node.val = value
			
			
			
cache = LFUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))
cache.put(3, 3)
print(cache.get(2))
cache.put(4, 4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))	