# /usr/bin/python
# encoding:utf-8

class Widget:
     def __init__(self, size=(40, 40)):
         self._size = size

     def get_size(self):
         return self._size

     def resize(self, width, height):
         if width < 0 or height < 0:
             raise ValueError, 'illegal size'
         self._size = (width, height)

if __name__ == '__main__':
    widget = Widget()
    print widget.get_size()
    widget.resize(100,100)
    print widget.get_size()