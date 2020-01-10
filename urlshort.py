import webbrowser

class shorturl:
    url1={}
    id=1
    def makeshort(self,ourl):
        if ourl in self.url1:
            id=self.url1[ourl]
            short=id
        else:
            self.url1[ourl]=self.id
            short=self.id
            self.id +=1
        print("short url is: ",'tinyurl.com/'+str(short))
    
        return self.url1

url=input("Enter the url you want to short: ")
s=shorturl()
j=s.makeshort(url)
print("\n")
en=input("Enter shoturl to get original : ")
ent=en.split("/")
enter=int(ent[1])
for key in j:
    if j[key] == enter:
        url=key
        print("The original url is: ",key)
    

webbrowser.open(p)
