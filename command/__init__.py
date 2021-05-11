from os import listdir
from os.path import isdir, join
from importlib import import_module
import yaml


CONFIG_PATH = "./config.yml"
with open(CONFIG_PATH) as f:
    config_yml = yaml.safe_load(f)

path = config_yml['path']['command']
dir_list = list(filter(lambda x: isdir(join(path, x)), listdir(path)))


def is_include(command):
    return command in dir_list

def read_manual(command):
    with open(path + '/' + command + '/manual.yml') as f:
        manual_yml = yaml.safe_load(f)
    return manual_yml

def run(command, props):
    return modules[command].run(props)

def get_cmd_mannual(props=None):
    if props is None:
        s = "使い方: /echi <command>\n\n"

        s += "<command>\n"
        for command in manuals:
            print(command)
            s += "  {:<15}: {}".format(manuals[command]['val'], manuals[command]['desc'])
        return  s + "\n"


modules = {command: import_module('command.'+command) for command in dir_list if command != '__pycache__'}
manuals = {command: read_manual(command) for command in dir_list if command != '__pycache__'}