from typing import List

from dongfeng_base.serializers import BaseSerializer
from dongfeng_base.serializers.host import UpHostsSerializer


class SubDomainSerializer(BaseSerializer):
    def __init__(self, subdomain: str, ip: list):
        self.subdomain = subdomain
        self.__resolve_ip = UpHostsSerializer(up_hosts=ip)

    @property
    def ip(self):
        return self.__resolve_ip.up_hosts


class EnumSubDomainSerializer(BaseSerializer):
    def __init__(self, domain: str, subdomain_list: List[SubDomainSerializer] = None):
        self.domain = domain
        self.subdomain_list = subdomain_list if subdomain_list else None


class SubDomainTitleSerializer(BaseSerializer):
    def __init__(self, subdomain: str, status_code: int, title: str, content: str, is_match: bool = False):
        self.subdomain = subdomain
        self.status_code = int(status_code)
        self.title = title
        self.content = content
        self.is_match = is_match