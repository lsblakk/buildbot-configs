hgUsername          = 'stage-ffxbld'
hgSshKey            = '~cltbld/.ssh/ffxbld_dsa'
mobileBranchNick    = 'mobile-1.9.2'
mozSourceRepoName      = 'mozilla-1.9.2'
# This parameter (and its l10n equivalent) is for staging only and necessary
# because the repo_setup builder needs to know where to clone repositories from.
# It is not used for anything else.
mozSourceRepoClonePath = 'releases/mozilla-1.9.2'
mozSourceRepoPath      = 'users/stage-ffxbld/mozilla-1.9.2'
mozSourceRepoRevision  = 'FILLMEIN'
mobileSourceRepoName      = 'mobile-1.1'
mobileSourceRepoClonePath = 'releases/mobile-1.1'
mobileSourceRepoPath      = 'users/stage-ffxbld/mobile-1.1'
mobileSourceRepoRevision  = 'FILLMEIN'
mozRelbranchOverride   = ''
l10nRelbranchOverride   = ''
mobileRelbranchOverride   = ''
l10nRepoClonePath   = 'releases/l10n-mozilla-1.9.2'
l10nRepoPath        = 'users/stage-ffxbld'
l10nRevisionFile    = 'l10n-changesets_mobile-1.1.json'
productName         = 'fennec'
appName             = 'mobile'
mergeLocales        = True
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version             = '1.1b1'
appVersion          = '1.1'
milestone           = '1.9.2.3'
buildNumber         = 1
baseTag             = 'FENNEC_1_1b1'
enUSPlatforms       = ('maemo4',)
l10nPlatforms       = enUSPlatforms
enUSDesktopPlatforms = ('linux-i686', 'macosx-i686', 'win32-i686')
l10nDesktopPlatforms = ()
talosTestPlatforms  = ()
ftpServer           = 'staging-stage.build.mozilla.org'
stagingServer       = 'staging-stage.build.mozilla.org'
stageBasePath       = '/home/ftp/pub/mobile/candidates'
base_enUS_binaryURL = 'http://%s/pub/mozilla.org/mobile/candidates/%s-candidates/build%d' % (ftpServer, version, buildNumber)
doPartnerRepacks    = True
partnersRepoPath    = 'build/partner-repacks'
partnerRepackPlatforms = ('maemo4',)
