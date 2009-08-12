hgUsername          = 'stage-ffxbld'
hgSshKey            = '~cltbld/.ssh/ffxbld_dsa'
sourceRepoName      = 'mozilla-central'
# This parameter (and it's l10n equivalent) is for staging only and necessary
# because the repo_setup builder needs to know where to clone repositories from.
# It is not used for anything else.
sourceRepoClonePath = sourceRepoName
sourceRepoPath      = 'users/stage-ffxbld/mozilla-central'
sourceRepoRevision  = '5c913c4662d8'
relbranchOverride   = ''
l10nRepoClonePath   = 'l10n-central'
l10nRepoPath        = 'users/stage-ffxbld'
l10nRevisionFile    = 'l10n-changesets'
cvsroot             = ':ext:stgbld@cvs.mozilla.org:/cvsroot'
productName         = 'firefox'
appName             = 'browser'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version             = '3.6a1'
appVersion          = version
milestone           = '1.9.2a1'
buildNumber         = 1
baseTag             = 'FIREFOX_3_6a1'
oldVersion          = ''
oldAppVersion       = ''
oldBuildNumber      = 1
oldBaseTag          = ''
releasePlatforms    = ('linux', 'win32', 'macosx')
# TODO: create this file before 3.6a2
patcherConfig       = 'moz192-branch-patcher2.cfg'
patcherToolsTag     = 'UPDATE_PACKAGING_R9'
ftpServer           = 'ftp.mozilla.org'
stagingServer       = 'staging-stage.build.mozilla.org'
bouncerServer       = 'download.mozilla.org'
ausServerUrl        = 'http://staging-stage.build.mozilla.org'
useBetaChannel      = 0
# TODO: create these files before 3.6a2
verifyConfigs       = {'linux':  'moz192-firefox-linux.cfg',
                       'macosx': 'moz192-firefox-mac.cfg',
                       'win32':  'moz192-firefox-win32.cfg'}