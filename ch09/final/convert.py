import requests
from celebs import *
class networthAPI():
  def __init__(self,api_url,want,networth):
   '''
   initializes class
   api_url: (var) adds want value and networth value to url
   '''
    self.api_url = 'https://api.api-ninjas.com/v1/convertcurrency?want='+ want + '&have=USD' + '&amount=' + networth
  def get(self,want,networth, api_url):
    '''
   want/networth (var): sets want and networth value
   '''
    self.want = want
    self.networth = networth
    response = requests.get(self.api_url, headers={'X-Api-Key': '4TbNu2L1ZjCUambF03wvVA==j2ZrwuVU8qRHBFXE'})
     
    if response.status_code == requests.codes.ok:
          response = response.text
          print(response[2:24])
          
    else:
          print("Error:", response.status_code, response.text)
        
          