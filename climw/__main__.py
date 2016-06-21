#!/usr/bin/env python

import sys
import configargparse

def main(args=None):
  if( args is None ):
    args = sys.argv[1:]

  config_instance = configargparse.ArgumentParser(prog='mw',
      description='Look up definitions and synonyms from the Merriam-Webster sources on Dictionary.com',
      default_config_files=['/etc/dictionary.conf', '~/.dictionary.conf'])
  config_instance.add('-c', '--config', required=True, is_config_file=True, help='Configuration file path')
  config_instance.add('--thesaurus-key', help='API key to the Collegiate Thesaurus on dictionaryapi.com')
  config_instance.add('--dictionary-key', help='API key to the Collegiate Dictionary on dictionaryapi.com')
  config_instance.add('action', nargs=1, required=True, help='<define|synonym> the word')
  config_instance.add('word', nargs=1, required=True, help='the word to lookup')

  options = config_instance.parse_args(args)

  if( options['action'] == 'define' ):
    print(DictionaryRequest(options['dictionary-key']).define(options['word']))
  elif( options['action'] == 'synonym' ):
    print('Filler')
  else:
    raise Exception('Invalid action option')

if __name__ == '__main__':
  main()
