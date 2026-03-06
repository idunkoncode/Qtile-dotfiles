#       █████████     ███████    ███████████ █████ █████ ███████████ █████ █████       ██████████
#      ███░░░░░███  ███░░░░░███ ░█░░░░░░███ ░░███ ░░███ ░█░░░███░░░█░░███ ░░███       ░░███░░░░░█
#     ███     ░░░  ███     ░░███░     ███░   ░░███ ███  ░   ░███  ░  ░███  ░███        ░███  █ ░
#    ░███         ░███      ░███     ███      ░░█████       ░███     ░███  ░███        ░██████
#    ░███         ░███      ░███    ███        ░░███        ░███     ░███  ░███        ░███░░█
#    ░░███     ███░░███     ███   ████     █    ░███        ░███     ░███  ░███      █ ░███ ░   █
#     ░░█████████  ░░░███████░   ███████████    █████       █████    █████ ███████████ ██████████
#      ░░░░░░░░░     ░░░░░░░    ░░░░░░░░░░░    ░░░░░       ░░░░░    ░░░░░ ░░░░░░░░░░░ ░░░░░░░░░░
#
#                                                                                    - DARKKAL44


from time import sleep

from libqtile import bar, hook, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen
from libqtile.dgroups import simple_key_binder
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import glob as _glob
HAS_BATTERY = bool(_glob.glob("/sys/class/power_supply/BAT*"))

mod = "mod4"
terminal = "ghostty"
browser = "firefox"
filemanager = "thunar"
menu = "rofi -show drun -l 12"

# █▄▀ █▀▀ █▄█ █▄▄ █ █▄░█ █▀▄ █▀
# █░█ ██▄ ░█░ █▄█ █ █░▀█y █▄▀ ▄█


keys = [
    #  D E F A U L T
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key(
        [mod, "control"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "control"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "control"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "shift"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "shift"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "shift"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "shift"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod], "e", lazy.window.toggle_fullscreen()),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod], "p", lazy.spawn("sh -c ~/.config/rofi/scripts/power"), desc="powermenu"),
    Key(
        [mod],
        "t",
        lazy.spawn("sh -c ~/.config/rofi/scripts/theme_switcher"),
        desc="theme_switcher",
    ),
    # C U S T O M
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pamixer -i 5"),
        desc="Volume Up",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pamixer -d 5"),
        desc="volume down",
    ),
    Key(
        [], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute"), desc="Volume Mute"
    ),
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="playerctl"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="playerctl"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="playerctl"),
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl s 10%+"),
        desc="brightness UP",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl s 10%-"),
        desc="brightness Down",
    ),
    Key([mod], "f", lazy.spawn(filemanager), desc="file manager"),
    Key([mod], "d", lazy.spawn(menu), desc="Launch rofi"),
    Key([mod], "s", lazy.spawn("flameshot gui"), desc="Screenshot"),
    Key([mod], "a", lazy.spawn("plasma-discover"), desc="KDE Discover"),
]


# █▀▀ █▀█ █▀█ █░█ █▀█ █▀
# █▄█ █▀▄ █▄█ █▄█ █▀▀ ▄█


groups = [Group(f"{i + 1}", label="") for i in range(8)]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )


# L A Y O U T S


lay_config = {
    "border_width": 0,
    "margin": 9,
    "border_focus": "3c3836",
    "border_normal": "3c3836",
    "font": "FiraCode Nerd Font",
    "grow_amount": 2,
}

layouts = [
    # layout.MonadWide(**lay_config),
    layout.Bsp(**lay_config, fair=False, border_on_single=True),
    layout.Columns(
        **lay_config,
        border_on_single=True,
        num_columns=2,
        split=False,
    ),
    # Plasma(lay_config, border_normal_fixed='#3b4252', border_focus_fixed='#3b4252', border_width_single=3),
    # layout.RatioTile(**lay_config),
    # layout.VerticalTile(**lay_config),
    # layout.Matrix(**lay_config, columns=3),
    # layout.Zoomy(**lay_config),
    # layout.Slice(**lay_config, width=1920, fallback=layout.TreeTab(), match=Match(wm_class="joplin"), side="right"),
    # layout.MonadTall(**lay_config),
    # layout.Tile(shift_windows=True, **lay_config),
    # layout.Stack(num_stacks=2, **lay_config),
    layout.Floating(**lay_config),
    layout.Max(**lay_config),
]


widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()


def search():
    qtile.spawn("rofi -show drun")


def power():
    qtile.spawn("sh -c ~/.config/rofi/scripts/power")


# █▄▄ ▄▀█ █▀█
# █▄█ █▀█ █▀▄


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Spacer(
                    length=15,
                    background="#282828",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/launch_Icon.png",
                    margin=2,
                    background="#282828",
                    mouse_callbacks={"Button1": power},
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/6.png",
                ),
                widget.GroupBox(
                    font="JetBrainsMono Nerd Font",
                    fontsize=24,
                    borderwidth=3,
                    highlight_method="block",
                    active="#ebdbb2",
                    block_highlight_text_color="#83a598",
                    highlight_color="#3c3836",
                    inactive="#282828",
                    foreground="#665c54",
                    background="#3c3836",
                    this_current_screen_border="#3c3836",
                    this_screen_border="#3c3836",
                    other_current_screen_border="#3c3836",
                    other_screen_border="#3c3836",
                    urgent_border="#3c3836",
                    rounded=True,
                    disable_drag=True,
                ),
                widget.Spacer(
                    length=8,
                    background="#3c3836",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/1.png",
                ),
                widget.CurrentLayout(
                    mode="icon",
                    custom_icon_paths=["~/.config/qtile/Assets/layout"],
                    background="#3c3836",
                    scale=0.50,
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/5.png",
                ),
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free Solid",
                    fontsize=13,
                    background="#282828",
                    foreground="#ebdbb2",
                    mouse_callbacks={"Button1": search},
                ),
                widget.TextBox(
                    fmt="Search",
                    background="#282828",
                    font="JetBrainsMono Nerd Font Bold",
                    fontsize=13,
                    foreground="#ebdbb2",
                    mouse_callbacks={"Button1": search},
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/4.png",
                ),
                widget.WindowName(
                    background="#3c3836",
                    font="JetBrainsMono Nerd Font Bold",
                    fontsize=13,
                    empty_group_string="Desktop",
                    max_chars=130,
                    foreground="#ebdbb2",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/3.png",
                ),
                widget.StatusNotifier(
                    background="#282828",
                    padding=4,
                ),
                widget.TextBox(
                    text=" ",
                    background="#282828",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/6.png",
                    background="#3c3836",
                ),
                widget.TextBox(
                    text="",
                    font="Font Awesome 6 Free Solid",
                    fontsize=13,
                    background="#3c3836",
                    foreground="#ebdbb2",
                ),
                widget.Memory(
                    background="#3c3836",
                    format="{MemUsed: .0f}{mm}",
                    foreground="#ebdbb2",
                    font="JetBrainsMono Nerd Font Bold",
                    fontsize=13,
                    update_interval=5,
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/2.png",
                ),
                widget.Spacer(
                    length=8,
                    background="#3c3836",
                ),
                *([
                    widget.TextBox(
                        text=" ",
                        font="Font Awesome 6 Free Solid",
                        fontsize=13,
                        background="#3c3836",
                        foreground="#ebdbb2",
                    ),
                    widget.Battery(
                        font="JetBrainsMono Nerd Font Bold",
                        fontsize=13,
                        background="#3c3836",
                        foreground="#ebdbb2",
                        format="{percent:2.0%}",
                    ),
                    widget.Image(
                        filename="~/.config/qtile/Assets/2.png",
                    ),
                    widget.Spacer(
                        length=8,
                        background="#3c3836",
                    ),
                ] if HAS_BATTERY else []),
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free Solid",
                    fontsize=13,
                    background="#3c3836",
                    foreground="#ebdbb2",
                ),
                widget.Volume(
                    font="JetBrainsMono Nerd Font Bold",
                    fontsize=13,
                    background="#3c3836",
                    foreground="#ebdbb2",
                    mute_command="pamixer --toggle-mute",
                    volume_up_command="pamixer -i 5",
                    volume_down_command="pamixer -d 5",
                    get_volume_command="pamixer --get-volume-human",
                    update_interval=0.2,
                    unmute_format="{volume}%",
                    mute_format="M",
                ),
                widget.Image(
                    filename="~/.config/qtile/Assets/5.png",
                    background="#3c3836",
                ),
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free Solid",
                    fontsize=13,
                    background="#282828",
                    foreground="#ebdbb2",
                ),
                widget.Clock(
                    format="%I:%M %p",
                    background="#282828",
                    foreground="#ebdbb2",
                    font="JetBrainsMono Nerd Font Bold",
                    fontsize=13,
                ),
                widget.Spacer(
                    length=18,
                    background="#282828",
                ),
            ],
            30,
            border_color="#282828",
            border_width=[0, 0, 0, 0],
            margin=[15, 60, 6, 60],
        ),
    ),
]


# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus="#1d2021",
    border_normal="#1d2021",
    border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
)


import os
import subprocess


# stuff
@hook.subscribe.startup_once
def autostart():
    subprocess.call([os.path.expanduser("~/.config/qtile/autostart_once.sh")])


auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


# E O F
