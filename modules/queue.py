class Queue(object):
  def __init__(self, items = None):
    if items is None:
      self.a = []
    else:
      self.a = items
 
  def enqueue(self, b):
    self.a.insert(0, b)
 
  def dequeue(self):
    return self.a.pop()
 
  def isEmpty(self):
    return self.a == []
 
  def size(self):
    return len(self.a)
