import paramiko

# Generate an RSA key
key = paramiko.RSAKey.generate(2048)

# Save the key to a file
key.write_private_key_file('test_rsa.key')

print("RSA key generated and saved as 'test_rsa.key'")
