from jadi import component
import aj
from aj.api.http import url, HttpPlugin
from aj.api.endpoint import endpoint, EndpointError, EndpointReturn
import json
from socket import AF_INET
from pyroute2 import IPRoute
from pyroute2 import IPDB

@component(HttpPlugin)
class Handler(HttpPlugin):
	def __init__(self, context):
		self.context = context

	@url(r'/api/coach/fabric/get/links')
	@endpoint(api=True)
	def handle_api_fabric_get_links(self, http_context):
		results = []
		ip = IPRoute()
		links = ip.get_links()
		for link in links:
			result = {}
			result['name'] = link.get_attr('IFLA_IFNAME')
			result['state'] = link.get_attr('IFLA_OPERSTATE')
			result['mac'] = link.get_attr('IFLA_ADDRESS')
			result['ipv4'] = []
			result['ipv6'] = []
			with IPDB() as ipdb:
				for ipv4 in ipdb.interfaces[link.get_attr('IFLA_IFNAME')].ipaddr.ipv4:
					result['ipv4'].append(ipv4)
				for ipv6 in ipdb.interfaces[link.get_attr('IFLA_IFNAME')].ipaddr.ipv6:
					result['ipv6'].append(ipv6)
			
			results.append(result)
		return results