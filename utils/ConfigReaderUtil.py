from configparser import ConfigParser
import os

class ConfigReaderUtil:
    '''
    Returns the value for key present in configuration.ini file
    '''
    @staticmethod
    def get_env_value(key_name):
        configur = ConfigParser()
        file_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.dirname(file_directory) + "\\resources\\configuration.ini"
        configur.read(parent_directory)
        try :
            value = configur.get('env',key_name)
            return value
        except KeyError:
            print("Key is not present in configuration file")
        except AttributeError:
            print("Config parser is not set")
        except Exception as ex:
            print(ex)
