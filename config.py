# - *- coding: utf- 8 - *-
import configparser

config = configparser.ConfigParser()
config.read("html_blanc.ini", encoding='UTF-8')
html_file_path = config["info"]["html_file_path"]