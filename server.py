import socketserver
import socket

f = open('data.txt', 'r')
DB = {}
for line in f:
    k, v, a, b = line.strip().split('|')
    DB[k.strip()] = k.strip() + "|" + v.strip() + "|" + a.strip() + "|" + b.strip()
f.close()

def findCustomer(customerName):
    print("I am finding a customer " + customerName)
    result = DB.get(customerName, customerName + " not found in database")
    print(result)
    return  result


def addCustomer(customerName, customerAge, customerAddress, customerPhone):
    print("I am adding a customer " + customerName)
    if customerName in DB:
        return("Customer already exist!")
    else:
        DB.update({customerName: customerName + "|" + customerAge + "|" + customerAddress + "|" + customerPhone})
        print(DB)
        return("Customer has been added")

def delCustomer(customerName):
    print("I am deleting a customer")
    if customerName in DB:
        del DB[customerName]
        print(DB)
        return("Customer "+ customerName + " has been deleted")
    else:
        return("The customer does not exist")


def updateAge(customerName, customerAge):
    print("I am updating the age")
    if customerName in DB:
        NewDb = DB[customerName].split("|")
        DB[customerName] = customerName + "|" + customerAge + "|" + NewDb[2] + "|" + NewDb[3]
        print(DB)
        return("The age has been updated!")
    else:
        return("The customer does not exist")


def updateAddress(customerName, customerAddress):
    print("I am updating the address")
    if customerName in DB:
        NewDb = DB[customerName].split("|")
        DB[customerName] = customerName + "|" + NewDb[1] + "|" + customerAddress + "|" + NewDb[3]
        print(DB)
        return("The address has been updated!")
    else:
        return("The customer does not exist")

def updatePhone(customerName, customerPhone):
    print("I am updating the phone")
    if customerName in DB:
        NewDb = DB[customerName].split("|")
        DB[customerName] = customerName + "|" + NewDb[1] + "|" + NewDb[2] + "|" + customerPhone
        print(DB)
        return("The phone has been updated!")
    else:
        return("The customer does not exist")


def printReport():
    # store in somewhere as a list
    list = ['** Python DB contents **']
    print("I am printing the whole thing")
    for key, v in sorted(DB.items()):
        print ("%s" % (v))
        list.append(v)
    print(("\n").join(list))
    return(("\n").join(list))

class MyUDPHandler(socketserver.BaseRequestHandler):

    def handle(self):

        data = self.request[0].strip().decode("utf-8")
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        request = data.split("|")

        if request[0] == "1":
            response = findCustomer(request[1])
        elif request[0] == "2" :
            response = addCustomer(request[1], request[2], request[3], request[4])
        elif request[0] == "3":
            response = delCustomer(request[1])
        elif request[0] == "4":
            response = updateAge(request[1], request[2])
        elif request[0] == "5":
            response = updateAddress(request[1], request[2])
        elif request[0] == "6":
            response = updatePhone(request[1], request[2])
        elif request[0] == "7":
            response = printReport()
        else:
            print("Cannot handle request")

        socket.sendto(bytes(response + "\n","utf-8"), self.client_address)


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()