import yaml
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

ENV = Environment(loader=FileSystemLoader('.'))
t = ENV.get_template("arista.j2")


def get_ntp_config() -> object:
    global location
    global t
    r = yaml.safe_load(Path("arista.yml").read_text())

    for i in location:
        print(t.render(name='name', ntp=r['Juniper'][i]['ntp']))


def get_arista_config() -> object:
    global t
    r = yaml.safe_load(Path("arista.yaml").read_text())
    for i in r['arista']:
        print(t.render(hostname=i['tor']['hostname'],
                   vlan=i['tor']['vlan'],
                   vteps=i['tor']['vteps'],
                   vni=i['tor']['vni'],
                   asn=i['tor']['bgp']['asn'],
                   router_id=i['tor']['bgp']['router_id'],
                   neighbor=i['tor']['bgp']['neighbor'],
                   remote_as=i['tor']['bgp']['remote_as'],
                   networks=i['tor']['bgp']['networks']))

# get_ntp_config()
get_arista_config()
