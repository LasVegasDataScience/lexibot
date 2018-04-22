#!/usr/bin/env python

from lvds.slack.message import SlackMsg

import os

ROBOT = 'slackinator'
#CHANNEL = '#playground'
#CHANNEL = '#random'
CHANNEL = '@Steve'

msg = """
I have so many things to say, it's hard to know where to start.

First I have this bit of code:
```
from lvds.slack.message import SlackMsg
```

It's :sunglasses: and all but I want make it do something great.

like add a url: https://www.lasvegasdatascience.com/

Can you help me?
"""

slack = SlackMsg(ROBOT, CHANNEL)

# this is not required if we are running from CRON or some other
#  non-interactive source
slack.ignore_interactive = True

slack.msg(msg)
