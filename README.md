# Pax-ssh_honeypot_with_keylogger
_______________________

# Combined Honeypot and Keylogger Tool

## Project Overview

This project combines a honeypot and a keylogger into a single tool to capture login attempts and keystrokes, providing a comprehensive view of potential threats. The honeypot simulates an SSH server to capture login attempts, while the keylogger captures keystrokes on the target system. All interactions are logged for analysis.

## Key Components

1. **SSH Honeypot**: Simulates an SSH server to capture login attempts.
2. **Keylogger**: Captures keystrokes on the target system.
3. **Logging**: Logs all interactions with the honeypot and keylogger.
4. **Data Analysis**: Analyzes the captured data to understand attacker behavior.

## Tools and Technologies

- **Programming Language**: Python
- **Libraries**:
  - `paramiko`: For SSH server simulation.
  - `pynput`: For keylogging.
  - `logging`: For logging interactions.

## Setup Instructions

### Prerequisites

- Python 3.x
- `paramiko` library
- `pynput` library

### Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/luckysitara/Pax-ssh_honeypot_with_keylogger.git
   cd Pax-ssh_honeypot_with_keylogger
   ```

2. **Install Dependencies**:
   ```sh
   pip install paramiko pynput
   ```

3. **Generate RSA Key**:
   ```sh
   python generate_rsa_key.py
   ```

   This script generates an RSA key for the SSH server and saves it as `test_rsa.key`.

### Running the Tool

1. **Start the Combined Tool**:
   ```sh
   python combined_tool.py
   ```

   This script starts the SSH honeypot server and the keylogger. The honeypot listens on port 2222 for incoming SSH connections, while the keylogger captures keystrokes.

### Connecting a Client

#### Using the Command Line SSH Client

Open a terminal and run the following command:
```sh
ssh username@localhost -p 2222
```
Replace `username` with any username you want to test. The honeypot will log the connection attempt and any commands you enter.

#### Using a Python Script to Automate the Connection

You can also write a Python script to automate the SSH connection to the honeypot. Save the following script to a file, for example, `ssh_client.py`, and run it:

```python
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
```

Run the script:
```sh
python ssh_client.py
```

### Monitoring and Analyzing the Logs

The combined tool logs all SSH connection attempts, commands received, and keystrokes to `combined_tool.log`. Review the log file to understand the behavior of attackers trying to access the honeypot and the keystrokes captured.

### Ethical and Legal Considerations

- **Consent**: Ensure you have explicit consent from all parties involved, especially if deploying the tool in a shared environment.
- **Legal Compliance**: Make sure you are complying with all relevant laws and regulations.
- **Privacy**: Respect the privacy of individuals and use the data responsibly.

### Enhancements

1. **Advanced Logging**: Implement more detailed logging to capture additional information about the attacker.
2. **Data Analysis**: Use tools like the ELK Stack (Elasticsearch, Logstash, Kibana) to analyze the captured data.
3. **Security Measures**: Ensure the tool is isolated from critical systems to prevent real attacks.
4. **Additional Services**: Simulate other services (e.g., FTP, HTTP) to capture a wider range of attacker behavior.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions, improvements, or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or support, please contact [your-email@example.com](mailto:your-email@example.com).

---

This `README.md` file provides a comprehensive overview of the combined honeypot and keylogger project, including setup instructions, usage guidelines, and important ethical and legal considerations. Always prioritize ethical considerations and legal compliance when working on such projects.
```

bye
