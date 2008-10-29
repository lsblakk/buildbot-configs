hgHost            = 'hg.mozilla.org'
hgUsername        = 'stage-ffxbld'
hgSshKey          = '~cltbld/.ssh/ffxbld_dsa'
mozillaCentral    = 'http://hg.mozilla.org/users/stage-ffxbld/mozilla-central/'
mozillaCentralRevision = 'd7d64f68423b'
relbranchOverride = ''
baseTag           = 'FIREFOX_3_1b2'
l10nCentral       = 'http://hg.mozilla.org/users/stage-ffxbld/'
l10nRevisionFile  = 'l10n-changesets'
buildTools        = 'http://hg.mozilla.org/build/tools/'
cvsroot           = ':ext:stgbld@cvs.mozilla.org:/cvsroot'
productName       = 'firefox'
appName           = 'browser'
appVersion        = '3.1b2'
milestone         = '1.9.1b2'
buildNumber       = 1
oldVersion        = '3.1b1'
releasePlatforms  = ('linux', 'win32', 'macosx')
patcherConfig     = 'moz191-branch-patcher2.cfg'
patcherToolsTag   = 'UPDATE_PACKAGING_R6'
ftpServer         = 'ftp.mozilla.org'
stagingServer     = 'staging-stage.build.mozilla.org'
bouncerServer     = 'download.mozilla.org'
useBetaChannel    = 0
linuxUpdateVerifyConfig = 'moz191-firefox-linux.cfg'
macUpdateVerifyConfig   = 'moz191-firefox-mac.cfg'
win32UpdateVerifyConfig = 'moz191-firefox-win32.cfg'
