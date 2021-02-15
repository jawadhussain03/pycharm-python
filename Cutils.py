#!/usr/bin/env python
import subprocess
class Cutils():
  def __init__(self,command):
    self.command = command
  def get_output(self):
    p1 = subprocess.Popen([self.command],stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell=False)
    out,err = p1.communicate()
    if err:
      return "command exited with error"
    else:
       return out
if __name__ == '__main__':
  obj1 = Cutils('ls')
  x = obj1.get_output()
  print (x)

