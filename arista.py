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
    print(t.render(hostname=r['arista']['tor']['hostname'],
                   vlan=r['arista']['tor']['vlan'],
                   vni=r['arista']['tor']['vni'],
                   vteps=r['arista']['tor']['vteps'],
                   asn=r['arista']['tor']['bgp']['asn'],
                   router_id=r['arista']['tor']['bgp']['router_id'],
                   neighbor=r['arista']['tor']['bgp']['neighbor'],
                   remote_as=r['arista']['tor']['bgp']['remote_as'],
                   networks=r['arista']['tor']['bgp']['networks']))


# get_ntp_config()
get_arista_config()
