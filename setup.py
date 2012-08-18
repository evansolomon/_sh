import os
import sys

# Welcome
print "Welcome to _sh.\n"

# Get the target location
target = raw_input('Where do you want to symlink _sh? ')
print "\n"

# No blank targets
if not target:
    print 'You have to pick a target.'
    sys.exit()

# Make sure it exists
target_dir = os.path.expanduser(target)
if not os.path.exists(target_dir):
    print target + ' is not a directory.'
    sys.exit()

# Make sure _sh is executable
os.system('chmod u+x ' + os.path.realpath('_sh'))

# Symlink it
command = 'ln -s ' + os.path.realpath('_sh') + ' ' + target_dir
print "\nRunning...\n\n" + command
result = os.system(command)
