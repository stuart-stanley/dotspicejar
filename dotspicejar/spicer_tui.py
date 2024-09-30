"""
things...
CNC/grbl widget:
- active
  - connects to device
  - jog
- passive
  - shows status
   - position
   - alarm
- authority
  - speed settings?
- api
  - home
  -

"""

from textual.app import App, ComposeResult
from textual.widgets import Static


class Hamster(Static):
