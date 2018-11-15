try:
    from http.server import HTTPServer, BaseHTTPRequestHandler
    import pyautogui
    import subprocess
    from time import sleep
    import sys
    import tkinter
    from tkinter import *
    window = Tk()
    IPaddress = StringVar()
except Exception as eImport:
    print("Import Error")
    print(eImport)
    exit(1)

PageData = ""

class Handler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        global PageData
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        z=list()
        try:
            z = self.path.split("?")
        except Exception as eSplit:
            print(eSplit)
            
        if(len(z)>1):
            if(z[1]!="-1"):
                key= list()
                value = list()
                try:
                    datas = z[1].split("&")
                    for elements in datas:
                        try:
                            keyValue = elements.split("=")
                            key.append(keyValue[0])
                            value.append(keyValue[1])
                        except Exception:
                            print(Exception)                       
                except Exception:
                    try:
                        datas = z[1].split("=")
                        key.append(datas[0])
                        value.append(datas[1])
                    except Exception as eSplit:
                        print(Exception)
                
                if(len(key)>0):
                    print(key[0]," = ",value[0])
                    if(key[0]=='user' and value[0]=='admin'):
                        self.wfile.write(PageData.encode())
                        return
                    elif(key[0]=="signal1"):
                        self.wfile.write("".encode())
                        pyautogui.press('backspace')
                        return
                    elif(key[0]=="signal2"):
                        self.wfile.write("".encode())
                        pyautogui.press('up')
                        return
                    elif(key[0]=="signal3"):
                        self.wfile.write("".encode())
                        pyautogui.press('enter')
                        return
                    elif(key[0]=="signal4"):
                        self.wfile.write("".encode())
                        pyautogui.press('left')
                        return
                    elif(key[0]=="signal5"):
                        self.wfile.write("".encode())
                        pyautogui.press('down')
                        return
                    elif(key[0]=="signal6"):
                        self.wfile.write("".encode())
                        pyautogui.press('right')
                        return
                    elif(key[0]=="signal7"):
                        self.wfile.write("".encode())
                        pyautogui.press('ctrl')
                        #print("Terminating Server ")
                        pyautogui.press('ctrl')
                        #sleep(2)
                        server.socket.close()
                    elif(key[0]=="signal8"):
                        self.wfile.write("".encode())
                        pyautogui.press('f5')
                        return
                    elif(key[0]=="signal9"):
                        self.wfile.write("".encode())
                        pyautogui.keyDown('alt')
                        pyautogui.press('tab')
                        pyautogui.keyUp('alt')
                        return
                    elif(key[0]=="signal10"):
                        self.wfile.write("".encode())
                        pyautogui.keyDown('alt')
                        pyautogui.press('f4')
                        pyautogui.keyUp('alt')
                        return
                    else:
                        self.wfile.write("testing".encode())
                        return
                else:
                    self.wfile.write("Some Error Occurred".encode())
            else:
                self.wfile.write("<html><head><title>Unauthorized</title></head><body><center> <h1>You are Not authorized </h1></center></body></html>".encode())
        else:
            self.wfile.write("<html><head><title>Unauthorized</title></head><body><center> <h1>You are not authorized </h1></center></body></html>".encode())

if __name__=='__main__':

    try:
        print("Here")
        handle = subprocess.Popen(['hostname','-I'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        host,err = handle.communicate()
        host = host.decode().split(' ')
        host = str(host[0])
        window.title("Host Ip address?")
        label = Label(window,text = " Enter host IP address ")
        label.grid(row = 0,column = 0)

        ErrLabel = Label(window,text = "")
        ErrLabel.grid(row=1,column = 0)

        userEntry = Entry(window,width = 15, textvariable = IPaddress)
        userEntry.grid(row=0,column = 1)

        def action():
            global IPaddress,window
            hostIP = IPaddress.get()
            try:
                hostIP = hostIP.split(".")
                triger = False
                for elements in hostIP:
                    if((int(elements)<=0 and int(elements)>=255)):
                        triger=True
                if (triger or len(hostIP)!=4):
                    raise Exception
                else:
                    window.destroy()
            except Exception as eSplit:
                print("Invalid IP address")
                ErrLabel.configure(text = IPaddress.get()+" is Invalid IP address\n Pleace Enter Valid IP address")

        btn = Button(window,text = "Submit", command = action)
        btn.grid(row=0,column=2)
        window.mainloop()
        host = IPaddress.get()
        port = 8080
        PageData = "<html>"
        PageData += "<head> <title> Remote </title></head>"
        PageData += "<body> <h1><center> "
        PageData += "<form method=\"get\" target=\"goddalika\" action=\"http://"+host+":"+str(port)+"/\">"
        PageData += "<input style=\"height: 35%;width: 33%;background: red;\" type=\"submit\" name=\"signal1\" value=\"BackSpace\">"
        PageData += "<input style=\"height: 35%;width: 33%;background: yellow;\" type=\"submit\" name=\"signal2\" value=\"Up\">"
        PageData += "<input style=\"height: 35%;width: 33%;background: green;\" type=\"submit\" name=\"signal3\" value=\"Enter |_|\"> <br>"
        #PageData += "</form><br>"
        #PageData += "<form method=\"get\" action=\"http://"+host+":"+str(port)+"/\">"
        PageData += "<input style=\"height: 35%;width: 33%;background: lightgreen;\" type=\"submit\" name=\"signal4\" value=\"Left\">"
        PageData += "<input style=\"height: 35%;width: 33%;background: blue;\" type=\"submit\" name=\"signal5\" value=\"Down\">"
        PageData += "<input style=\"height: 35%;width: 33%;background: red;\" type=\"submit\" name=\"signal6\" value=\"Right\"> <br>"
        #PageData += "</form><br>"
        #PageData += "<form method=\"get\" action=\"http://"+host+":"+str(port)+"/\">" 
        PageData += "<input style=\"height: 30%;width: 25%;background: pink;\" type=\"submit\" name=\"signal7\" value=\"Terminate Remote\">"
        PageData += "<input style=\"height: 30%;width: 25%;background: blue;\" type=\"submit\" name=\"signal8\" value=\"F5\">"
        PageData += "<input style=\"height: 30%;width: 25%;background: lightgreen;\" type=\"submit\" name=\"signal9\" value=\"Alt_Tab\">"
        PageData += "<input style=\"height: 30%;width: 24%;background: red;\" type=\"submit\" name=\"signal10\" value=\"Alt_F4\"> <br>"
        PageData += "</form><iframe width=\"0px\" height=\"0px\" name=\"goddalika\"></iframe><br>"
        PageData += "</center></h1>"
        PageData += "</body>"
        PageData += "</html>"
        print("Starting Server at "+"http://"+host+":"+str(port)+"/")
        server = HTTPServer((host,port),Handler)
        server.serve_forever()
    except Exception:
        print(" Termination Signal")
    finally :
        print("Terminating Server ")
        pyautogui.press('ctrl')
        sleep(2)
        server.socket.close()
