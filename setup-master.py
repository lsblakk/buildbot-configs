#!/usr/bin/env python
"""setup-master.py master_dir master [master_num]

Sets up mozilla buildbot master in master_dir.  Some masters require an
additional number since they have been split up, e.g. mozilla2"""

import os, glob, shutil, subprocess

class MasterConfig:
    def __init__(self, name=None, globs=None, renames=None, local_links=None):
        self.name = name or None
        self.globs = globs or []
        self.renames = renames or []
        self.local_links = local_links or []

    def __add__(self, o):
        retval = MasterConfig(
                name = self.name or o.name,
                globs = self.globs + o.globs,
                renames = self.renames + o.renames,
                local_links = self.local_links + o.local_links,
                )
        return retval

    def createMaster(self, master_dir):
        null = open(os.devnull, "w")
        subprocess.check_call(['buildbot', 'create-master', master_dir], stdout=null)
        if not os.path.exists(master_dir):
            os.makedirs(master_dir)
        for g in self.globs:
            for f in glob.glob(os.path.join(self.name, g)):
                dst = os.path.join(master_dir, os.path.basename(f))
                if os.path.lexists(dst):
                    os.unlink(dst)
                src = os.path.join("..", f)
                os.symlink(src, dst)

        for src, dst in self.local_links:
            dst = os.path.join(master_dir, dst)
            if os.path.lexists(dst):
                os.unlink(dst)
            os.symlink(src, dst)

        for src, dst in self.renames:
            dst = os.path.join(master_dir, dst)
            if os.path.lexists(dst):
                os.unlink(dst)
            shutil.copy(os.path.join(self.name, src), dst)

mozilla2_staging = MasterConfig(
        'mozilla2-staging',
        globs=['*.py', '*.cfg', '*.ini', 'l10n-changesets*'],
        renames=[
            ('BuildSlaves.py.template', 'BuildSlaves.py'),
            ],
        local_links=[
            ('release-fennec-mozilla-1.9.2.py', 'release_mobile_config.py'),
            ],
        )

mozilla2_staging1 = mozilla2_staging + MasterConfig(
        local_links=[
            ('master1.cfg', 'master.cfg'),
            ('release_config1.py', 'release_config.py'),
            ],
        )

mozilla2_staging2 = mozilla2_staging + MasterConfig(
        local_links=[
            ('master2.cfg', 'master.cfg'),
            ('release_config2.py', 'release_config.py'),
            ],
        )

mozilla2 = MasterConfig(
        'mozilla2',
        globs=['*.py', '*.cfg', '*.ini', 'l10n-changesets*'],
        renames=[
            ('BuildSlaves.py.template', 'BuildSlaves.py'),
            ],
        local_links=[
            ('release-fennec-mozilla-1.9.2.py', 'release_mobile_config.py'),
            ],
        )

mozilla2_1 = mozilla2 + MasterConfig(
        local_links=[
            ('master1.cfg', 'master.cfg'),
            ('release_config1.py', 'release_config.py'),
            ],
        )

mozilla2_2 = mozilla2 + MasterConfig(
        local_links=[
            ('master2.cfg', 'master.cfg'),
            ('release_config2.py', 'release_config.py'),
            ],
        )

talos_staging = MasterConfig(
        'talos-staging-pool',
        globs=['*.py', '*.cfg'],
        )

talos_staging_try = MasterConfig(
        'talos-staging-try',
        globs=['*.py', '*.cfg'],
        )

talos = MasterConfig(
        'talos-pool',
        globs=['*.py', '*.cfg'],
        )

talos_try = MasterConfig(
        'talos-try',
        globs=['*.py', '*.cfg'],
        )

masters = {
        'mozilla2-staging': [mozilla2_staging1, mozilla2_staging2],
        'mozilla2': [mozilla2_1, mozilla2_2],
        'talos-staging': [talos_staging],
        'talos-staging-try': [talos_staging_try],
        'talos': [talos],
        'talos-try': [talos_try],
        }

if __name__ == "__main__":
    from optparse import OptionParser

    parser = OptionParser(__doc__)
    parser.set_defaults(action=None)
    parser.add_option("-l", "--list", action="store_const", dest="action", const="list")

    options, args = parser.parse_args()

    if options.action == "list":
        for master_name, master_list in sorted(masters.items()):
            n = len(master_list)
            if n == 1:
                print master_name
            else:
                for i in range(1,n+1):
                    print master_name, i
        parser.exit()

    if len(args) < 2:
        parser.error("You need at least 2 arguments")

    master_dir, master_name = args[:2]

    if master_name not in masters:
        parser.error("Unknown master %s" % master_name)

    n = len(masters[master_name])
    if n == 1:
        if len(args) > 2:
            parser.error("Master %s doesn't require a number" % master_name)
        m = masters[master_name][0]
    else:
        if len(args) == 2:
            parser.error("Master %s requires a number" % master_name)
        try:
            master_num = int(args[2])
        except ValueError:
            parser.error("master_num must be an integer")

        if not 1 <= master_num <= n:
            parser.error("master_num must be between 1 and %s" % n)
        # master_num-1 because we accept 1-based numbers, and the array is 0-based
        m = masters[master_name][master_num-1]

    m.createMaster(master_dir)