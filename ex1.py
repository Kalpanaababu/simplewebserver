from http.server import HTTPServer, BaseHTTPRequestHandler

contents = '''
<html>
    <head>
        <title>
             
        </title>
    </head>
    <body>
        <font color="Red" face="Verdana">
        <h1 align="Center">List of Protocols in TCP/IP Protocol</h1>
        </font>
        <font color="Blue">
        <h2>
            Application Layer - HTTP,FTP,DNS,Telnet & SSH <br>
            Transport Layer - TCP & UDP  <br>
            Netwrok Layer - IPV4/IPV6 <br>
            Link Layer - Ethernet 



        </h2>
        
        </font>
        
       
        

    </body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(contents.encode())

print("This is my webserver") 
server_address =('',5000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()