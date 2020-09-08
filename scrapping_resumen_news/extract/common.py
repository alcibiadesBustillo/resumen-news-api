import yaml

__config = None

def config():
    """Configuration file with the url of the sites 
       and css classes

    Returns:
        file: return yaml file with the configuration
    """
    global __config
    if not __config:
        with open('config.yaml', mode='r') as f:
            config = yaml.safe_load(f)
    return config