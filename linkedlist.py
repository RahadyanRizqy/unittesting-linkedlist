class Node:
    def __init__(self, data):
        self.data = data
        self.then = None

class LinkedList:
    def __init__(self, *datas):
        self.init = None
        if datas:
            self.datas = datas
            self.__Append()
        else:
            pass
    
    def __iter__(self):
        if self.init is None:
            yield
        element = self.init
        while element is not None:
            yield element.data
            element = element.then
    
    def __str__(self):
        return "< " + self.__str_recursive(self.init) + " >"
    
    def __len__(self, element=None, n=1):
        if element is None:
            element = self.init
        if element:
            if element.then is None:
                return n
            else:
                return self.__len__(element.then, n+1)
        else:
            return 0 

    def __getitem__(self,index):
        return self.__GetItemByIndex(index)

    def __str_recursive(self, node):
        if node is None:
            return ""
        elif node.then is None:
            return str(node.data)
        else:
            return str(node.data) + ", " + self.__str_recursive(node.then)
    
    def __GetItemByIndex(self, index):
        if self.init is None or index > self.__len__():
            raise IndexError('Index out of range')

        current_node : Node = self.init
        while index > 0:
            current_node = current_node.then
            index -= 1
        return current_node.data     
    
    def insertAtFront(self, item):
        Element = Node(item)
        Element.then = self.init
        self.init = Element

    def insertAtEnd(self, item, element=None):
        if self.init is None:
            self.init = Node(item)
            return
        if element is None:
            element = self.init
        if element.then is None:
            element.then = Node(item)
        else:
            self.insertAtEnd(item, element.then)
    
    def listPop(self, element=None):
        if self.init is None:
            print("List has no element")
            return
        if element is None:
            element = self.init
        if element:
            if element.then.then is None:
                element.then = None
            else:
                self.listPop(element.then)
        else:
            print('No element')
    
    def getIndex(self, item, current=None, index=0):
        if current is None:
            current = self.init

        if current is None:
            return -1
        elif current.data == item:
            return index
        else:
            return self.getIndex(item, current.then, index+1)

    def __Append(self):
        for i in self.datas:
            self.insertAtEnd(i)

# sc: pekerjaan sendiri dari tugas akhir struktur data semester 3 dari repository pribadi
# https://github.com/RahadyanRizqy/TugasTA-StrukturData

x = LinkedList(1,2,3,4,5,6,7,8)
print(x[5])