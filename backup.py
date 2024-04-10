# Backup system

class BackupSystem:
    def __init__(self, backup_name):
        self.name = backup_name
        self.__source = None
        self.__destination = None

    def __str__(self):
        return self.name

    def set_source(self, source):
        if source is not None:
            if source is str:
                self.__source = source
            else:
                raise ValueError("Source must be a string")
        else:
            raise ValueError("Source cannot be None")

    def set_destination(self, destination):
        if destination is not None:
            if destination is str:
                self.__destination = destination
            else:
                raise ValueError("Destination must be a string")
        else:
            raise ValueError("Destination cannot be None")

    def get_source(self):
        return self.__source

    def get_destination(self):
        return self.__destination