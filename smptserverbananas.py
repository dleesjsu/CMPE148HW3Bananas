# Bananas 10/5/2025

from socket import *
msg = "\r\nFrom: banana@banana.banana\r\nTo: notbanana@mee.sjsu\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver

# the link you gave us for the free smtp server did not work so I just hosted a local one
#mailserver = "smtp.freesmtpservers.com"
#port = 25

mailserver = "localhost"
port = 2525

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))
#Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
mfcmd = 'MAIL FROM: <banana@banana.banana>\r\n'
clientSocket.send(mfcmd.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

if recv2[:3] != '250':
    print('250 reply not received from server.')
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
rcptcmd = "RCPT TO: notbanana@mee.sjsu\r\n"
clientSocket.send(rcptcmd.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
# Fill in end

# Send DATA command and print server response.
# Fill in start
datacmd = "DATA\r\n"
clientSocket.send(datacmd.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
# Fill in end

# Send message data.
# Fill in start
clientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitcmd = "QUIT\r\n"
clientSocket.send(quitcmd.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
# Fill in end