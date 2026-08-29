# my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# my_dict["occupation"] = "Engineer"

# for k, v in my_dict.items():
#     print(k)

server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

# Find Server Status
from OpenSSL.rand import status

server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

# Find server status
# def get_server_status(server_name):
#     if server_name in server_config:
#         return server_config[server_name]['status']
#     else:
#         return "server not found"
#
# server_name = "server1"
# print(get_server_status(server_name))

def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', "server not found")

server_name = "server1"
status = get_server_status(server_name)
print(status)


