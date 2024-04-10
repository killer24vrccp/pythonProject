# Backup system
import os.path
import shutil


class BackupSystem:
    """
****************
Backup system

You must setup first 'set_name'
You must setup second 'set_source'
You must setup third 'set_destination'

Possible to backup folder or file

    """

    def __init__(self):
        self.__name = None
        self.__source = None
        self.__destination = None

    def __str__(self):
        if self.__name is not None:
            return self.__name
        else:
            return f"Not set yet \n{self.__doc__}"

    def set_name(self, backup_name):
        if backup_name is not None:
            b = "%s backup-system" % backup_name
            self.__name = b
        else:
            raise ValueError("Backup Name is required")

    def set_source(self, source):
        if source is not None:
            if isinstance(source, str):
                self.__source = source
            else:
                raise ValueError("Source must be a string")
        else:
            raise ValueError("Source cannot be None")

    def set_destination(self, destination):
        if destination is not None:
            if isinstance(destination, str):
                self.__destination = destination
            else:
                raise ValueError("Destination must be a string")
        else:
            raise ValueError("Destination cannot be None")

    def get_source(self):
        return "source: %s" % self.__source

    def get_destination(self):
        return "destination: %s" % self.__destination

    # Execute copy source to destination
    def copy_exec(self):
        if self.__source is not None:
            if self.__destination is not None:
                if os.path.abspath(self.__source) != os.path.abspath(self.__destination):
                    try:
                        source_path = os.path.join(self.__destination, os.path.basename(self.__source))
                        if os.path.exists(source_path):
                            user_input = input(
                                "Destination already exists. Do you want to overwrite it? (yes/no): ").lower()
                            if user_input == 'yes':
                                shutil.copy2(self.__source, self.__destination)
                                return "Backup copied to '%s' finished with success" % self.__destination
                            else:
                                return "Backup not copied. Destination not overwritten."
                        else:
                            shutil.copy2(self.__source, self.__destination)
                            return "Backup copied to '%s' finished with success" % self.__destination
                    except shutil.Error as e:
                        print('Error: {}'.format(e))
                else:
                    raise ValueError("Source and destination are the same.")
            else:
                raise ValueError("Destination is not set. Please set destination")
        else:
            raise ValueError("Source is not set. Please set source")


    # Execute move source to destination
    def move_exec(self):
        if self.__source is not None:
            if self.__destination is not None:
                if os.path.abspath(self.__source) != os.path.abspath(self.__destination):
                    try:
                        source_path = os.path.join(self.__destination, os.path.basename(self.__source))
                        if os.path.exists(source_path):
                            user_input = input(
                                "Destination already exists. Do you want to overwrite it? (yes/no): ").lower()
                            if user_input == 'yes':
                                shutil.move(self.__source, self.__destination)
                                return "Backup move to '%s' finished with success" % self.__destination
                            else:
                                return "Backup not copied. Destination not overwritten."
                        else:
                            shutil.move(self.__source, self.__destination)
                            return "Backup move to '%s' finished with success" % self.__destination
                    except shutil.Error as e:
                        print('Error: {}'.format(e))
                else:
                    raise ValueError("Source and destination are the same.")
            else:
                raise ValueError("Destination is not set. Please set destination")
        else:
            raise ValueError("Source is not set. Please set source")

