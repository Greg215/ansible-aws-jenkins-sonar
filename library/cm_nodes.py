from ansible.module_utils.basic import *
from collections import Counter, defaultdict

if __name__ == '__main__':
    global module
    module = AnsibleModule(
        argument_spec={
            'machines': {'required': True, 'type': 'list'}
        },
        supports_check_mode=False
    )

    machines = module.params.get('machines')
    
    roles_counter = Counter([machine['tags']['Name'] for machine in machines])
    roles_count = defaultdict(int)
    nodes = []
    for machine in machines:
      assert isinstance(machine, dict)
      role = machine['tags']['Name']
      if roles_counter[role] > 1:
         roles_count[role] += 1
         node_name = "{}-{}".format(role, roles_count[role])
      else:
         node_name = "{}".format(role)
      nodes.append({
                     'name': node_name, 
                     'private_ip': machine['private_ip_address'], 
                     'public_ip': machine['public_ip_address'],
                   })

    module.exit_json(changed=False, nodes=nodes)
