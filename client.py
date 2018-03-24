import socket
import sys


HOST, PORT = "localhost", 9999

while True:
    # SOCK_DGRAM is the socket type to use for UDP sockets
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("Pyrhon DB Menu\n")
    print("1. Find customer")
    print("2. Add customer")
    print("3. Delete customer")
    print("4. Update customer age")
    print("5. Update customer address")
    print("6. Update customer phone")
    print("7. Print report")
    print("8. Exit!\n")

    number = input("choose option from 1..8: ")
    print()

    if number == "1":
        print("Please enter the name you want to find")
        name = input("Customer name: ")
        data = number+"|"+name
    if number == "2":
        name = input("Please enter the name you want to add: ")
        age = input("Please enter the age: ")
        address = input("Please enter the address: ")
        phone = input("Please enter the phone number: ")
        data = number + "|" + name + "|" + age + "|" + address + "|" + phone
    if number == "3":
        print("Please enter the name you want to delete")
        name = input("Customer name: ")
        data = number + "|" + name
    if number == "4":
        print("Please enter the name you want to update")
        name = input("Customer name: ")
        age = input("Enter the new age of the customer: ")
        data = number + "|" + name + "|" + age
    if number == "5":
        print("Please enter the name you want to update")
        name = input("Customer name: ")
        address = input("Enter the new address of the customer: ")
        data = number + "|" + name + "|" + address
    if number == "6":
        print("Please enter the name you want to update")
        name = input("Customer name: ")
        phone = input("Enter the new phone number of the customer: ")
        data = number + "|" + name + "|" + phone
    if number == "7":
        data = number
        # print("** Python DB contents **")
    elif number == "8" :
        print("Quitting client")
        sys.exit(0)


    sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
    received = str(sock.recv(1024), "utf-8")

    print("Server response: {}".format(received))