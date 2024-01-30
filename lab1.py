class List:
   def __init__(self, elements):
      self._elements = elements
   
   def __add__(self, other):
      if isinstance(other, List):
         return List(self._elements + other._elements)
      else:
         raise TypeError("Unsupported operand type for +")
   
   def __neg__(self):
      self._elements.pop(0)
      return self
         
   def __eq__(self, other):
      if isinstance(other, List):
         return self._elements == other._elements
      else:
         return False

list1 = List([1, 2, 3])
list2 = List([4, 5, 6])

print("First list:", list1._elements)
print("Second list:", list2._elements)

combined_list = list1 + list2
print("Combined list:", combined_list._elements)

modified_list = -list1
print("Modified List:", modified_list._elements)

print("Equality check list1 and list2:", list1 == list2)
