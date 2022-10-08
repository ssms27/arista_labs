import yaml
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

ENV = Environment(loader=FileSystemLoader('.'))
t = ENV.get_template("test.j2")

location = ['DR', 'PROD']


def get_ntp_config() -> object:
    global location
    global t
    r = yaml.safe_load(Path("test.yml").read_text())

    for i in location:
        print(t.render(name='name', ntp=r['Juniper'][i]['ntp']))


get_ntp_config()
