import vfs
import time
while True:
    try:
        VFS = vfs.vfs()
        VFS.login()
        VFS.close()
    except:
        pass
    # time.sleep(120)
