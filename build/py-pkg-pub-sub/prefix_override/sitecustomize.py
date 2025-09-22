import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/jibrilinux/ros2_ws/install/py-pkg-pub-sub'
