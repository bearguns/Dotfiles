# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import json
from pathlib import Path
from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook
from typing import List  # noqa: F401

mod = "mod4"
my_terminal = "alacritty"
my_nord_theme = {
    'nord0': '#2E3440',
    'nord1': '#3B4252',
    'nord2': '#434C5E',
    'nord3': '#4C566A',
    'nord4': '#D8DEE9',
    'nord5': '#E5E9F0',
    'nord6': '#ECEFF4',
    'nord7': '#8FBCBB',
    'nord8': '#88C0D0',
    'nord9': '#81A1C1',
    'nord10': '#5E81AC',
    'nord11': '#BF616A',
    'nord12': '#D08770',
    'nord13': '#EBCB8B',
    'nord14': '#A3BE8C',
    'nord15': '#B48EAD'
}
my_background = my_nord_theme['nord0']
my_foreground = my_nord_theme['nord4']

keys = [
    ### Essentials
    Key([mod], "Return", lazy.spawn(my_terminal), desc='Launches my terminal emulator'),
    Key([mod], "q", lazy.window.kill(), desc='Kills window with focus'),
    Key([mod, "control"], "r", lazy.restart(), desc='Restarts QTile and reloads config'),
    Key([mod, "control"], "q", lazy.shutdown(), desc='Quit QTile'),
    Key([mod], "space", lazy.spawn("rofi -show run"), desc='Start rofi application launcher'),
    Key(["mod1"], "Tab", lazy.spawn("rofi -show window"), desc='Start rofi window switcher'),
    Key([mod], "r", lazy.spawn("alacritty -e ranger"), desc='Start ranger file manager'),
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_up()),
    Key([mod, "control"], "j", lazy.layout.shuffle_down()),
    Key([mod, "control"], "h", lazy.layout.shuffle_left()),
    # Switch window focus to other pane(s) of stack
    #Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split()),


    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout()),
   
    #Key([mod], "r", lazy.spawncmd()),
]

my_groups = [
    ("WEB", {'layout': 'monadtall'}),
    ("STEAM", {'layout': 'max'}),
    ("DEV", {'layout': 'bsp'}),
    ("CHAT", {'layout': 'matrix'}),
    ("SCRATCH", {'layout': 'tile'})
]

groups = [Group(name, **kwargs) for name, kwargs in my_groups]

for i, (name, kwargs) in enumerate(my_groups, 1):
    keys.extend([
        Key([mod], str(i), lazy.group[name].toscreen()),
        Key([mod, "shift"], str(i), lazy.window.togroup(name, switch_group=True)),
    ])

groups = [
    Group("WEB"),
    Group("STEAM", matches=[Match(wm_class=["Steam"])]),
    Group("DEV"),
    Group("CHAT", matches=[Match(wm_class=["Discord"])]),
    Group("SCRATCH")
]

my_margin = 8
my_border_width = 5
my_border_normal = my_nord_theme['nord5']
my_border_focus = my_nord_theme['nord8']

layouts = [
    layout.MonadTall(
        margin=my_margin,
        border_width=my_border_width,
        border_focus=my_border_focus,
        border_normal=my_border_normal,
        align=0
    ),
    layout.Bsp(
        margin=my_margin,
        border_width=my_border_width,
        border_normal=my_border_normal,
        border_focus=my_border_focus
    ),
    layout.Max(),
    layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.



    # layout.Columns(),
    layout.Matrix(
        margin=my_margin,
        border_focus=my_border_focus,
        border_normal=my_border_normal,
        border_width=my_border_width
    ),
    layout.MonadWide(
        margin=my_margin,
        border_normal=my_border_normal,
        border_focus=my_border_focus,
        border_width=my_border_width
    ),
    # layout.RatioTile(),
    layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Overpass Mono',
    fontsize=12,
    padding=8,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(
                    foreground=my_nord_theme['nord4'],
                ),
                widget.GroupBox(
                    visible_groups=[group.name for group in groups],
                    active=my_nord_theme['nord14'],
                    inactive=my_nord_theme['nord3'],
                    block_highlight_text_color=my_nord_theme['nord1'],
                    rounded = False,
                    highlight_method="block",
                    this_current_screen_border=my_nord_theme['nord7'],
                ),
                widget.Spacer(
                    length=bar.STRETCH,
                ),
                widget.Systray(
                    margin=8
                ),
                widget.Spacer(
                    length=12,
                    padding=4
                ),
                widget.Pacman(
                    foreground=my_nord_theme['nord1'],
                    background=my_nord_theme['nord13'],
                    unavailable=my_foreground
                ),
                widget.Clock(
                    format='%Y-%m-%d %a %I:%M %p',
                    foreground=my_foreground,
                    background=my_nord_theme['nord1'],
                ),
                widget.QuickExit(
                    background=my_nord_theme['nord11'],
                    foreground=my_nord_theme['nord1'],
                ),
            ],
            28,
            background = my_nord_theme['nord1'],
            font="Ubuntu Condensed"
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.client_new
def _swallow(window):
    pid = window.window.get_net_wm_pid()
    ppid = psutil.Process(pid).ppid()
    cpids = {c.window.get_net_wm_pid(): wid for wid, c in window.qtile.windows_map.items()}
    for i in range(5):
        if not ppid:
            return
        if ppid in cpids:
            parent = window.qtile.windows_map.get(cpids[ppid])
            parent.minimized = True
            window.parent = parent
            return
        ppid = psutil.Process(ppid).ppid()

@hook.subscribe.client_killed
def _unswallow(window):
    if hasattr(window, 'parent'):
        window.parent.minimized = False

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
