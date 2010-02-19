SLAVES = {
    'n810': ['maemo-n810-%02i' % x for x in [1,3,4,5,6] + range(9,81)],
}

BRANCHES = {
    'mozilla-central': {},
    'mozilla-1.9.2': {},
    'tracemonkey'  : {},
}

#
# {{{1 mozilla-central
#
BRANCHES['mozilla-central']['tinderbox_tree'] = "Mobile"
BRANCHES['mozilla-central']['graph_server'] = "graphs.mozilla.org"
BRANCHES['mozilla-central']['platforms'] = {
    'n810': {},
}
BRANCHES['mozilla-central']['platforms']['n810']['base_name'] = 'Maemo mozilla-central'
BRANCHES['mozilla-central']['platforms']['n810']['slaves'] = SLAVES['n810']
BRANCHES['mozilla-central']['platforms']['n810']['buildbot_branch'] = 'maemo-trunk'
BRANCHES['mozilla-central']['platforms']['n810']['talos_branch'] = 'mobile'
BRANCHES['mozilla-central']['platforms']['n810']['poll_interval'] = 5*60
BRANCHES['mozilla-central']['platforms']['n810']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-trunk/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-trunk/',
]
BRANCHES['mozilla-central']['platforms']['n810']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-trunk/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-trunk/',
]
BRANCHES['mozilla-central']['platforms']['n810']['poller_string'] = 'fennec-.*\.en-US\.linux.*arm\.tar\.bz2'
BRANCHES['mozilla-central']['platforms']['n810']['talos_scripts'] = 'http://production-mobile-master.build.mozilla.org/maemo/talos.tar.bz2'
BRANCHES['mozilla-central']['platforms']['n810']['talos_pageloader'] = 'http://production-mobile-master.build.mozilla.org/maemo/pageloader.tar.bz2'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites'] = {
    'tp4': {},
    'tp4_nochrome': {},
    'tpan': {},
    'tzoom': {},
    'ts': {},
    'twinopen': {},
    'tdhtml': {},
    'tsvg': {},
    'tsspider': {},
    'tgfx': {},
}
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tp4']['suite_name'] = 'N810 mozilla-central talos Tp4'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tp4']['build_dir'] = 'n810-trunk-tp4'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tp4']['config_file'] = 'mobile.config'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tp4']['timeout'] = 90
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tp4_nochrome']['suite_name'] = 'N810 mozilla-central talos Tp4 nochrome'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tp4_nochrome']['build_dir'] = 'n810-trunk-tp4-nochrome'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tp4_nochrome']['config_file'] = 'mobile.config'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tp4_nochrome']['timeout'] = 90
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tpan']['suite_name'] = 'N810 mozilla-central talos Tpan'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tpan']['build_dir'] = 'n810-trunk-tpan'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tpan']['config_file'] = 'mobile.config'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tpan']['timeout'] = 60
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tzoom']['suite_name'] = 'N810 mozilla-central talos Tzoom'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tzoom']['build_dir'] = 'n810-trunk-tzoom'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tzoom']['config_file'] = 'mobile.config'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tzoom']['timeout'] = 60
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['ts']['suite_name'] = 'N810 mozilla-central talos Ts'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['ts']['build_dir'] = 'n810-trunk-ts'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['ts']['config_file'] = 'mobile.config'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['ts']['timeout'] = 60
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['twinopen']['suite_name'] = 'N810 mozilla-central talos Twinopen'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['twinopen']['build_dir'] = 'n810-trunk-twinopen'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['twinopen']['config_file'] = 'mobile.config'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['twinopen']['timeout'] = 60
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tdhtml']['suite_name'] = 'N810 mozilla-central talos Tdhtml'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tdhtml']['build_dir'] = 'n810-trunk-tdhtml'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tdhtml']['config_file'] = 'mobile.config'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tdhtml']['timeout'] = 60
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tsvg']['suite_name'] = 'N810 mozilla-central talos Tsvg'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tsvg']['build_dir'] = 'n810-trunk-tsvg'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tsvg']['config_file'] = 'mobile.config'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tsvg']['timeout'] = 60
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tsspider']['suite_name'] = 'N810 mozilla-central talos Tsspider'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tsspider']['build_dir'] = 'n810-trunk-tsspider'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tsspider']['config_file'] = 'mobile.config'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tsspider']['timeout'] = 60
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tgfx']['suite_name'] = 'N810 mozilla-central talos Tgfx'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tgfx']['build_dir'] = 'n810-trunk-tgfx'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tgfx']['config_file'] = 'mobile.config'
BRANCHES['mozilla-central']['platforms']['n810']['talos_suites']['tgfx']['timeout'] = 60
BRANCHES['mozilla-central']['platforms']['n810']['test_suites'] = {
    'reftest':    {},
    'crashtest':  {},
    'xpcshell':   {},
}
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['reftest']['knownFailCount'] = 98
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['crashtest']['knownFailCount'] = 4
BRANCHES['mozilla-central']['platforms']['n810']['test_suites']['xpcshell']['knownFailCount'] = 182

#
# {{{1 mozilla-1.9.2
#
BRANCHES['mozilla-1.9.2']['tinderbox_tree'] = "Mobile"
BRANCHES['mozilla-1.9.2']['graph_server'] = "graphs.mozilla.org"
BRANCHES['mozilla-1.9.2']['platforms'] = {
    'n810': {},
}
BRANCHES['mozilla-1.9.2']['platforms']['n810']['base_name'] = 'Maemo mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['slaves'] = SLAVES['n810']
BRANCHES['mozilla-1.9.2']['platforms']['n810']['buildbot_branch'] = 'maemo-1.9.2'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_branch'] = 'mobile-1.9.2'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['poll_interval'] = 5*60
BRANCHES['mozilla-1.9.2']['platforms']['n810']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-1.9.2/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-1.9.2/',
]
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-1.9.2/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-1.9.2/',
]
BRANCHES['mozilla-1.9.2']['platforms']['n810']['poller_string'] = 'fennec-.*\.en-US\.linux.*arm\.tar\.bz2'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_scripts'] = 'http://production-mobile-master.build.mozilla.org/maemo/talos.tar.bz2'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_pageloader'] = 'http://production-mobile-master.build.mozilla.org/maemo/pageloader.tar.bz2'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites'] = {
    'tp4': {},
    'tp4_nochrome': {},
    'tpan': {},
    'tzoom': {},
    'ts': {},
    'twinopen': {},
    'tdhtml': {},
    'tsvg': {},
    'tsspider': {},
    'tgfx': {},
}
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tp4']['suite_name'] = 'N810 mozilla-1.9.2 talos Tp4'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tp4']['build_dir'] = 'n810-1.9.2-tp4'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tp4']['config_file'] = 'mobile.config'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tp4']['timeout'] = 90
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tp4_nochrome']['suite_name'] = 'N810 mozilla-1.9.2 talos Tp4 nochrome'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tp4_nochrome']['build_dir'] = 'n810-1.9.2-tp4-nochrome'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tp4_nochrome']['config_file'] = 'mobile.config'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tp4_nochrome']['timeout'] = 90
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tpan']['suite_name'] = 'N810 mozilla-1.9.2 talos Tpan'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tpan']['build_dir'] = 'n810-1.9.2-tpan'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tpan']['config_file'] = 'mobile.config'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tpan']['timeout'] = 60
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tzoom']['suite_name'] = 'N810 mozilla-1.9.2 talos Tzoom'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tzoom']['build_dir'] = 'n810-1.9.2-tzoom'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tzoom']['config_file'] = 'mobile.config'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tzoom']['timeout'] = 60
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['ts']['suite_name'] = 'N810 mozilla-1.9.2 talos Ts'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['ts']['build_dir'] = 'n810-1.9.2-ts'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['ts']['config_file'] = 'mobile.config'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['ts']['timeout'] = 60
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['twinopen']['suite_name'] = 'N810 mozilla-1.9.2 talos Twinopen'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['twinopen']['build_dir'] = 'n810-1.9.2-twinopen'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['twinopen']['config_file'] = 'mobile.config'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['twinopen']['timeout'] = 60
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tdhtml']['suite_name'] = 'N810 mozilla-1.9.2 talos Tdhtml'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tdhtml']['build_dir'] = 'n810-1.9.2-tdhtml'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tdhtml']['config_file'] = 'mobile.config'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tdhtml']['timeout'] = 60
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tsvg']['suite_name'] = 'N810 mozilla-1.9.2 talos Tsvg'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tsvg']['build_dir'] = 'n810-1.9.2-tsvg'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tsvg']['config_file'] = 'mobile.config'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tsvg']['timeout'] = 60
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tsspider']['suite_name'] = 'N810 mozilla-1.9.2 talos Tsspider'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tsspider']['build_dir'] = 'n810-1.9.2-tsspider'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tsspider']['config_file'] = 'mobile.config'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tsspider']['timeout'] = 60
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tgfx']['suite_name'] = 'N810 mozilla-1.9.2 talos Tgfx'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tgfx']['build_dir'] = 'n810-1.9.2-tgfx'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tgfx']['config_file'] = 'mobile.config'
BRANCHES['mozilla-1.9.2']['platforms']['n810']['talos_suites']['tgfx']['timeout'] = 60
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites'] = {
    'reftest':    {},
    'crashtest':  {},
    'xpcshell':   {},
}
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['reftest']['knownFailCount'] = 98
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['crashtest']['knownFailCount'] = 4
BRANCHES['mozilla-1.9.2']['platforms']['n810']['test_suites']['xpcshell']['knownFailCount'] = 182

#
# {{{1 TraceMonkey
#
BRANCHES['tracemonkey']['tinderbox_tree'] = "TraceMonkey"
BRANCHES['tracemonkey']['graph_server'] = "graphs.mozilla.org"
BRANCHES['tracemonkey']['platforms'] = {
    'n810': {},
}
BRANCHES['tracemonkey']['platforms']['n810']['base_name'] = 'Maemo tracemonkey'
BRANCHES['tracemonkey']['platforms']['n810']['slaves'] = SLAVES['n810']
BRANCHES['tracemonkey']['platforms']['n810']['buildbot_branch'] = 'maemo-tm'
BRANCHES['tracemonkey']['platforms']['n810']['talos_branch'] = 'mobile-tracemonkey'
BRANCHES['tracemonkey']['platforms']['n810']['poll_interval'] = 5*60
BRANCHES['tracemonkey']['platforms']['n810']['unit_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-tracemonkey/',
]
BRANCHES['tracemonkey']['platforms']['n810']['talos_build_dirs'] = [
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/mobile-tracemonkey/',
    'http://ftp.mozilla.org/pub/mozilla.org/mobile/nightly/latest-mobile-tracemonkey/',
]
BRANCHES['tracemonkey']['platforms']['n810']['poller_string'] = 'fennec-.*\.en-US\.linux.*arm\.tar\.bz2'
BRANCHES['tracemonkey']['platforms']['n810']['talos_scripts'] = 'http://production-mobile-master.build.mozilla.org/maemo/talos.tar.bz2'
BRANCHES['tracemonkey']['platforms']['n810']['talos_pageloader'] = 'http://production-mobile-master.build.mozilla.org/maemo/pageloader.tar.bz2'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites'] = {
    'tp4': {},
    'tp4_nochrome': {},
    'tpan': {},
    'tzoom': {},
    'ts': {},
    'twinopen': {},
    'tdhtml': {},
    'tsvg': {},
    'tsspider': {},
    'tgfx': {},
}
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tp4']['suite_name'] = 'N810 tracemonkey talos Tp4'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tp4']['build_dir'] = 'n810-tm-tp4'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tp4']['config_file'] = 'mobile.config'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tp4']['timeout'] = 90
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tp4_nochrome']['suite_name'] = 'N810 tracemonkey talos Tp4 nochrome'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tp4_nochrome']['build_dir'] = 'n810-tm-tp4-nochrome'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tp4_nochrome']['config_file'] = 'mobile.config'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tp4_nochrome']['timeout'] = 90
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tpan']['suite_name'] = 'N810 tracemonkey talos Tpan'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tpan']['build_dir'] = 'n810-tm-tpan'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tpan']['config_file'] = 'mobile.config'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tpan']['timeout'] = 60
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tzoom']['suite_name'] = 'N810 tracemonkey talos Tzoom'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tzoom']['build_dir'] = 'n810-tm-tzoom'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tzoom']['config_file'] = 'mobile.config'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tzoom']['timeout'] = 60
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['ts']['suite_name'] = 'N810 tracemonkey talos Ts'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['ts']['build_dir'] = 'n810-tm-ts'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['ts']['config_file'] = 'mobile.config'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['ts']['timeout'] = 60
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['twinopen']['suite_name'] = 'N810 tracemonkey talos Twinopen'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['twinopen']['build_dir'] = 'n810-tm-twinopen'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['twinopen']['config_file'] = 'mobile.config'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['twinopen']['timeout'] = 60
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tdhtml']['suite_name'] = 'N810 tracemonkey talos Tdhtml'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tdhtml']['build_dir'] = 'n810-tm-tdhtml'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tdhtml']['config_file'] = 'mobile.config'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tdhtml']['timeout'] = 60
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tsvg']['suite_name'] = 'N810 tracemonkey talos Tsvg'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tsvg']['build_dir'] = 'n810-tm-tsvg'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tsvg']['config_file'] = 'mobile.config'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tsvg']['timeout'] = 60
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tsspider']['suite_name'] = 'N810 tracemonkey talos Tsspider'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tsspider']['build_dir'] = 'n810-tm-tsspider'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tsspider']['config_file'] = 'mobile.config'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tsspider']['timeout'] = 60
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tgfx']['suite_name'] = 'N810 tracemonkey talos Tgfx'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tgfx']['build_dir'] = 'n810-tm-tgfx'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tgfx']['config_file'] = 'mobile.config'
BRANCHES['tracemonkey']['platforms']['n810']['talos_suites']['tgfx']['timeout'] = 60
BRANCHES['tracemonkey']['platforms']['n810']['test_suites'] = {
    'reftest':    {},
    'crashtest':  {},
    'xpcshell':   {},
}
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['reftest']['knownFailCount'] = 98
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['crashtest']['knownFailCount'] = 4
BRANCHES['tracemonkey']['platforms']['n810']['test_suites']['xpcshell']['knownFailCount'] = 182
