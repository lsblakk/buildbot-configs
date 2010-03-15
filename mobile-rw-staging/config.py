from copy import deepcopy
from defaults import default_platform, default_n810, default_n900

def generate_build_dirs(branch):
    for platform in branch['platforms'].keys():
        if branch['nightly']:
            branch['platforms'][platform]['unit_build_dirs'].append(
                'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-%s/' % branch['ftp_string'])
            branch['platforms'][platform]['talos_build_dirs'].append(
                'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-%s/' % branch['ftp_string'])
        if branch['per_checkin']:
            branch['platforms'][platform]['unit_build_dirs'].append(
                'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/%s/' % branch['ftp_string'])
            branch['platforms'][platform]['talos_build_dirs'].append(
                'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/%s/' % branch['ftp_string'])

SLAVES = {
    'n900': ['n900-019'],
    'n900': ['n900-%03i' % x for x in range(1,21)],
    'n810': ['maemo-n810-%02i' % x for x in [1,3,4,5,6] + range(9,81)],
}

default_n900['slaves'] = SLAVES['n900']
default_n810['slaves'] = SLAVES['n810']

BRANCHES = {
    'mozilla-central': {
        'ftp_string': 'mobile-trunk',
        'talos_branch': 'mobile',
        'tinderbox_tree': 'MobileTest',
        'graph_server': 'graphs-stage.mozilla.org',
        'tree_stable_timer': 0,
        'nightly': True,
        'per_checkin': True,
        'platforms': {
            'n810': deepcopy(default_n810),
            'n900': deepcopy(default_n900),
            'n900-qt': deepcopy(default_n900),
        },
    },
    'mozilla-1.9.2': {
        'ftp_string': 'mobile-1.9.2',
        'talos_branch': 'mobile-1.9.2',
        'tinderbox_tree': 'MobileTest',
        'graph_server': 'graphs-stage.mozilla.org',
        'tree_stable_timer': 0,
        'nightly': True,
        'per_checkin': True,
        'platforms': {
            'n810': deepcopy(default_n810),
            'n900': deepcopy(default_n900),
            'n900-qt': deepcopy(default_n900),
        },
    },
    'tracemonkey'  : {
        'ftp_string': 'mobile-tracemonkey',
        'talos_branch': 'mobile-tracemonkey',
        'tinderbox_tree': 'MobileTest',
        'graph_server': 'graphs-stage.mozilla.org',
        'tree_stable_timer': 0,
        'nightly': True,
        'per_checkin': True,
        'platforms': {
            'n810': deepcopy(default_n810),
            'n900': deepcopy(default_n900),
            'n900-qt': deepcopy(default_n900),
        },
    },
    'electrolysis': {
        'ftp_string': 'mobile-electrolysis',
        'talos_branch': 'mobile-electrolysis',
        'tinderbox_tree': 'MobileTest',
        'graph_server': 'graphs-stage.mozilla.org',
        'tree_stable_timer': 0,
        'nightly': True,
        'per_checkin': True,
        'platforms': {
            'n810': deepcopy(default_n810),
            'n900': deepcopy(default_n900),
            'n900-qt': deepcopy(default_n900),
        },
    },
    'places': {
        'ftp_string': 'mobile-places',
        'talos_branch': 'mobile-places',
        'tinderbox_tree': 'MobileTest',
        'graph_server': 'graphs-stage.mozilla.org',
        'tree_stable_timer': 0,
        'nightly': True,
        'per_checkin': True,
        'platforms': {
            'n810': deepcopy(default_n810),
            'n900': deepcopy(default_n900),
            'n900-qt': deepcopy(default_n900),
        },
    },
    'try': {
        'ftp_string': 'mobile-try',
        'talos_branch': 'mobile-try',
        'tinderbox_tree': 'MobileTest',
        'graph_server': 'graphs-stage.mozilla.org',
        'tree_stable_timer': 0,
        'nightly': True,
        'per_checkin': True,
        'platforms': {
            'n810': deepcopy(default_n810),
            'n900': deepcopy(default_n900),
            'n900-qt': deepcopy(default_n900),
        },
    },
}




###
### NOTE THAT THE AUTOMATIC BRANCH POLL LOCATIONS CONFIG GENERATION HAPPENS HERE
###
for branch in BRANCHES:
    generate_build_dirs(BRANCHES[branch])


#
# MANUAL OVERRIDES BELOW
#

#Example Override
# BRANCHES['mozilla-central']['platforms']['n900-qt']['talos_suites']['tp4']['timeout']=10

#As work on making unit tests progresses, it is likely that we are going to have
#to manually override fail counts in this section