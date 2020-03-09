import json

def create_ip_json():
    ips = []
    for i in range(1, 254):
        ip = {
            "model": "inventory.ipaddress",
            "pk": i, "fields":
            {
                "ip_address": "10.10.10." + str(i)
            }
        }
        ips.append(ip)

        with open("ips.json", "w") as outfile:
            json.dump(ips, outfile)

create_ip_json()
