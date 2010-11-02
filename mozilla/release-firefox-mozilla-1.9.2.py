releaseConfig = {}

releaseConfig['hgUsername']          = 'ffxbld'
releaseConfig['hgSshKey']            = '~cltbld/.ssh/ffxbld_dsa'
releaseConfig['sourceRepoName']      = 'mozilla-1.9.2'
releaseConfig['sourceRepoPath']      = 'releases/mozilla-1.9.2'
releaseConfig['sourceRepoRevision']  = '2cfbdde77508'
releaseConfig['relbranchOverride']   = 'GECKO19211_20100930_RELBRANCH'
releaseConfig['l10nRepoPath']        = 'releases/l10n-mozilla-1.9.2'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mozilla-1.9.2'
releaseConfig['mergeLocales']        = False
releaseConfig['cvsroot']             = ':ext:cltbld@cvs.mozilla.org:/cvsroot'
releaseConfig['productName']         = 'firefox'
releaseConfig['appName']             = 'browser'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
releaseConfig['version']             = '3.6.11'
releaseConfig['appVersion']          = releaseConfig['version']
releaseConfig['milestone']           = '1.9.2.11'
releaseConfig['buildNumber']         = 3
releaseConfig['baseTag']             = 'FIREFOX_3_6_11'
releaseConfig['oldVersion']          = '3.6.10'
releaseConfig['oldAppVersion']       = releaseConfig['oldVersion']
releaseConfig['oldBuildNumber']      = 1
releaseConfig['oldBaseTag']          = 'FIREFOX_3_6_10'
releaseConfig['enUSPlatforms']       = ('linux', 'win32', 'macosx')
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['talosTestPlatforms']  = releaseConfig['enUSPlatforms']
releaseConfig['unittestPlatforms']   = releaseConfig['enUSPlatforms']
releaseConfig['xulrunnerPlatforms']  = releaseConfig['enUSPlatforms']
releaseConfig['patcherConfig']       = 'moz192-branch-patcher2.cfg'
releaseConfig['patcherToolsTag']     = 'UPDATE_PACKAGING_R11'
releaseConfig['binaryName']          = releaseConfig['productName'].capitalize()
releaseConfig['oldBinaryName']       = releaseConfig['binaryName']
releaseConfig['ftpServer']           = 'ftp.mozilla.org'
releaseConfig['stagingServer']       = 'stage-old.mozilla.org'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'https://aus2.mozilla.org'
releaseConfig['ausUser']             = 'cltbld'
releaseConfig['ausSshKey']           = 'cltbld_dsa'
releaseConfig['releaseNotesUrl']     = None
releaseConfig['testOlderPartials']   = True
releaseConfig['useBetaChannel']      = 1
releaseConfig['verifyConfigs']       = {
    'linux':  'moz192-firefox-linux.cfg',
    'macosx': 'moz192-firefox-mac.cfg',
    'win32':  'moz192-firefox-win32.cfg'
}
releaseConfig['doPartnerRepacks']    = True
releaseConfig['partnersRepoPath']    = 'build/partner-repacks'
releaseConfig['majorUpdateRepoPath'] = None
# Tuxedo/Bouncer related
releaseConfig['tuxedoConfig']        = 'firefox-tuxedo.ini'
releaseConfig['tuxedoServerUrl']     = 'https://bounceradmin.mozilla.com/api/'
