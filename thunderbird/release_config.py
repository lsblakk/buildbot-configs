hgUsername                 = 'tbirdbld'
hgSshKey                   = '~cltbld/.ssh/tbirdbld_dsa'
relbranchPrefix            = 'COMM'
sourceRepoName             = 'comm-central' # buildbot branch name
sourceRepoPath             = 'comm-central'
sourceRepoRevision         = '9125466f2b34'
relbranchOverride          = ''
mozillaRepoPath            = 'releases/mozilla-1.9.1'
mozillaRepoRevision        = 'd08f35b964dd'
#mozillaRelbranchOverride   = 'GECKO1913_20090824_RELBRANCH' # put Gecko relbranch here that we base upon
mozillaRelbranchOverride   = ''
inspectorRepoPath          = 'dom-inspector' # leave empty if inspector is not to be tagged
inspectorRepoRevision      = '653c0e6ca601'
inspectorRelbranchOverride = ''
venkmanRepoPath            = '' # leave empty if venkman is not to be tagged
venkmanRepoRevision        = ''
venkmanRelbranchOverride   = ''
chatzillaCVSRoot           = ''
chatzillaTimestamp         = '' # leave empty if chatzilla is not to be tagged
l10nRepoPath               = 'releases/l10n-mozilla-1.9.1'
l10nRevisionFile           = 'l10n-changesets'
toolsRepoPath              = 'build/tools'
cvsroot                    = ':ext:cltbld@cvs.mozilla.org:/cvsroot' # for patcher, etc.
productVersionFile         = 'mail/config/version-191.txt'
productName                = 'thunderbird'
brandName                  = 'Thunderbird'
appName                    = 'mail'
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version                    = '3.0b4'
appVersion                 = version
milestone                  = '1.9.1.3'
buildNumber                = 1
baseTag                    = 'THUNDERBIRD_3_0b4'
oldVersion                 = '3.0b3'
oldAppVersion              = oldVersion
oldBuildNumber             = 1
oldBaseTag                 = 'THUNDERBIRD_3_0b3'
releasePlatforms           = ('linux', 'win32', 'macosx')
patcherConfig              = 'moz191-thunderbird-branch-patcher2.cfg'
patcherToolsTag            = 'UPDATE_PACKAGING_R9'
ftpServer                  = 'ftp.mozilla.org'
stagingServer              = 'stage-old.mozilla.org'
bouncerServer              = 'download.mozilla.org'
ausServerUrl               = 'https://aus2.mozillamessaging.com'
useBetaChannel             = 0
verifyConfigs              = {'linux':  'moz191-thunderbird-linux.cfg',
                              'macosx': 'moz191-thunderbird-mac.cfg',
                              'win32':  'moz191-thunderbird-win32.cfg'}
