import socket,threading,select

def doListen():
    try:
        while True:
            (readlist,writelist,exceptlist)=select.select([s],[],[s],1) 
            if (s in readlist):
                b=s.recv(128)
                print(b.decode("utf-8"),end="", sep="")
            elif (s in exceptlist):
                print("Exception on socket")
                break

    except Exception as err:
        print("Connection aborted.",err)
    

print("Connecting...")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("srtmoo.net",8492))
    x=threading.Thread(target=doListen)
    x.start()
    print("Connected")
    while True:
        cmd=input(">")
        if cmd=="/quit":
            break
        s.send((cmd+"\n").encode("utf-8"))

print("Done")    
