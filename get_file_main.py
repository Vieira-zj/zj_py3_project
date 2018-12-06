'''
Created on 2018-12-6

@author: zhengjin
'''

import os
import sys
import urllib.request

KEY_URL = 'url'
KEY_SAVE_DIR_PATH = 'save_dir_path'
KEY_SAVE_FILE_NAME = 'save_file_name'


def get_file_by_url(input_dict):
    tmp_url = ''
    save_dir_path = ''
    try:
        tmp_url = input_dict[KEY_URL]
        save_dir_path = input_dict[KEY_SAVE_DIR_PATH]
    except KeyError as e:
        print('Error: input params save_dir_path or save_file_name is null!')
        raise

    file_name = ''
    save_file_name = input_dict.get(KEY_SAVE_FILE_NAME, '')
    if len(save_file_name) == 0:
        file_name = tmp_url[(tmp_url.rindex('/') + 1) : ]
    else:
        file_name = save_file_name
    urllib.request.urlretrieve(tmp_url, os.path.join(save_dir_path, file_name))


def cmd_args_parse():

    def usage():
        lines = []
        lines.append('Usage:')
        lines.append('  $ python get_file_main.py -u http://host/path -d d:\\local_path [-s new_file_name]')
        lines.append('Options:')
        lines.append('  -u: File download url.')
        lines.append('  -d: Local directory path to save download file.')
        lines.append('  -f: Local save file name. Default to file name in url.')
        lines.append('  -h: Help')
        print('\n'.join(lines))

    import getopt
    opts, _ = getopt.getopt(sys.argv[1:], 'hu:d:f:')
    
    ret_dict = {}
    if len(opts) == 0:
        usage()
        return ret_dict
    
    for op, value in opts:
        if op == '-u':
            ret_dict[KEY_URL] = value
        elif op == '-d':
            ret_dict[KEY_SAVE_DIR_PATH] = value
        elif op == '-f':
            ret_dict[KEY_SAVE_FILE_NAME] = value
        elif op == '-h':
            usage()
            exit(0)

    return ret_dict


if __name__ == '__main__':
    
    # run command:
    # python get_file_main.py -d "D:\JDTestLogs" -f "test.apk" 
    # -u http://10.182.44.8/job/b2b_master/lastSuccessfulBuild/artifact/JDB2B/app/build/outputs/apk/release/zgb-4.5.0-debug.apk
    tmp_dict = cmd_args_parse()
    get_file_by_url(tmp_dict)

    print('File download main DONE.')
