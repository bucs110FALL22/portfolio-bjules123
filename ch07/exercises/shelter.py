import time
import uuid
class Animal: 
  def __int__(self, name, type):
    self.id = time.strftime("%d%M%S")
    self.name = name
    self.type = type
    self.arrived = time.strftime("%d/%m/%Y")
    self.adopted = None
  def self_adopted(self):
    self.arrived = time.shrftime("%d/%m/%Y")
 
  def __str__(self):
    result_str = f"{self.name}[{self.type}]"
    result_str += f"\narrived: {self.arrived}"
    result_str += f"\nadopted:{self.adopted}"
    return result_str
  def main():
    fido = Animal("fido", "cat")
    fido.set_adopted()
    print(fido)

main()