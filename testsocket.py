import socket,threading

def doListen():
    try:
        while True:
            b=s.recv(128)
            print(b.decode("utf-8"),end="", sep="")
    except ConnectionAbortedError:
        print("Connection aborted.")
    

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
