class FilterModule(object):

    def filters(self):
        return {
            'match_config': self.match_config,
        }

    def match_config(self, machines, conf):
        return [dict(machine=host, config=cf)  for host in machines 
                for cf in conf if cf['tags'] == host['tags']]
