#!/usr/bin/env python

from lvds.slack.bots.lexibot import SlackLexiBot

import sys

if __name__ == "__main__":

    print("press <crtl>-c to stop the bot\n"
          "run this in the background to keep your bot alive.\n"
          "{} &".format(sys.argv[0]))
    
    try:
        SlackLexiBot()
    except:
        sys.exit()
