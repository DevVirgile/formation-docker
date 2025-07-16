import configparser

config = configparser.ConfigParser()
config.read('config.ini')

port = int(config['app']['port'])
db_url = config['database']['url']