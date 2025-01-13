import paramiko
import time

# Honeypot server configuration
hostname = 'localhost'
port = 2222
username = 'testuser'
password = 'testpass'

# Create an SSH client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connect to the honeypot
    client.connect(hostname, port=port, username=username, password=password)
    print("Connected to the honeypot")

    # Open a shell session
    channel = client.invoke_shell()

    # Send commands to the honeypot
    commands = [
        'ls',
        'whoami',
        'uname -a',
        'exit'
    ]

    for command in commands:
        channel.send(command + '\n')
        time.sleep(1)  # Wait for the command to be processed
        output = channel.recv(4096).decode()
        print(output)

    # Close the channel
    channel.close()

except paramiko.SSHException as e:
    print(f"SSHException: {e}")

finally:
    # Close the client connection
    client.close()
