nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f','h',False],
    [1, 2, None],
]

class FlatIterator:
    def __init__(self, lst): # начальные установки, при создании объекта класса
        self.lst = lst
        self.cursor = -1
        self.list_len = len(self.lst)
    def __iter__(self): # каждый раз при вызове итератора устанавливаются значения атрибутов, для новой итерации
        self.cursor +=1
        self.nest_cursor = 0
        return self

    def __next__(self):
        if self.nest_cursor == len(self.lst[self.cursor]): # когда nest_cursor становится равен длине вложенного списка вызывается итератор с начальными установками, которые указаны в __iter__
          iter(self)
        if self.cursor == self.list_len:
          raise StopIteration
        self.nest_cursor += 1
        return self.lst[self.cursor][self.nest_cursor - 1]
      
def flat_generator(my_list):
    for elem in my_list:
        for el in elem:
            yield el

if __name__ == '__main__':
  for item in FlatIterator(nested_list):
        print(item)
  print('#'*20)
  flat_list = [item for item in FlatIterator(nested_list)]
  print(flat_list)
  print('#'*20)
  for item in flat_generator(nested_list):
        print(item)