import ConfigParser
import os

def getConfig(config_path_name,section, key):
    """
    @param config_path_name:
    @param section:
    @type section:
    @param key:
    @type key:
    @return:
    @rtype:
    """
    config = ConfigParser.ConfigParser()
    path = os.path.split(os.path.realpath(__file__))[0] + "/../../config/" + config_path_name
    config.read(path)
    return config.get(section, key)

#?? os.path.split(os.path.realpath(__file__))[0] ?????????????
