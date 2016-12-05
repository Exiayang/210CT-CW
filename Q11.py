class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None
 
class List(object):
    def __init__(self):
          self.head=None
          self.tail=None
    def insert(self,n,x):
        if n!=None:
            x.next=n.next
            n.next=x
            x.prev=n
            if x.next!=None:
                x.next.prev=x              
        if self.head==None:
            self.head=self.tail=x
            x.prev=x.next=None
        elif self.tail==n:
            self.tail=x
    def display(self):
        values=[]
        n=self.head
        while n!=None:
            values.append(str(n.value))
            n=n.next
            print ("List: ", ",".join(values))
         
if __name__ == '__main__':
    l=List()
    y = 9
    x = 5
    l.insert(None, Node(x))
    l.insert(l.head,Node(7))
    l.insert(l.head,Node(y))
    l.display()

"""
m = len(1)/2
l(m).prev.next = l(m).next
l(m).next.prev = l(m).prev
print ("List: ", ",".join(values))
"""
