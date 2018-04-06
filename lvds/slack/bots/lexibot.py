#!/usr/bin/env python

from lvds.slack.listen import SlackListen

import datetime, os, requests, sys, time


class SlackLexiBot(SlackListen):

    def __init__(self, username='lexibot'):

        if username is None:
            raise AttributeError("which username should we use with Slack?")

        SlackListen.__init__(self, username)


    def response(self, command=None, output=None):

        return (":astonished: Wait! What?! I'm Alive!!!\n\n"
                "Here's my thinking face. :zany_face: are you impressed?")


if __name__ == "__main__":

    print("starting...")
    SlackLexiBot()
