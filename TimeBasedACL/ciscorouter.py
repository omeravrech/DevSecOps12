from paramiko import SSHClient, AutoAddPolicy
from interfaces import IRouter
from enums import UserMode
from time import sleep
import re


class CiscoRouter(IRouter):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__connection = None
        self.__shell = None

    def connect(self) -> None:
        # Verify first if connection isn't open already
        # If so, pass this function
        if self.is_connected():
            return

        # Preparing connection variables
        self.__connection = SSHClient()
        self.__connection.set_missing_host_key_policy(AutoAddPolicy())
        address = getattr(self, "_address", None)
        port = getattr(self, "_port", 22)
        user = getattr(self, "_username", "cisco")
        passwd = getattr(self, "_password", "cisco")

        # Connection open attempt
        try:
            self.__connection.connect(address, port=port, username=user, password=passwd, allow_agent=False,
                                      look_for_keys=False)
            self._connected = True
        except Exception as e:
            print("Connection aborted due to error.", e)
            self._connected = False

    def check_user_mode(self) -> UserMode:
        if not self.is_connected():
            raise ConnectionError()
        output = self.execute("")
        if re.search(r"\(\w+(-)?\w+\)#", output, re.MULTILINE):
            return UserMode.config
        elif re.search(r"#", output, re.MULTILINE):
            return UserMode.admin
        elif re.search(r">", output, re.MULTILINE):
            return UserMode.user
        else:
            return UserMode.unclear

    def execute(self, commands) -> str:
        # Connection must be open before execute commands
        if not self.is_connected():
            raise ConnectionError()

        # Verify commands is a list of strings
        if isinstance(commands, str):
            commands = [commands]
        elif not isinstance(commands, list):
            raise TypeError("Commands must be one string or array of strings")

        # Initiate returned data
        stdout = ""

        try:
            # Execute commands one by one
            if self.__shell is None:
                self.__shell = self.__connection.invoke_shell()
            self.__shell.recv(-1)  # clear buffer

            for command in commands:
                if isinstance(command, str):
                    self.__shell.send(f"{command}\n")

            # read all data from router
            while True:
                sleep(2)  # is there is delay in traffic
                data_from_router = self.__shell.recv(-1).decode("utf-8")
                if data_from_router == '':  # No data received anymore
                    break
                stdout += data_from_router

        except Exception as e:
            print("Connection aborted due to error.", e)
            self._connected = False  # If there is any type of issue it mean the connection is close

        return stdout

    def close(self) -> None:
        #  If connection is open, then try to close it
        if self.is_connected():
            try:
                self.__connection.close()
            except:
                pass
