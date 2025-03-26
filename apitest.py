import requests

endpoint = "http://localhost:8000/api"

#first get request to /home/
# data = requests.get(endpoint + "/home/",params={"name":"Deepak"},json={"name":"dummy"})
# print(data.json())

choice = int(input("Enter the choice,1 for get,2 for post,3 for put,4 for patch:,5 for delete:"))

# if(choice == 1):
#     #api decorator/get
#     data = requests.get(endpoint + "/apidecorator/")
#     print(data.text)
# elif(choice == 2):
#     #api decorator/post
#     data = requests.post(endpoint + "/apidecorator/",json={"title":"Dummy Data","content":"Dummy Text","price":99})
#     print(data.text)


if(choice == 1):
    #api decorator/get (serializer)
    data = requests.get(endpoint + "/apidecoratorv2/")
    print(data.text)
elif(choice == 2):
    #api decorator/post (serializer)
    data = requests.post(endpoint + "/apidecoratorv2/",json={"title":"Dummy Data","content":"Dummy Text","price":99})
    print(data.text)
elif(choice == 3):
    #api decorator/post (serializer)
    data = requests.put(endpoint + "/apidecoratorv2/",json={"id":1,"title":"Updated Data","content":"Updated Content","price":99.22})
    print(data.text)
elif(choice == 4):
    #api decorator/post (serializer)
    data = requests.patch(endpoint + "/apidecoratorv2/",json={"id":1,"title":"Patched Data"})
    print(data.text)
else:
    data = requests.delete(endpoint + "/apidecoratorv2/",json={"id":1})
    print(data.text)