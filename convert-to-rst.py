import os
import subprocess

mediawiki_dir = './mediawiki'
rst_dir = './rst'

for filename in os.listdir(mediawiki_dir):
    if filename.endswith('.mediawiki'):
        input_file = mediawiki_dir + os.sep + filename
        output_file = rst_dir + os.sep + filename.replace('.mediawiki', '.rst')
        print("Converting %s" % (filename))
        try:
            proc = subprocess.check_output(['pandoc', '-f', 'mediawiki', '-r', 'rst', '-o', output_file, input_file], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError:
            print("Error: ", filename, ' could not be converted')
        # break               # to try on single file
