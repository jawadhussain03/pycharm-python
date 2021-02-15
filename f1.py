#!/usr/bin/env python
class Example():
  def __init__(self,first,last,role):
    self.first = first
    self.last = last
    self.role = role
  @property
  def fullname(self):
    full_name =self.first + ' ' + self.last
    return full_name
  @classmethod
  def test(cls,String):
     first,last,role= String.split(' ')
     return cls(first,last,role)
e1 = Example.test('Jawad Hussain developer')
print (e1.first)
print (e1.last)
print (e1.role)
p1 = e1.fullname
print (p1)
e2 = Example.test('test user1 testing')
print (e2.first)
print (e2.last)
print (e2.role)
print (e2.fullname)
e3 = Example('test','user2','testing')
print (e3.last)
print (e3.role)
print (e3.first)