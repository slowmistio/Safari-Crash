#!/usr/bin/python2.7
import argparse
from terminaltables import SingleTable
import os
import lib.logs as logs
import importlib
from bottle import route, run

PATH = __file__.replace('./safari_crash.py', '')
sun = "{}{}o{}{}{}O{}".format(logs.color().BLINK, logs.color().RED, logs.color().END, logs.color().BLINK, logs.color().YELLOW, logs.color().END)

print "\n{} Safari Crash Exploit Kit".format(logs.red("(*)"))
print "{} Created by: TheSecondSun {} (thescndsun@gmail.com)".format(logs.red("(*)"), sun)
print "\n"

def list_exploits():
    header = logs.green(logs.bold('***'))
    print '\n'
    print  header + 'AVAILABLE EXPLOITS' + header
    exploits = os.listdir(PATH+'exploits')
    table_data = [['--NAME--', '--DESCRIPTION--']]
    for e in exploits:
        if ('init' not in e and '.pyc' not in e):
            name = e.replace('.py', '')
            imported_exploit = importlib.import_module('exploits.'+name)
            description = imported_exploit.description
            table_data.append([name, imported_exploit.description])
    table_instance = SingleTable(table_data) 
    table_instance.inner_heading_row_border = True
    table_instance.inner_row_border = True
    table_instance.justify_columns = {0: 'left', 1: 'left', 2: 'left'}
    print table_instance.table

def arguments():
    parser = argparse.ArgumentParser(prog='safari_crash')
    parser.add_argument('EXPLOIT_NAME', nargs='?',help='Name of the exploit to use (use "-l" flag to list exploits)')
    parser.add_argument('-l', '--list', action='store_true',
            dest='LIST',
            help='List available exploits')
    parser.add_argument('-p', '--port', action='store',
            default=8080,
            dest='PORT',
            help='Port to serve the exploit on (default: 8080)')
    parser.add_argument('-hst', '--hostname', action='store',
            default='localhost',
            dest='HOSTNAME',
            help='Local hostname (default: localhost)')
    parser.add_argument('-u', '--url', action='store',
            default='/index',
            dest='URL',
            help='Sub-url to serve exploit on (default: /index)')
    parser.add_argument('-d', '--debug', action='store_true',
            dest='DEBUG',
            help='Start Bottle server in a debug mode')

    res = parser.parse_args()
    if res.LIST:
        list_exploits()
    elif not res.EXPLOIT_NAME:
        parser.error('"EXPLOIT_NAME" option is required')
    return res

def main():
    res = arguments()
    try:
        exploit_code = importlib.import_module('exploits.'+res.EXPLOIT_NAME).code
        @route('{}'.format(res.URL))
        def exploit():
            return exploit_code
        logs.good('Started serving {} on {}:{}{} ...'.format(logs.bold(logs.purple(res.EXPLOIT_NAME)), 
                        res.HOSTNAME, res.PORT, res.URL))
        print '\n'
        run(host=res.HOSTNAME, port=res.PORT, debug=res.DEBUG)
    except TypeError:
        pass
    except ImportError:
        logs.err('No such exploit')

if __name__ == '__main__':
    main()