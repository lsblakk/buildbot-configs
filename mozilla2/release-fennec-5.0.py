hgUsername          = 'ffxbld'
hgSshKey            = '~cltbld/.ssh/ffxbld_dsa'
mobileBranchNick    = 'mozilla-mobile-5.0'
mozSourceRepoName      = 'mozilla-mobile-5.0'
# This parameter (and its l10n equivalent) is for staging only and necessary
# because the repo_setup builder needs to know where to clone repositories from.
# It is not used for anything else.
mozSourceRepoPath      = 'releases/mozilla-mobile-5.0'
mozSourceRepoRevision  = 'cca618b4594a'
mobileSourceRepoName      = 'mobile-5.0'
mobileSourceRepoPath      = 'releases/mobile-5.0'
mobileSourceRepoRevision  = '1ad394075948'
mozRelbranchOverride      = 'GECKO50b1_20110512_RELBRANCH'
l10nRelbranchOverride     = 'GECKO50b1_20110512_RELBRANCH'
mobileRelbranchOverride   = 'GECKO50b1_20110512_RELBRANCH'
mozconfigDir        = 'mozilla-beta'
l10nRepoPath        = 'releases/l10n/mozilla-aurora'
l10nRevisionFile    = 'l10n-changesets_mobile-5.0.json'
productName         = 'fennec'
appName             = 'mobile'
mergeLocales        = True
enableMultiLocale   = True
androidMozharnessConfig = "multi_locale/5.0_release_android.json"
# Sometimes we need the application version to be different from what we "call"
# the build, eg public release candidates for a major release (3.1 RC1).
# appVersion and oldAppVersion are optional definitions used in places that
# don't care about what we call it. Eg, when version bumping we will bump to
# appVersion, not version.
version             = '5.0b1'
appVersion          = version
milestone           = '5.0b1'
buildNumber         = 2
baseTag             = 'FENNEC_5_0b1'
oldVersion          = '4.0.1'
oldAppVersion       = oldVersion
oldBuildNumber      = 1
oldBaseTag          = 'FENNEC_4_0_1'
enUSPlatforms       = ('maemo5-gtk', 'android-r7')
l10nPlatforms       = ('maemo5-gtk',)
enUSDesktopPlatforms = ('linux-i686', 'macosx-i686', 'win32-i686')
l10nDesktopPlatforms = ()
talosTestPlatforms  = ()
ausBaseUploadDir    = '/opt/aus2/incoming/3/Fennec'
ftpServer           = 'ftp.mozilla.org'
stagingServer       = 'stage.mozilla.org'
stageBasePath       = '/home/ftp/pub/mobile/candidates'
base_enUS_binaryURL = 'http://%s/pub/mozilla.org/mobile/candidates/%s-candidates/build%d' % (ftpServer, version, buildNumber)
ausServerUrl        = 'http://aus2.mozilla.org'
ausUser             = 'cltbld'
ausSshKey           = 'cltbld_dsa'
doPartnerRepacks    = False
partnersRepoPath    = 'build/partner-repacks'
partnerRepackPlatforms = ('maemo5-gtk',)