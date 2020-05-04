import socket
import json
from custom_exceptions import BadCommand

MAX_PACKET_SIZE = 2 ** 16

def api_search(path):
    
    target_path = "/api/" + "/".join(path)
    target_host = "www.dnd5eapi.co"
    request = f"GET {target_path} HTTP/1.0\r\nHost: {target_host}\r\n\r\n"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host, 80))
    client.send(request.encode())

    data = []
    while True:
        
        # Processing multiple packets if necessary
        response = client.recv(MAX_PACKET_SIZE)
        if not response:
            break
        http_response = repr(response)
        data.append(http_response)
    client.close()

    # Processing packets into a string
    packet = "".join(data)
    split_packet = packet.split("\\r\\n\\r\\n")
    header, body = split_packet[0], split_packet[1]

    sanitized_body = body[:-1].replace('\\', '')
    payload = json.loads(sanitized_body)

    return payload


def backend_search(path, header=None):
    queried_obj = api_search(path)

    def dump_obj(json_obj):
        for key in json_obj:
            print("\n" + key)
            print(json_obj[key])
    
    if header:
        for head in header:
            if head == "all":
                dump_obj(queried_obj)
            else:
                print(queried_obj[header])
    
    else:
        print(f"Found: {queried_obj['name']}")
        user_input = ""
        while user_input != "back":
            for key in queried_obj:
                print(key)
            user_input = input("Input one of the above or 'back' to return: ")
            
            try:
                print(queried_obj[user_input])
            except KeyError:
                continue


def search(word_list):
    default_msg = "Search syntax is 'search [category] [subcategory]: [header(s)]"
    executed_properly = False
    path = []
    header = None

    if len(word_list) >= 2:
        path = word_list[:2]
        if len(word_list) >= 3:
            header = word_list[2:]
        
        backend_search(path, header)
        executed_properly = True
    
    if not executed_properly:
        print(default_msg)
