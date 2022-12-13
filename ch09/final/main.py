import celebs 
import convert

def main():
  
  person = celebs.celebrityAPI(inputname,"https://api.api-ninjas.com/v1/celebrity?name={}".format(inputname))
  person.get(inputname,"https://api.api-ninjas.com/v1/celebrity?name={}") 
  conversion = convert.networthAPI('https://api.api-ninjas.com/v1/convertcurrency?want='+ inputwant + '&have=USD'  + '&amount=' + networth,inputwant,networth)
  conversion.get(inputwant,networth,'https://api.api-ninjas.com/v1/convertcurrency?want='+ inputwant + '&have=USD'  + '&amount=' + networth)


inputname = input("Which celebrity's networth would you like to see")
inputwant = str(input('Type 3 letter currency'))

person = celebs.celebrityAPI(inputname,"https://api.api-ninjas.com/v1/celebrity?name={}".format(inputname))
networth =  person.getnetworth('',"https://api.api-ninjas.com/v1/celebrity?name={}",inputname) 
#inputamount = str(input('Amount? '))
main()
