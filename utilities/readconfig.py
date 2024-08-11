import configparser

config = configparser.RawConfigParser()
config.read("configuration/config.ini")


class Read_config_class:

    @staticmethod
    def getUsername():
        Username = config.get('Login Details', 'Username')
        return Username
    @staticmethod
    def getPassword():
        Password=config.get('Login Details','Password')
        return Password




