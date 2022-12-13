import requests
class celebrityAPI():
    
    def __init__(self,name,net_worth):
      self.api_url = "https://api.api-ninjas.com/v1/celebrity?name={}".format(name)
   '''
   intializes class
   '''

    def get(self,name,api_url):
   '''
   name (var): pulls name from user
   api_url (var): uses url from init
   '''
      self.name = name
      response = requests.get(self.api_url,headers={'X-Api-Key': '4TbNu2L1ZjCUambF03wvVA==j2ZrwuVU8qRHBFXE'})
      response = response.text
      number = 14 + len(self.name)
      number2 = number + 22
      print(response[number:number2])
      networth = response[number2-9:number2]
      print(networth)      
    def getnetworth(self,networth,api_url,name):
      self.networth = networth
      response = requests.get(self.api_url,headers={'X-Api-Key': '4TbNu2L1ZjCUambF03wvVA==j2ZrwuVU8qRHBFXE'})
      if response.status_code == requests.codes.ok:
        response = response.text
        self.name = name
        #number = 12 + inputname
        number = 14 + len(self.name)
        number2 = number + 22
        networth = response[number2-9:number2]
        return networth    
      else:
        print("Error:", response.status_code, response.text)
  
      
     
      
  