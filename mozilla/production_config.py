MAC_SNOW_MINIS = ['moz2-darwin10-slave%02i' % x for x in range(5,10) + range(11,30) + range(40,53)]
MAC_MINIS      = ['moz2-darwin9-slave%02i' % x for x in [1,2,5,6,7] + range(9,10) + range(11,27) + range(29,68) + range(69,73)]
XSERVES        = ['bm-xserve%02i' % x for x in [6,7,8,9,10,11,12,15,16,17,18,19,20,21,22,23,24]]
LINUX_VMS      = ['moz2-linux-slave%02i' % x for x in [1,2] + range(5,10) + range(11,17) + range(18,47)]
LINUX64_VMS    = ['moz2-linux64-slave%02i' % x for x in range(1,7) + range(8,10) + range(11,13)]
LINUX_IXS      = ['mv-moz2-linux-ix-slave%02i' % x for x in range(2,22)] + ['linux-ix-slave%02i' % x for x in range(12,43)]
WIN32_VMS      = ['win32-slave%02i' % x for x in [1,2] + range(5,10) + range(11,21) + range(22,50)]
WIN32_IXS      = ['mw32-ix-slave%02i' % x for x in range(2,22)] + ['w32-ix-slave%02i' % x for x in range(22,43)]
SLAVES = {
    'linux':       LINUX_VMS + LINUX_IXS,
    'linux64':     LINUX64_VMS,
    'win32':       WIN32_VMS + WIN32_IXS,
    'macosx':      MAC_MINIS + XSERVES,
    'macosx64':    MAC_SNOW_MINIS,
}

TRY_LINUX      = ['try-linux-slave%02i' % x for x in range(1,5) + range(6,31)] + \
                 ['moz2-linux-slave%02i' % x for x in range(47,51)]
TRY_LINUX_IXS  = ['mv-moz2-linux-ix-slave%02i' % x for x in range(22,24)] + \
                 ['linux-ix-slave%02i' % x for x in range(3,12)]
TRY_LINUX64    = ['try-linux64-slave%02i' % x for x in range(1,11)]
TRY_MAC        = ['try-mac-slave%02i' % x for x in range(1,5) + range(6,48)]
TRY_XSERVES    = ['bm-xserve%02i' % x for x in [8,10,20,23,24]]
TRY_MAC64      = ['try-mac64-slave%02i' % x for x in range(1,27)]
TRY_WIN32      = ['try-w32-slave%02i' % x for x in range(1,5) + range(6,37)] + \
                 ['win32-slave%02i' % x for x in range(50,60)]
TRY_WIN32_IXS  = ['mw32-ix-slave%02i' % x for x in range(22,26)] + \
                 ['w32-ix-slave%02i' % x for x in range(3,22)]
TRY_SLAVES = {
    'linux':       TRY_LINUX + TRY_LINUX_IXS,
    'linux64':     TRY_LINUX64,
    'win32':       TRY_WIN32 + TRY_WIN32_IXS,
    'macosx':      TRY_MAC + TRY_XSERVES,
    'macosx64':    TRY_MAC64,
}


# Local overrides for default values
GLOBAL_VARS = {
    'config_repo_path': 'build/buildbot-configs',
    'buildbotcustom_repo_path': 'build/buildbotcustom',
    'stage_server': 'stage.mozilla.org',
    'aus2_host': 'aus2-staging.mozilla.org',
    'download_base_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox',
    'mobile_download_base_url': 'http://ftp.mozilla.org/pub/mozilla.org/mobile',
    'graph_server': 'graphs.mozilla.org',
    'build_tools_repo_path': 'build/tools',
    'base_clobber_url': 'http://build.mozilla.org/clobberer/index.php',
    # List of talos masters to notify of new builds,
    # and if a failure to notify the talos master should result in a warning,
    # and sendchange retry count before give up
    'talos_masters': [
        ('production-master01.build.mozilla.org:9009', True, 5),
        ('talos-master.mozilla.org:9010', True, 5),
        ('staging-master.build.mozilla.org:9009', False, 1),
        ('talos-staging-master02.build.mozilla.org:9012', False, 1),
    ],
    # List of unittest masters to notify of new builds to test,
    # if a failure to notify the master should result in a warning,
    # and sendchange retry count before give up
    'unittest_masters': [
        ('production-master01.build.mozilla.org:9009', True, 5),
        ('staging-master.build.mozilla.org:9009', False, 1),
        ('talos-staging-master02.build.mozilla.org:9012', False, 1),
        ('geriatric-master.build.mozilla.org:9989', False, 1),
    ],
    'xulrunner_tinderbox_tree': 'XULRunner',
    'weekly_tinderbox_tree': 'Testing',
    'l10n_tinderbox_tree': 'Mozilla-l10n',
}

BUILDS_BEFORE_REBOOT = 1
SYMBOL_SERVER_HOST = 'dm-symbolpush01.mozilla.org'

# Local branch overrides
BRANCHES = {
    'mozilla-central': {
        'packaged_unittest_tinderbox_tree': 'Firefox',
        'tinderbox_tree': 'Firefox',
        'mobile_tinderbox_tree': 'Mobile',
        'mobile_build_failure_emails': ['mobile-build-failures@mozilla.org'],
    },
    'shadow-central': {
        'packaged_unittest_tinderbox_tree': 'Shadow-Central',
        'tinderbox_tree': 'Shadow-Central',
        'mobile_tinderbox_tree': 'Shadow-Central',
        'mobile_build_failure_emails': ['mobile-build-failures@mozilla.org'],
        'build_tools_repo_path' : 'http://hg.mozilla.org/build/tools',
        'stage_server' : 'dm-pvtbuild01.mozilla.org',
        'hghost' : 'ssh://ffxbld@hgpvt.mozilla.org',
        'stage_base_path' : '/mnt/pvt_builds',
        'stage_log_base_url': 'https://dm-pvtbuild01.mozilla.org',
    },
    'mozilla-1.9.1': {
        'packaged_unittest_tinderbox_tree': 'Firefox3.5',
        'tinderbox_tree': 'Firefox3.5',
        'mobile_tinderbox_tree': 'MobileTest',
    },
    'mozilla-1.9.2': {
        'tinderbox_tree': 'Firefox3.6',
        'packaged_unittest_tinderbox_tree': 'Firefox3.6',
        'mobile_tinderbox_tree': 'Mobile1.1',
    },
    'mozilla-2.0': {
        'tinderbox_tree': 'Firefox4.0',
        'packaged_unittest_tinderbox_tree': 'Firefox4.0',
    },
    'tracemonkey': {
        'tinderbox_tree': 'TraceMonkey',
        'mobile_tinderbox_tree': 'TraceMonkey',
        'packaged_unittest_tinderbox_tree': 'TraceMonkey',
    },
    'places': {
        'tinderbox_tree': 'Places',
        'mobile_tinderbox_tree': 'Places',
        'packaged_unittest_tinderbox_tree': 'Places',
    },
    'electrolysis': {
        'tinderbox_tree': 'Electrolysis',
        'mobile_tinderbox_tree': 'Electrolysis',
        'packaged_unittest_tinderbox_tree': 'Electrolysis',
    },
    'addonsmgr': {
        'tinderbox_tree': 'AddonsMgr',
        'mobile_tinderbox_tree': 'AddonsMgr',
        'packaged_unittest_tinderbox_tree': 'AddonsMgr',
    },
    'jaegermonkey': {
        'tinderbox_tree': 'Jaegermonkey',
        'mobile_tinderbox_tree': 'Jaegermonkey',
        'packaged_unittest_tinderbox_tree': 'Jaegermonkey',
    },
    'tryserver': {
        'tinderbox_tree': 'MozillaTry',
        'graph_branch': 'Tryserver',
        'mobile_tinderbox_tree': 'MozillaTry',
        'packaged_unittest_tinderbox_tree': 'MozillaTry',
        'download_base_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox/tryserver-builds',
        'mobile_download_base_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox/tryserver-builds',
        'enable_mail_notifier': True,
        'notify_real_author': True,
        'package_url': 'http://ftp.mozilla.org/pub/mozilla.org/firefox/tryserver-builds',
        'talos_masters': [],
        'platforms': {
            'win32': {
                'env': {
                    'SYMBOL_SERVER_HOST': 'build.mozilla.org',
                    'CVS_RSH': 'ssh',
                    'MOZ_OBJDIR': 'obj-firefox',
                    'TINDERBOX_OUTPUT': '1',
                    'MOZ_CRASHREPORTER_NO_REPORT': '1',
                    # Source server support, bug 506702
                    'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe',
                    'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
                }
            }
        }
    },
   'maple': {
        'tinderbox_tree': 'Maple',
        'mobile_tinderbox_tree': 'Maple',
        'packaged_unittest_tinderbox_tree': 'Maple',
    },
    'cedar': {
        'tinderbox_tree': 'Cedar',
        'mobile_tinderbox_tree': 'Cedar',
        'packaged_unittest_tinderbox_tree': 'Cedar',
    },
    'birch': {
        'tinderbox_tree': 'Birch',
        'mobile_tinderbox_tree': 'Birch',
        'packaged_unittest_tinderbox_tree': 'Birch',
    },

}

PLATFORM_VARS = {
}

PROJECTS = {
    'fuzzing': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'fuzzing_repo': 'ssh://ffxbld@hg.mozilla.org/private/fuzzing',
        'fuzzing_remote_host': 'ffxbld@dm-pvtbuild01.mozilla.org',
        # Path needs extra leading slash due to optparse expansion on Win32
        'fuzzing_base_dir': '//mnt/pvt_builds/fuzzing/',
        'idle_slaves': 3,
    },
    'nanojit': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 3,
        'tinderbox_tree': 'Nanojit',
    },
    'valgrind': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 3, # 3 slaves have to be idle before we start
        'tinderbox_tree': 'Firefox',
    },
    'spidermonkey': {
        'scripts_repo': 'http://hg.mozilla.org/build/tools',
        'idle_slaves': 0,
        'tinderbox_tree': 'TraceMonkey',
    },
}
