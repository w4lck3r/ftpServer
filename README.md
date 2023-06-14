# RAPPORT : Badr-Eddine SALMI


# FTP Server

This program sets up an FTP server using the `pyftpdlib` library in Python. It allows clients to connect to the server, authenticate with a username and password, and perform various file transfer operations.

## Features

- User authentication: The server supports user authentication using a username and password. The default username is "epsi", and the default password is "client22". You can modify these credentials in the code.

- Passive mode: The server operates in passive mode, which means the server opens a port and listens for incoming data connections from the client. The range of passive ports is set to 60000-65535, but you can adjust it if needed.

## Requirements

- Python 3.x
- `pyftpdlib` library

## Installation

1. Install the `pyftpdlib` library by running the following command:
   ```shell
    pip install pyftpdlib
   ```

2. Download or clone the code from the repository.

## Usage

1. Open the code in an IDE or text editor, such as Visual Studio Code.

2. Customize the username and password as desired:

```python
user = "epsi"
password = "client22"
```

3. Run the code in your preferred Python environment.

The server will start running on 127.0.0.1 (localhost) and port 21, the default FTP port.

Connect to the server using an FTP client, such as FileZilla or the command-line ftp utility, with the following credentials:

    Host: 127.0.0.1
    Port: 21
    Username: epsi
    Password: client22

4. Perform file transfer operations, such as uploading, downloading, listing directories, etc.

5. To change the password for the "epsi" user, modify the code as follows:
```
authorizer = server.handler.authorizer
authorizer.update_user("epsi", "new_password", ".")
```
Replace "new_password" with the desired new password.( for me i used : bqdr)

6. Stop the server by terminating the program.
