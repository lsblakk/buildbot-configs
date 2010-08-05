SLAVES = {
    'fedora': ["talos-r3-fed-%03i" % x for x in range(1,54)],
    'fedora64' : ["talos-r3-fed64-%03i" % x for x in range (1,56)],
    'xp': ["talos-r3-xp-%03i" % x for x in range(1,54)],
    'win7': ["talos-r3-w7-%03i" % x for x in range(1,54)],
    'w764': ["t-r3-w764-%03i" % x for x in range(1,51)],
    'leopard': ["talos-r3-leopard-%03i" % x for x in range(1,54)],
    'snowleopard': ["talos-r3-snow-%03i" % x for x in range(1,56)],
}

GRAPH_CONFIG = ['--resultsServer', 'graphs.mozilla.org',
    '--resultsLink', '/server/collect.cgi']

GLOBAL_VARS = {
    'build_tools_repo_path': 'build/tools',
}

# Local branch overrides
BRANCHES = {
    'mozilla-central': {
        'tinderbox_tree': 'Firefox',
    },
    'shadow-central': {
        'tinderbox_tree': 'Shadow-Central',
    },
    'mozilla-2.0': {
        'tinderbox_tree': 'Firefox4.0',
    },
    'mozilla-1.9.1': {
        'tinderbox_tree': 'Firefox3.5',
    },
    'mozilla-1.9.2': {
        'tinderbox_tree': 'Firefox3.6',
    },
    'tracemonkey': {
        'tinderbox_tree': 'TraceMonkey',
    },
    'places': {
        'tinderbox_tree': 'Places',
    },
    'electrolysis': {
        'tinderbox_tree': 'Electrolysis',
    },
    'addontester': {
        'tinderbox_tree': 'Firefox3.6',
    },
    'tryserver': {
        'tinderbox_tree': 'MozillaTry',
        'enable_mail_notifier': True,
        'enable_merging': False,
        'package_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox/tryserver-builds',
        'package_dir': '%(who)s-%(got_revision)s',
    },
    'birch': {
        'tinderbox_tree': 'Birch',
    },
    'cedar': {
        'tinderbox_tree': 'Cedar',
    },
    'maple': {
        'tinderbox_tree': 'Maple',
    },
    'jaegermonkey': {
        'tinderbox_tree': 'Jaegermonkey',
    },

}

PLATFORM_VARS = {
}