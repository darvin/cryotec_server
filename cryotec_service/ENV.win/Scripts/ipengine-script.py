#!E:\workspace\cryotec_service\cryotec_service\ENV.win\Scripts\python27.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'ipython==0.10','console_scripts','ipengine'
__requires__ = 'ipython==0.10'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('ipython==0.10', 'console_scripts', 'ipengine')()
    )
