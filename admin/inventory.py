#!/usr/bin/env python

import sys
import os
import os.path
import json

filter_yaml = lambda s: not s.startswith('.') and s.endswith('.yaml') or s.endswith('.yml')
map_appname = lambda s: s.rsplit('.', 1)[0]

playbook_dir = os.path.dirname(os.path.abspath(__file__))
platform_dir = os.path.abspath('{}/../platform'.format(playbook_dir))
projects_dir = os.path.abspath('{}/../projects'.format(playbook_dir))

platform_files = os.listdir(platform_dir)
platform_yamls = filter(filter_yaml, platform_files)
platform_apps = map(map_appname, platform_yamls)

projects_files = os.listdir(projects_dir)
projects_yamls = filter(filter_yaml, projects_files)
projects_apps = map(map_appname, projects_yamls)

hosts_list = {
    'platform': {
        'hosts': list(platform_apps)
    },
    'projects': {
        'hosts': list(projects_apps)
    }
}

script_action = sys.argv[1]

if script_action == '--list':
    print(json.dumps(hosts_list))

elif script_action == '--host':
    print('{}')

else:
    print('Usage: {} [--list|--host <hostname>]'.format(__file__))
    sys.exit(1)
