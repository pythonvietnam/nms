from .models import IP


class UtilsIP(object):
    def get_list_ip(self, vhost):
        obj_vhost = {}
        obj_vhost['default'] = []

        if not vhost:
            list_ip = IP.objects.values_list('vhost', 'address').distinct()
            for ip in list_ip:
                key = ip[0]
                if key:
                    if not key in obj_vhost:
                        obj_vhost[key] = []

                    if ip[1] not in obj_vhost[key]:
                        obj_vhost[key].append(ip[1])
                else:
                    obj_vhost['default'].append(ip[1])
            return obj_vhost
        else:
            return IP.objects.values_list('address', 'vhost').distinct()


