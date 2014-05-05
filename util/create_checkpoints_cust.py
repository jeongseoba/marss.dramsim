#! /usr/bin/python
import os
import subprocess
import sys
import time
from time import localtime, strftime

# Set up default variables
cwd = os.getcwd()
qemu_bin = '%s/qemu/qemu-system-x86_64' % cwd
qemu_img = '/home/jeongseob/marss.pseudo_proc.modified/disks/linux_tslice.qcow2'
vm_memory = 4096
qemu_cmd = ''

def add_to_cmd(opt):
    global qemu_cmd
    qemu_cmd = "%s %s" % (qemu_cmd, opt)

# Generate a common command string
add_to_cmd(qemu_bin)
add_to_cmd('-m %d' % vm_memory)
add_to_cmd('-serial pty')
add_to_cmd('-vnc :20')
#add_to_cmd('-cpu core2duo')

# Add Image at the end
# add_to_cmd('-hda %s' % qemu_img)
add_to_cmd('-drive file=%s,cache=unsafe' % qemu_img)

# Checkpoint list
check_list = []

# SPEC 2006 Benchmarks
# Directory structure :
# $HOME/spec2006/[compile_config]/[bench_name]/[executables]

spec_list = [

#		 {'name' : 'mcf-milc-30ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 30 1 2 mcf milc
#		 '''
#         },
#
#		 {'name' : 'mcf-milc-1ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 1 1 2 mcf milc
#		 '''
#         },
#
#		 {'name' : 'namd-milc-30ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 30 1 2 namd milc
#		 '''
#         },
#
#		 {'name' : 'namd-milc-1ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 1 1 2 namd milc
#		 '''
#         },
#
#		 {'name' : 'bzip2-milc-30ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 30 1 2 bzip2 milc
#		 '''
#         },
#
#		 {'name' : 'bzip2-milc-1ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 1 1 2 bzip2 milc
#		 '''
#         },
#
#		 {'name' : 'soplex-milc-30ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 30 1 2 soplex milc
#		 '''
#         },
#
#		 {'name' : 'soplex-milc-1ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 1 1 2 soplex milc
#		 '''
#         },
#
#		 {'name' : 'xalancbmk-milc-30ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 30 1 2 xalancbmk milc
#		 '''
#         },
#
#		 {'name' : 'xalancbmk-milc-1ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 1 1 2 xalancbmk milc
#		 '''
#         },

####################################################################
#		 {'name' : 'mcf-libquantum-30ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 30 1 2 mcf libquantum
#		 '''
#         },
#
#		 {'name' : 'mcf-libquantum-1ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 1 1 2 mcf libquantum
#		 '''
#         },
#
#		 {'name' : 'namd-libquantum-30ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 30 1 2 namd libquantum
#		 '''
#         },
#
#		 {'name' : 'namd-libquantum-1ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 1 1 2 namd libquantum
#		 '''
#         },
#
#		 {'name' : 'bzip2-libquantum-30ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 30 1 2 bzip2 libquantum
#		 '''
#         },
#
#		 {'name' : 'bzip2-libquantum-1ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 1 1 2 bzip2 libquantum
#		 '''
#         },
#
#		 {'name' : 'soplex-libquantum-30ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 30 1 2 soplex libquantum
#		 '''
#         },
#
#		 {'name' : 'soplex-libquantum-1ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 1 1 2 soplex libquantum
#		 '''
#         },
#
#		 {'name' : 'xalancbmk-libquantum-30ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 30 1 2 xalancbmk libquantum
#		 '''
#         },
#
#		 {'name' : 'xalancbmk-libquantum-1ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 1 1 2 xalancbmk libquantum
#		 '''
#         },
#
		 {'name' : 'astar-libquantum-30ms', 
         'command' :
         '''~/run_spec_on_marss_tslice.py 30 1 2 astar libquantum
		 '''
         },

		 {'name' : 'astar-libquantum-1ms', 
         'command' :
         '''~/run_spec_on_marss_tslice.py 1 1 2 astar libquantum
		 '''
         },

		 {'name' : 'milc-libquantum-30ms', 
         'command' :
         '''~/run_spec_on_marss_tslice.py 30 1 2 milc libquantum
		 '''
         },

		 {'name' : 'milc-libquantum-1ms', 
         'command' :
         '''~/run_spec_on_marss_tslice.py 1 1 2 milc libquantum
		 '''
         },

		 {'name' : 'lbm-libquantum-30ms', 
         'command' :
         '''~/run_spec_on_marss_tslice.py 30 1 2 lbm libquantum
		 '''
         },

		 {'name' : 'lbm-libquantum-1ms', 
         'command' :
         '''~/run_spec_on_marss_tslice.py 1 1 2 lbm libquantum
		 '''
         },

		 {'name' : 'gcc-libquantum-30ms', 
         'command' :
         '''~/run_spec_on_marss_tslice.py 30 1 2 gcc libquantum
		 '''
         },

		 {'name' : 'gcc-libquantum-1ms', 
         'command' :
         '''~/run_spec_on_marss_tslice.py 1 1 2 gcc libquantum
		 '''
         },
#
#		 ##########################################################		 
#
#		 {'name' : 'mcf-namd-30ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 30 1 2 mcf namd
#		 '''
#         },
#
#		 {'name' : 'mcf-namd-1ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 1 1 2 mcf namd
#		 '''
#         },
#
#		 {'name' : 'bzip2-namd-30ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 30 1 2 bzip2 namd
#		 '''
#         },
#
#		 {'name' : 'bzip2-namd-1ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 1 1 2 bzip2 namd
#		 '''
#         },
#
#		 {'name' : 'soplex-namd-30ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 30 1 2 soplex namd
#		 '''
#         },
#
#		 {'name' : 'soplex-namd-1ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 1 1 2 soplex namd
#		 '''
#         },
#
#		 {'name' : 'xalancbmk-namd-30ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 30 1 2 xalancbmk namd
#		 '''
#         },
#
#		 {'name' : 'xalancbmk-namd-1ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 1 1 2 xalancbmk namd
#		 '''
#         },
#
#		 {'name' : 'astar-namd-30ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 30 1 2 astar namd
#		 '''
#         },
#
#		 {'name' : 'astar-namd-1ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 1 1 2 astar namd
#		 '''
#         },
#
#		 {'name' : 'milc-namd-30ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 30 1 2 milc namd
#		 '''
#         },
#
#		 {'name' : 'milc-namd-1ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 1 1 2 milc namd
#		 '''
#         },
#
#		 {'name' : 'lbm-namd-30ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 30 1 2 lbm namd
#		 '''
#         },
#
#		 {'name' : 'lbm-namd-1ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 1 1 2 lbm namd
#		 '''
#         },
#
#		 {'name' : 'gcc-namd-30ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 30 1 2 gcc namd
#		 '''
#         },
#
#		 {'name' : 'gcc-namd-1ms', 
#         'command' :
#         '''~/run_spec_on_marss_tslice.py 1 1 2 gcc namd
#		 '''
#         },

        ]

# To create all spec checkpoints
check_list = spec_list

print("Execution command: %s" % qemu_cmd)
print("Number of Chekcpoints to create: %d" % len(check_list))

login_cmds = ["root\n", "calab4406\n"]

def pty_to_stdout(fd, untill_chr):
    chr = '1'
    while chr != untill_chr:
        try:
		    chr = os.read(fd, 1)
        except OSError:
            chr = untill_chr
            #print "OSError"	
        else:
     	    sys.stdout.write(chr)
    sys.stdout.flush()

def pty_login(fd):
    os.write(fd, login_cmds[0])
    pty_to_stdout(fd, ':')
    os.write(fd, login_cmds[1])

# Start simulation from checkpoints
pty_prefix = 'char device redirected to '
for checkpoint in check_list:

    print("Starting QEMU for checkpoint: %s" % checkpoint['name'])

    p = subprocess.Popen(qemu_cmd.split(), stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, bufsize=0)

    pty_term = None

    while p.poll() is None:
        line = p.stdout.readline()
        sys.stdout.write(line)
        if line.startswith(pty_prefix):
            dev_name = line[len(pty_prefix):].strip()

            # Open the device terminal and send simulation command
            pty_term = os.open(dev_name, os.O_RDWR)

            break

    if pty_term == None:
        print("ERROR: While connecting with pty terminal")
        continue

    pty_to_stdout(pty_term, ':')

    # Now send the login commands to the termianl and wait
    # untill some response text
    pty_login(pty_term)

    pty_to_stdout(pty_term, '#')

    # At this point we assume that we have successfully logged in
    # Now give the command to create checkpoint
    os.write(pty_term, checkpoint['command'])

    pty_to_stdout(pty_term, '#')
#
#    sys.stdout.write('\n')
#    for line in p.stdout:
#        sys.stdout.write(line)

    # Wait for simulation to complete
    p.wait()
