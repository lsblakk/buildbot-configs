from copy import deepcopy

from buildbot.steps.shell import WithProperties

import project_branches
reload(project_branches)
from project_branches import PROJECT_BRANCHES, ACTIVE_PROJECT_BRANCHES

import localconfig
reload(localconfig)
from localconfig import SLAVES, GLOBAL_VARS, GRAPH_CONFIG

REMOTE_PROCESS_NAMES = { 'default':         'org.mozilla.fennec',
                         'mozilla-beta':    'org.mozilla.firefox_beta',
                         'mozilla-aurora':  'org.mozilla.fennec_aurora',
                         'mozilla-release': 'org.mozilla.firefox',
                       }

TALOS_CMD = ['python', 'run_tests.py', '--noisy', WithProperties('%(configFile)s')]

TALOS_ADDON_CMD = ['python', 'run_tests.py', '--noisy', '--amo', WithProperties('%(configFile)s')]

TALOS_DIRTY_OPTS = {'talosAddOns': ['profiles/dirtyDBs.zip', 'profiles/dirtyMaxDBs.zip']}

TALOS_TP_OPTS = {'plugins': 'zips/plugins.zip', 'pagesets': ['zips/tp5.zip']}
TALOS_TP4_OPTS = {'plugins': 'zips/plugins.zip', 'pagesets': ['zips/tp4.zip',]}

TALOS_ADDON_OPTS = {'addonTester' : True, 'releaseTester' : True, 'plugins': 'zips/plugins.zip'}
TALOS_BASELINE_ADDON_OPTS = {'releaseTester' : True, 'plugins': 'zips/plugins.zip'}

TALOS_REMOTE_FENNEC_OPTS = { 'productName':  'fennec',
                             'remoteTests':  True,
                             'remoteExtras': { 'options': [ '--sampleConfig', 'remote.config',
                                                            '--output', 'local.yml',
                                                            '--webServer', 'bm-remote.build.mozilla.org',
                                                            '--browserWait', '60',
                                                          ],
                                               'processName': REMOTE_PROCESS_NAMES,
                                             },
                           }

UNITTEST_REMOTE_EXTRAS = { 'processName': REMOTE_PROCESS_NAMES,
                         }

BRANCHES = {
    'mozilla-central':     { 'release_branch': True },
    'mozilla-release':     { 'release_branch': True },
    'mozilla-beta':        { 'release_branch': True },
    'mozilla-aurora':      { 'release_branch': True },
    'mozilla-1.9.2':       { 'release_branch': True },
    'shadow-central':      {},
    'try':                 {},
    'addontester':         {},
    'addonbaselinetester': {},
}

# Talos
PLATFORMS = {
    'macosx': {},
    'macosx64': {},
    'win32': {},
    'win64': {},
    'linux': {},
    'linux64' : {},
    'linux-android': {},
}

# work around path length problem bug 599795
# leopard-o == leopard-old
PLATFORMS['macosx']['slave_platforms'] = ['leopard-o']
PLATFORMS['macosx']['env_name'] = 'mac-perf'
PLATFORMS['macosx']['leopard-o'] = {'name': "Rev3 MacOSX Leopard 10.5.8"}
PLATFORMS['macosx']['stage_product'] = 'firefox'

PLATFORMS['macosx64']['slave_platforms'] = ['leopard', 'snowleopard']
PLATFORMS['macosx64']['env_name'] = 'mac-perf'
PLATFORMS['macosx64']['leopard'] = {'name': "Rev3 MacOSX Leopard 10.5.8"}
PLATFORMS['macosx64']['snowleopard'] = {'name': "Rev3 MacOSX Snow Leopard 10.6.2"}
PLATFORMS['macosx64']['stage_product'] = 'firefox'

PLATFORMS['win32']['slave_platforms'] = ['xp', 'win7']
PLATFORMS['win32']['env_name'] = 'win32-perf'
PLATFORMS['win32']['xp'] = {'name': "Rev3 WINNT 5.1"}
PLATFORMS['win32']['win7'] = {'name': "Rev3 WINNT 6.1"}
PLATFORMS['win32']['stage_product'] = 'firefox'

PLATFORMS['win64']['slave_platforms'] = ['w764']
PLATFORMS['win64']['env_name'] = 'win64-perf'
PLATFORMS['win64']['w764'] = {'name': "Rev3 WINNT 6.1 x64",
                              'download_symbols': False,
                             }
PLATFORMS['win64']['stage_product'] = 'firefox'

PLATFORMS['linux']['slave_platforms'] = ['fedora']
PLATFORMS['linux']['env_name'] = 'linux-perf'
PLATFORMS['linux']['fedora'] = {'name': "Rev3 Fedora 12"}
PLATFORMS['linux']['stage_product'] = 'firefox'

PLATFORMS['linux64']['slave_platforms'] = ['fedora64']
PLATFORMS['linux64']['env_name'] = 'linux-perf'
PLATFORMS['linux64']['fedora64'] = {'name': "Rev3 Fedora 12x64"}
PLATFORMS['linux64']['stage_product'] = 'firefox'

PLATFORMS['linux-android']['slave_platforms'] = ['tegra_android']
PLATFORMS['linux-android']['env_name'] = 'android-perf'
PLATFORMS['linux-android']['is_mobile'] = True
PLATFORMS['linux-android']['tegra_android'] = {'name': "Android Tegra 250",
                                         'download_symbols': False,
                                        }
PLATFORMS['linux-android']['stage_product'] = 'mobile'
PLATFORMS['linux-android']['stage_platform'] = 'android'


# Copy the slave names into PLATFORMS[platform][slave_platform], trimming off
# the -o suffix if necessary
for platform, platform_config in PLATFORMS.items():
    for slave_platform in platform_config['slave_platforms']:
        platform_config[slave_platform]['slaves'] = sorted(SLAVES[slave_platform.split('-')[0]])

MOBILE_PLATFORMS = PLATFORMS['linux-android']['slave_platforms']

ALL_PLATFORMS = PLATFORMS['linux']['slave_platforms'] + \
                PLATFORMS['linux64']['slave_platforms'] + \
                PLATFORMS['win32']['slave_platforms'] + \
                PLATFORMS['win64']['slave_platforms'] + \
                PLATFORMS['macosx64']['slave_platforms']

NO_WIN = PLATFORMS['macosx64']['slave_platforms'] + PLATFORMS['linux']['slave_platforms'] + PLATFORMS['linux64']['slave_platforms']

NO_MAC = PLATFORMS['linux']['slave_platforms'] + PLATFORMS['linux64']['slave_platforms'] + PLATFORMS['win32']['slave_platforms'] + PLATFORMS['win64']['slave_platforms']

ANDROID = PLATFORMS['linux-android']['slave_platforms']

ADDON_TESTER_PLATFORMS = ['win7', 'fedora', 'snowleopard']

SUITES = {
    'chrome': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'ts:tdhtml:twinopen:tsspider'],
        'options': (True, {}, ALL_PLATFORMS),
    },
    'nochrome': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tdhtml:tsspider', '--noChrome'],
        'options':  (True, {}, ALL_PLATFORMS),
    },
    'dirty': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'ts_places_generated_min:ts_places_generated_med:ts_places_generated_max'],
        'options':   (True, TALOS_DIRTY_OPTS, ALL_PLATFORMS),
    },
    'tp': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp5'],
        'options':    (True, TALOS_TP_OPTS, ALL_PLATFORMS),
    },
    'tp4': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp4'],
        'options': (True, TALOS_TP4_OPTS, ALL_PLATFORMS),
    },
    'cold': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'ts_cold:ts_cold_generated_min:ts_cold_generated_med:ts_cold_generated_max'],
        'options': (True, TALOS_DIRTY_OPTS, NO_WIN),
    },
    'v8': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'v8'],
        'options':  (True, {}, ALL_PLATFORMS),
    },
    'svg': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tsvg:tsvg_opacity'],
        'options': (True, {}, ALL_PLATFORMS),
    },
    'scroll': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tscroll'],
        'options': (True, {}, ALL_PLATFORMS),
    },
    'dromaeo': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'dromaeo_basics:dromaeo_v8:dromaeo_sunspider:dromaeo_jslib:dromaeo_css:dromaeo_dom'],
        'options': (True, {}, ALL_PLATFORMS),
    },
    'addon': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'ts', '--noShutdown', '--sampleConfig', 'addon.config'],
        'options': (False, TALOS_ADDON_OPTS, ALL_PLATFORMS),
    },
    'addon-baseline': {
        'enable_by_default': False,
        'suites': GRAPH_CONFIG + ['--activeTests', 'ts', '--noShutdown', '--sampleConfig', 'addon.config'],
        'options': (False, TALOS_BASELINE_ADDON_OPTS, ALL_PLATFORMS),
    },
    'a11y': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'a11y'],
        'options': (True, {}, NO_MAC),
    },
    'paint': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'ts_paint:tpaint', '--setPref', 'dom.send_after_paint_to_content=true'],
        'options': (True, {}, ALL_PLATFORMS),
    },
    'remote-ts': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'ts', '--noChrome'],
        'options': (True, TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-tdhtml': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tdhtml', '--noChrome'],
        'options': (True, TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-tsvg': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tsvg', '--noChrome'],
        'options': (True, TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-tsspider': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tsspider', '--noChrome'],
        'options': (True, TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-tpan': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tpan', '--noChrome'],
        'options': (True, TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-tp4m': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp4m'],
        'options': (True, TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-tp4m_nochrome': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tp4m', '--noChrome'],
        'options': (True, TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-twinopen': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'twinopen'],
        'options': (True, TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
    'remote-tzoom': {
        'enable_by_default': True,
        'suites': GRAPH_CONFIG + ['--activeTests', 'tzoom'],
        'options': (True, TALOS_REMOTE_FENNEC_OPTS, ANDROID),
    },
}

# these three are for mozilla-1.9.2
OLD_BRANCH_ALL_PLATFORMS = PLATFORMS['linux']['slave_platforms'] + \
                PLATFORMS['win32']['slave_platforms'] + \
                PLATFORMS['macosx']['slave_platforms']

OLD_BRANCH_NO_WIN = PLATFORMS['macosx']['slave_platforms'] + PLATFORMS['linux']['slave_platforms']

OLD_BRANCH_NO_MAC = PLATFORMS['linux']['slave_platforms'] + PLATFORMS['win32']['slave_platforms']

OLD_BRANCH_ADDON_TESTER_PLATFORMS = ['win7'] + ['fedora'] + ['snowleopard']

BRANCH_UNITTEST_VARS = {
    'hghost': 'hg.mozilla.org',
    # turn on platforms as we get them running
    'platforms': {
        'linux': {},
        'linux64': {},
        'macosx': {},
        'macosx64': {},
        'win32': {},
        'win64': {},
        'linux-android': {},
    },
}

# Default set of unit tests
UNITTEST_SUITES = {
    'opt_unittest_suites': [
        # Turn on chunks for mochitests
        ('mochitests', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
        ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
                             'mochitest-a11y', 'mochitest-ipcplugins']),
        ('reftest', ['reftest']),
        ('crashtest', ['crashtest']),
        ('xpcshell', ['xpcshell']),
        ('jsreftest', ['jsreftest']),
        # Disabled in bug 630551
        #('mozmill-all', ['mozmill']),
    ],
    'debug_unittest_suites': [
        # Turn on chunks for mochitests
        ('mochitests', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
        ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
                             'mochitest-a11y', 'mochitest-ipcplugins']),
        ('reftest', ['reftest']),
        ('crashtest', ['crashtest']),
        ('xpcshell', ['xpcshell']),
        ('jsreftest', ['jsreftest']),
        # Disabled in bug 630551
        #('mozmill-all', ['mozmill']),
    ],
    'mobile_unittest_suites': [
        # The disabled test suites are only disabled until we can get
        # to 100% green
        #('mochitests', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
        #('mochitest-other', ['mochitest-chrome', 'mochitest-a11y',
        #                     'mochitest-ipcplugins']),
        ('mobile-mochitest-browser-chrome', ['mobile-mochitest-browser-chrome']),
        #('reftest', ['reftest']),
        #('crashtest', ['crashtest']),
        #('xpcshell', ['xpcshell']),
        #('jsreftest', ['jsreftest']),
    ],

}

def removeSuite(suiteName, suiteList):
    '''It removes 'suite' from 'suiteList' and returns it.

    Keyword arguments:
    suiteName -- it is the name of the suite that we want to remove
    suiteList -- it is the list of suites from where we want to remove
                 suiteList is a list of tuples. The tuples is formed
                 of a string and a list of suites.
    '''
    # Let's iterate over each tuple
    for i, info in enumerate(suiteList):
        name, suites = info
        # Let's see if suiteName is on this list of suites
        if suiteName in suites:
            suites = suites[:]
            suites.remove(suiteName)
            suiteList[i] = (name, suites)
    return suiteList

def addSuite(suiteGroupName, newSuiteName, suiteList):
    # In UNITTEST_SUITES we have opt, debug and mobile unit tests keys.
    # Each one of these have a list of tuples of test suites.
    #     e.g. suiteGroup = ('reftest', ['reftest])
    newSuiteList = []
    added = False
    for tuple in suiteList:
        name, suites = tuple
        if suiteGroupName == name:
            suites.append(newSuiteName)
            added = True
        newSuiteList.append((name, suites))

    if not added:
        newSuiteList.append((name, suites))

    return newSuiteList

def loadDefaultValues(BRANCHES, branch, branchConfig):
    BRANCHES[branch]['repo_path'] = branchConfig.get('repo_path', 'projects/' + branch) 
    BRANCHES[branch]['branch_name'] = branchConfig.get('branch_name', branch.title())
    BRANCHES[branch]['mobile_branch_name'] = branchConfig.get('mobile_branch_name', branch.title())
    BRANCHES[branch]['build_branch'] = branchConfig.get('build_branch', branch.title())
    BRANCHES[branch]['talos_command'] = branchConfig.get('talos_cmd', TALOS_CMD)
    BRANCHES[branch]['fetch_symbols'] = branchConfig.get('fetch_symbols', True)
    BRANCHES[branch]['support_url_base'] = branchConfig.get('support_url_base', 'http://build.mozilla.org/talos')
    BRANCHES[branch]['enable_unittests'] = branchConfig.get('enable_unittests', True)

def loadCustomTalosSuites(BRANCHES, SUITES, branch, branchConfig):
    # Check if Talos is enabled, if False, set 0 runs for all suites
    if branchConfig.get('enable_talos') == False:
        branchConfig['talos_suites'] = {}
        for suite in SUITES.keys():
            branchConfig['talos_suites'][suite]  = 0

    # Want to turn on/off a talos suite? Set it in the PROJECT_BRANCHES[branch]['talos_suites'] otherwise, defaults below
    if branchConfig.get('talos_suites'):
        talosConfig = branchConfig['talos_suites']
    else:
        # This is the default and will make all talosConfig.get(key,0) calls
        # to default to 0 a.k.a. disabled suite
        talosConfig = {}

    for suite in SUITES.keys():
        if not SUITES[suite]['enable_by_default']:
            # Suites that are turned off by default
            BRANCHES[branch][suite + '_tests'] = (talosConfig.get(suite, 0), ) + SUITES[suite]['options']
        else:
            # Suites that are turned on by default
            BRANCHES[branch][suite + '_tests'] = (talosConfig.get(suite, 1), ) + SUITES[suite]['options']

def loadTalosSuites(BRANCHES, SUITES, branch):
    '''
    This is very similar to loadCustomTalosSuites and is to deal with branches that are not in project_branches.py
    but in config.py. Both functions could be unified later on when we do further refactoring.
    '''
    for suite in SUITES.keys():
        if not SUITES[suite]['enable_by_default']:
            # Suites that are turned off by default
            BRANCHES[branch][suite + '_tests'] = (0,) + SUITES[suite]['options']
        else:
            # Suites that are turned on by default
            BRANCHES[branch][suite + '_tests'] = (1,) + SUITES[suite]['options']

def loadCustomUnittestSuites(BRANCHES, branch, branchConfig):
    # If you want a project branch to have a different set of unit tests you can
    # do the following:
    #  - add a key called "add_test_suites"
    #  - add a tuple for each test suite with the following format:
    #      ('OS_nick', 'platform', 'opt|debug', 'new or existing group', 'suite name')
    #      e.g. ('macosx64', 'snowleopard', 'debug', 'mochitest-other', 'a11y')
    #
    # Old way of adding suites but still the same format
    #    BRANCHES['mozilla-central']['platforms']['win32']['win7']['debug_unittest_suites'] \
    #        += [('jetpack', ['jetpack'])]
    #
    for suiteToAdd in branchConfig.get('add_test_suites', []):
        type = 'opt_unittest_suites' if suiteToAdd[2] == 'opt' else 'debug_unittest_suites'
        # 'debug_unittest_suites' or 'opt_unittest_suites' is a list of tuple
        # addSuite() modifies that list and returns a new one with the added suite
        BRANCHES[branch]['platforms'][suiteToAdd[0]][suiteToAdd[1]][type] = \
            addSuite( suiteGroupName=suiteToAdd[3], newSuiteName=suiteToAdd[4],
                      suiteList=BRANCHES[branch]['platforms'][suiteToAdd[0]][suiteToAdd[1]][type])

# You must define opt_unittest_suites when enable_opt_unittests is True for a 
# platform. Likewise debug_unittest_suites for enable_debug_unittests
PLATFORM_UNITTEST_VARS = {
        'linux': {
            'builds_before_reboot': 1,
            'unittest-env' : {'DISPLAY': ':0'},
            'enable_opt_unittests': True,
            'enable_debug_unittests': True,
            'fedora': {
                'opt_unittest_suites' : \
                    UNITTEST_SUITES['opt_unittest_suites'][:] + \
                    [('reftest-ipc', ['reftest-ipc'])] + \
                    [('crashtest-ipc', ['crashtest-ipc'])],
                'debug_unittest_suites' : UNITTEST_SUITES['debug_unittest_suites'][:],
                'mobile_unittest_suites' : UNITTEST_SUITES['mobile_unittest_suites'][:],
            },
        },
        'linux64': {
            'builds_before_reboot': 1,
            'unittest-env' : {'DISPLAY': ':0'},
            'enable_opt_unittests': True,
            'enable_debug_unittests': True,
            'fedora64': {
                'opt_unittest_suites' : UNITTEST_SUITES['opt_unittest_suites'][:],
                'debug_unittest_suites' : UNITTEST_SUITES['debug_unittest_suites'][:],
            },
        },
        'win32': {
            'builds_before_reboot': 1,
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'env_name' : 'win32-perf-unittest',
            'enable_opt_unittests': True,
            'enable_debug_unittests': True,
            'xp': {
                'opt_unittest_suites' : UNITTEST_SUITES['opt_unittest_suites'][:],
                'debug_unittest_suites' : UNITTEST_SUITES['debug_unittest_suites'][:],
            },
            'win7': {
                'opt_unittest_suites' : UNITTEST_SUITES['opt_unittest_suites'][:],
                'debug_unittest_suites' : UNITTEST_SUITES['debug_unittest_suites'][:],
            }
        },
        'win64': {
            'builds_before_reboot': 1,
            'download_symbols': False,
            'enable_opt_unittests': True,
            # We can't yet run unit tests on debug builds - see bug 562459
            'enable_debug_unittests': False,
            'w764': {
                'opt_unittest_suites' : UNITTEST_SUITES['opt_unittest_suites'][:],
                'debug_unittest_suites' : UNITTEST_SUITES['debug_unittest_suites'][:],
            },
        },
        'macosx': {
            'builds_before_reboot': 1,
            'enable_opt_unittests': True,
            'enable_debug_unittests': True,
            'leopard-o': {
                'opt_unittest_suites' : [],
                'debug_unittest_suites' : removeSuite('mochitest-a11y', UNITTEST_SUITES['debug_unittest_suites'][:]),
            },
        },
        'macosx64': {
            'builds_before_reboot': 1,
            'enable_opt_unittests': True,
            'enable_debug_unittests': True,
            'leopard': {
                'opt_unittest_suites' : removeSuite('mochitest-a11y', UNITTEST_SUITES['opt_unittest_suites'][:]),
                'debug_unittest_suites' : [],
            },
            'snowleopard': {
                'opt_unittest_suites' : removeSuite('mochitest-a11y', UNITTEST_SUITES['opt_unittest_suites'][:]),
                'debug_unittest_suites' : removeSuite('mochitest-a11y', UNITTEST_SUITES['debug_unittest_suites'][:]),
            },
        },
        'linux-android': {
            'is_remote': True,
            'host_utils_url': 'http://bm-remote.build.mozilla.org/tegra/tegra-host-utils.zip',
            'remote_extras': UNITTEST_REMOTE_EXTRAS,
            'tegra_android': {
                'opt_unittest_suites': [
                    ('mochitest-1', (
                        {'suite': 'mochitest-plain',
                         'testPaths': [
                             'content/smil/test', 'content/xml/document/test',
                             'content/xslt/tests/mochitest'
                         ]
                        },
                    )),
                    ('mochitest-2', (
                        {'suite': 'mochitest-plain',
                         'testPaths': [
                             'dom/src/json/test', 'dom/src/jsurl/test',
                             'dom/tests/mochitest/dom-level0', 'js/jsd/test',
                             'js/src/xpconnect/tests/mochitest'
                         ]
                        },
                    )),
                    ('mochitest-3', (
                        {'suite': 'mochitest-plain',
                         'testPaths': ['dom/tests/mochitest/dom-level1-core']
                        },
                    )),
                    ('mochitest-4', (
                        {'suite': 'mochitest-plain',
                         'testPaths': ['dom/tests/mochitest/dom-level2-core']
                        },
                    )),
                    ('mochitest-5', (
                        {'suite': 'mochitest-plain',
                         'testPaths': ['dom/tests/mochitest/ajax/mochikit',
                                       'dom/tests/mochitest/ajax/scriptaculous',
                                       'dom/tests/mochitest/ajax/jquery'],
                        },
                    )),
                    ('mochitest-6', (
                        {'suite': 'mochitest-plain',
                         'testPaths': ['dom/tests/mochitest/dom-level2-html'],
                        },
                    )),
                    ('mochitest-7', (
                        {'suite': 'mochitest-plain',
                         'testPaths': ['Harness_sanity',
                                       'editor/composer/test',
                                       'intl/uconv/tests',
                                       'dom/tests/mochitest/orientation',
                                       'dom/tests/mochitest/storageevent'],
                        },
                    )),
                    ('mochitest-8', (
                        {'suite': 'mochitest-plain',
                         'testPaths': ['layout/xul/test',
                                       'modules/libjar/test/mochitest',
                                       'layout/inspector/tests',
                                       'toolkit/xre/test',
                                       'toolkit/components/microformats/tests',
                                       'MochiKit-1.4.2/tests',
                                       'parser/htmlparser/tests/mochitest'],
                       },
                    )),
                    ('browser-chrome', (
                        {'suite': 'mochitest-browser-chrome',
                         'testPaths': ['mobile']
                        },
                    )),
                    ('reftest-1', (
                        {'suite': 'reftest',
                         'totalChunks': 2,
                         'thisChunk': 1,
                        },
                    )),
                    ('reftest-2', (
                        {'suite': 'reftest',
                         'totalChunks': 2,
                         'thisChunk': 2,
                        },
                    )),
                    ('crashtest', (
                        {'suite': 'crashtest'},
                    )),
                    ('jsreftest-1', (
                        {'suite': 'jsreftest',
                         'totalChunks': 2,
                         'thisChunk': 1,
                        },
                    )),
                    ('jsreftest-2', (
                        {'suite': 'jsreftest',
                         'totalChunks': 2,
                         'thisChunk': 2,
                        },
                    )),
                ]
            },
        },
}

# Copy project branches into BRANCHES keys
for branch in ACTIVE_PROJECT_BRANCHES:
    BRANCHES[branch] = deepcopy(PROJECT_BRANCHES[branch])

# Copy unittest vars in first, then platform vars
for branch in BRANCHES.keys():
    for key, value in GLOBAL_VARS.items():
        # Don't override platforms if it's set
        if key == 'platforms' and 'platforms' in BRANCHES[branch]:
            continue
        BRANCHES[branch][key] = deepcopy(value)

    for key, value in BRANCH_UNITTEST_VARS.items():
        # Don't override platforms if it's set and locked
        if key == 'platforms' and 'platforms' in BRANCHES[branch] and BRANCHES[branch].get('lock_platforms'):
            continue
        BRANCHES[branch][key] = deepcopy(value)

    for platform, platform_config in PLATFORM_UNITTEST_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value

    # Copy in local config
    if branch in localconfig.BRANCHES:
        for key, value in localconfig.BRANCHES[branch].items():
            if key == 'platforms':
                # Merge in these values
                if 'platforms' not in BRANCHES[branch]:
                    BRANCHES[branch]['platforms'] = {}

                for platform, platform_config in value.items():
                    for key, value in platform_config.items():
                        value = deepcopy(value)
                        if isinstance(value, str):
                            value = value % locals()
                        BRANCHES[branch]['platforms'][platform][key] = value
            else:
                BRANCHES[branch][key] = deepcopy(value)
 
    # Merge in any project branch config for platforms
    if branch in ACTIVE_PROJECT_BRANCHES and PROJECT_BRANCHES[branch].has_key('platforms'):
        for platform, platform_config in PROJECT_BRANCHES[branch]['platforms'].items():
            if platform in PLATFORMS:
                for key, value in platform_config.items():
                    value = deepcopy(value)
                    if isinstance(value, str):
                        value = value % locals()
                    BRANCHES[branch]['platforms'][platform][key] = value

    for platform, platform_config in localconfig.PLATFORM_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value

### PROJECTS ###
PROJECTS = {
    'jetpack': {
        'platforms': {
            'w764': {'ext':'win64-x86_64.zip',}, 
            'fedora64': {'ext':'linux-x86_64.tar.bz2',}, 
            'fedora':{'ext':'linux-i686.tar.bz2'}, 
            'leopard':{'ext':'mac.dmg'}, 
            'snowleopard':{'ext':'mac.dmg'},   
            'xp':{
                'ext':'win32.zip',
                'env':PLATFORM_UNITTEST_VARS['win32']['env_name'],
                }, 
            'win7':{
                'ext':'win32.zip',
                'env':PLATFORM_UNITTEST_VARS['win32']['env_name'],
                }, 

            },
        'hgurl': 'http://hg.mozilla.org',
        'repo_path': 'projects/addon-sdk',
        'jetpack_tarball': 'archive/tip.tar.bz2',
        'ftp_url': 'ftp://ftp.mozilla.org/pub/mozilla.org/firefox/nightly/latest-mozilla-central',
    },
}
for k, v in localconfig.PROJECTS.items():
    if k not in PROJECTS:
        PROJECTS[k] = {}
    for k1, v1 in v.items():
        PROJECTS[k][k1] = v1

########
# Entries in BRANCHES for tests should be a tuple of:
# - Number of tests to run per build
# - Whether queue merging is on
# - TalosFactory options
# - Which platforms to run on

# Let's load the defaults
for branch in BRANCHES.keys():
    BRANCHES[branch]['branch_name'] = branch.title()
    BRANCHES[branch]['mobile_branch_name'] = branch.title()
    BRANCHES[branch]['build_branch'] = branch.title()
    BRANCHES[branch]['enable_unittests'] = True
    BRANCHES[branch]['talos_command'] = TALOS_CMD
    BRANCHES[branch]['fetch_symbols'] = True
    BRANCHES[branch]['fetch_release_symbols'] = False
    if BRANCHES[branch].has_key('release_branch'):
        BRANCHES[branch]['release_tests'] = 5
    BRANCHES[branch]['support_url_base'] = 'http://build.mozilla.org/talos'
    loadTalosSuites(BRANCHES, SUITES, branch)


# The following are exceptions to the defaults

######## mozilla-central
BRANCHES['mozilla-central']['branch_name'] = "Firefox"
BRANCHES['mozilla-central']['repo_path'] = "mozilla-central"
BRANCHES['mozilla-central']['mobile_branch_name'] = "Mobile"
BRANCHES['mozilla-central']['mobile_talos_branch'] = "mobile"
BRANCHES['mozilla-central']['build_branch'] = "1.9.2"
BRANCHES['mozilla-central']['platforms']['linux']['enable_mobile_unittests'] = True
BRANCHES['mozilla-central']['platforms']['linux']['fedora']['opt_unittest_suites'] += [('reftest-no-accel', ['opengl-no-accel'])]
BRANCHES['mozilla-central']['platforms']['linux-android']['enable_opt_unittests'] = True

######## mozilla-release
BRANCHES['mozilla-release']['repo_path'] = "releases/mozilla-release"
BRANCHES['mozilla-release']['platforms']['linux-android']['enable_opt_unittests'] = True
BRANCHES['mozilla-release']['platforms']['linux']['enable_mobile_unittests'] = True

######## mozilla-beta
BRANCHES['mozilla-beta']['repo_path'] = "releases/mozilla-beta"
BRANCHES['mozilla-beta']['platforms']['linux-android']['enable_opt_unittests'] = True
BRANCHES['mozilla-beta']['platforms']['linux']['enable_mobile_unittests'] = True

######## mozilla-aurora
BRANCHES['mozilla-aurora']['repo_path'] = "releases/mozilla-aurora"
BRANCHES['mozilla-aurora']['platforms']['linux-android']['enable_opt_unittests'] = True
BRANCHES['mozilla-aurora']['platforms']['linux']['enable_mobile_unittests'] = True

######## shadow-central
BRANCHES['shadow-central']['repo_path'] = "shadow-central"

######## mozilla-1.9.2
BRANCHES['mozilla-1.9.2']['branch_name'] = "Firefox3.6"
BRANCHES['mozilla-1.9.2']['mobile_branch_name'] = "Mobile1.1"
BRANCHES['mozilla-1.9.2']['build_branch'] = "1.9.2"
BRANCHES['mozilla-1.9.2']['chrome_tests'] = (1, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['nochrome_tests'] = (1, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['dromaeo_tests'] = (1, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['dirty_tests'] = (0, True, TALOS_DIRTY_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['tp4_tests'] = (1, True, TALOS_TP4_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['tp_tests'] = (0, True, TALOS_TP_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, OLD_BRANCH_NO_WIN)
BRANCHES['mozilla-1.9.2']['svg_tests'] = (1, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['scroll_tests'] = (1, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['a11y_tests'] = (0, True, {}, OLD_BRANCH_NO_MAC)
BRANCHES['mozilla-1.9.2']['paint_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['mozilla-1.9.2']['enable_unittests'] = False

######## addontester 
BRANCHES['addontester']['branch_name'] = "AddonTester"
BRANCHES['addontester']['mobile_branch_name'] = "AddonTester"
BRANCHES['addontester']['build_branch'] = "N/A"
BRANCHES['addontester']['talos_command'] = TALOS_ADDON_CMD
BRANCHES['addontester']['fetch_symbols'] = False
BRANCHES['addontester']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['addontester']['fetch_release_symbols'] = False
BRANCHES['addontester']['chrome_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['nochrome_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['dromaeo_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['dirty_tests'] = (0, True, TALOS_DIRTY_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['tp4_tests'] = (0, True, TALOS_TP4_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['tp_tests'] = (0, True, TALOS_TP_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, OLD_BRANCH_NO_WIN)
BRANCHES['addontester']['remote-ts_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addontester']['remote-tdhtml_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addontester']['remote-tsvg_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addontester']['remote-tsspider_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addontester']['remote-tpan_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addontester']['remote-tp4m_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addontester']['remote-tp4m_nochrome_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addontester']['remote-twinopen_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addontester']['remote-tzoom_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addontester']['svg_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['v8_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['scroll_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addontester']['addon_tests'] = (1, False, TALOS_ADDON_OPTS, OLD_BRANCH_ADDON_TESTER_PLATFORMS)
BRANCHES['addontester']['addon-baseline_tests'] = (0, False, TALOS_BASELINE_ADDON_OPTS, OLD_BRANCH_ADDON_TESTER_PLATFORMS)
BRANCHES['addontester']['a11y_tests'] = (0, True, {}, OLD_BRANCH_NO_MAC)
BRANCHES['addontester']['paint_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['addontester']['enable_unittests'] = False
######## addonbaselinetester - tests against 1.9.2
BRANCHES['addonbaselinetester']['branch_name'] = "AddonTester"
BRANCHES['addonbaselinetester']['mobile_branch_name'] = "AddonTester"
BRANCHES['addonbaselinetester']['build_branch'] = "N/A"
BRANCHES['addonbaselinetester']['talos_command'] = TALOS_ADDON_CMD
BRANCHES['addonbaselinetester']['fetch_symbols'] = False
BRANCHES['addonbaselinetester']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['addonbaselinetester']['fetch_release_symbols'] = False
BRANCHES['addonbaselinetester']['chrome_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['nochrome_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['dromaeo_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['dirty_tests'] = (0, True, TALOS_DIRTY_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['tp4_tests'] = (0, True, TALOS_TP4_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['tp_tests'] = (0, True, TALOS_TP_OPTS, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['cold_tests'] = (0, True, TALOS_DIRTY_OPTS, OLD_BRANCH_NO_WIN)
BRANCHES['addonbaselinetester']['remote-ts_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addonbaselinetester']['remote-tdhtml_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addonbaselinetester']['remote-tsvg_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addonbaselinetester']['remote-tsspider_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addonbaselinetester']['remote-tpan_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addonbaselinetester']['remote-tp4m_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addonbaselinetester']['remote-tp4m_nochrome_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addonbaselinetester']['remote-twinopen_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addonbaselinetester']['remote-tzoom_tests'] = (0, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['addonbaselinetester']['svg_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['v8_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['scroll_tests'] = (0, True, {}, OLD_BRANCH_ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, OLD_BRANCH_ADDON_TESTER_PLATFORMS)
BRANCHES['addonbaselinetester']['addon-baseline_tests'] = (1, False, TALOS_BASELINE_ADDON_OPTS, OLD_BRANCH_ADDON_TESTER_PLATFORMS)
BRANCHES['addonbaselinetester']['a11y_tests'] = (0, True, {}, OLD_BRANCH_NO_MAC)
BRANCHES['addonbaselinetester']['paint_tests'] = (0, True, {}, ALL_PLATFORMS)
BRANCHES['addonbaselinetester']['enable_unittests'] = False

######## try
BRANCHES['try']['branch_name'] = "Try"
BRANCHES['try']['mobile_branch_name'] = "Try"
BRANCHES['try']['build_branch'] = "Try"
BRANCHES['try']['talos_command'] = TALOS_CMD
BRANCHES['try']['fetch_symbols'] = True
BRANCHES['try']['support_url_base'] = 'http://build.mozilla.org/talos'
BRANCHES['try']['chrome_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['try']['nochrome_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['try']['dromaeo_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['try']['dirty_tests'] = (1, False, TALOS_DIRTY_OPTS, ALL_PLATFORMS)
BRANCHES['try']['tp4_tests'] = (1, False, TALOS_TP4_OPTS, ALL_PLATFORMS)
BRANCHES['try']['tp_tests'] = (1, False, TALOS_TP_OPTS, ALL_PLATFORMS)
BRANCHES['try']['cold_tests'] = (0, False, TALOS_DIRTY_OPTS, NO_WIN)
BRANCHES['try']['remote-ts_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['try']['remote-tdhtml_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['try']['remote-tsvg_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['try']['remote-tsspider_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['try']['remote-tpan_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['try']['remote-tp4m_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['try']['remote-tp4m_nochrome_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['try']['remote-twinopen_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['try']['remote-tzoom_tests'] = (1, True, TALOS_REMOTE_FENNEC_OPTS, ANDROID)
BRANCHES['try']['svg_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['try']['v8_tests'] = (0, False, {}, ALL_PLATFORMS)
BRANCHES['try']['scroll_tests'] = (1, False, {}, ALL_PLATFORMS)
BRANCHES['try']['addon_tests'] = (0, False, TALOS_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['try']['addon-baseline_tests'] = (0, False, TALOS_BASELINE_ADDON_OPTS, ALL_PLATFORMS)
BRANCHES['try']['a11y_tests'] = (1, False, {}, NO_MAC)
BRANCHES['try']['paint_tests'] = (1, True, {}, ALL_PLATFORMS)
BRANCHES['try']['repo_path'] = "try"
BRANCHES['try']['platforms']['linux']['fedora']['opt_unittest_suites'] += [('reftest-no-accel', ['opengl-no-accel'])]
BRANCHES['try']['platforms']['win32']['win7']['opt_unittest_suites'] += [('reftest-no-accel', ['reftest-no-d2d-d3d'])]
BRANCHES['try']['platforms']['linux-android']['enable_opt_unittests'] = True

# Let's load jetpack for the following branches:
for branch in ('mozilla-central', 'mozilla-aurora', 'try',  ):
    for pf in PLATFORMS:
        if pf in ('linux-android', ):
            continue
        for slave_pf in PLATFORMS[pf]['slave_platforms']:
            # These two mac excpetions are because we have been adding debug jetpack to macosx/leopard-o
            # and opt jetpack to macosx64/leopard. This probably was not correct but that's how it came about
            # XXX clean this mess in the next refactoring patch 
            if pf == "macosx" and slave_pf == "leopard-o":
                BRANCHES[branch]['platforms'][pf][slave_pf]['debug_unittest_suites'] += [('jetpack', ['jetpack'])]
                continue
            if pf == "macosx64" and slave_pf == "leopard":
                BRANCHES[branch]['platforms'][pf][slave_pf]['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
                continue
            BRANCHES[branch]['platforms'][pf][slave_pf]['opt_unittest_suites'] += [('jetpack', ['jetpack'])]
            BRANCHES[branch]['platforms'][pf][slave_pf]['debug_unittest_suites'] += [('jetpack', ['jetpack'])]

######## generic branch variables for project branches
for projectBranch in ACTIVE_PROJECT_BRANCHES:
    branchConfig = PROJECT_BRANCHES[projectBranch]
    loadDefaultValues(BRANCHES, projectBranch, branchConfig)
    loadCustomTalosSuites(BRANCHES, SUITES, projectBranch, branchConfig)
    loadCustomUnittestSuites(BRANCHES, projectBranch, branchConfig)

# This is here rather than in project_branches.py, because enabling it there
# will enable old-style, on-buildslave opt unittests due to the same file
# existing in both mozilla/ and mozilla-tests/.
BRANCHES['tracemonkey']['platforms']['linux-android']['enable_opt_unittests'] = True
BRANCHES['mozilla-inbound']['platforms']['linux-android']['enable_opt_unittests'] = True
BRANCHES['electrolysis']['platforms']['linux-android']['enable_opt_unittests'] = True
BRANCHES['fx-team']['platforms']['linux-android']['enable_opt_unittests'] = True
BRANCHES['ionmonkey']['platforms']['linux-android']['enable_opt_unittests'] = True
BRANCHES['jaegermonkey']['platforms']['linux-android']['enable_opt_unittests'] = True
BRANCHES['services-central']['platforms']['linux-android']['enable_opt_unittests'] = True
for b in ('accessibility', 'build-system', 'private-browsing', 'alder', 'birch', 'cedar', 'holly', 'larch', 'maple'):
    BRANCHES[b]['platforms']['linux-android']['enable_opt_unittests'] = True

if __name__ == "__main__":
    import sys, pprint, re

    class BBPrettyPrinter(pprint.PrettyPrinter):
        def format(self, object, context, maxlevels, level):
            if isinstance(object, WithProperties):
                return pprint.PrettyPrinter.format(self, object.fmtstring, context, maxlevels, level)
            return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)

    args = sys.argv[1:]

    if len(args) > 0:
        branches = args
    else:
        branches = BRANCHES.keys()

    pp = BBPrettyPrinter()
    for branch in branches:
        print branch
        pp.pprint(BRANCHES[branch])

    for suite in SUITES:
        print suite
        pp.pprint(SUITES[suite])
