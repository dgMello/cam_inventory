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

    with open("../ips.json", "w") as outfile:
        json.dump(ips, outfile)


def create_patch_panels_json():
    ips = []
    for i in range(1, 10):
        ip = {
            "model": "inventory.patchpanel",
            "pk": i, "fields":
                {
                    "patch_panel": "PP" + str(i)
                }
        }
        ips.append(ip)

    with open("patch_panels.json", "w") as outfile:
        json.dump(ips, outfile)


def create_patch_connections_json():
    ips = []
    x = 1
    for i in range(1, 10):
        for j in range(1, 25):
            ip = {
                "model": "inventory.patchpanelconnection",
                "pk": x, "fields":
                    {
                        "connection": str(j),
                        "patch_panel": "PP" + str(i)
                    }
            }
            ips.append(ip)
            x += 1

    with open("patch_panels_conn.json", "w") as outfile:
        json.dump(ips, outfile)


create_patch_connections_json()
