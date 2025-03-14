#  ___  _   _ _                  A Qtile Config With Pywal
# / _ \| |_(_) | ___  Requires:  playerctl dunst scrot clipmenu xautolock 
#| | | | __| | |/ x \ pywal rofi dmenu lm-sensors urxvt firefox
#| | | | |_| | |  __/ i3lock htop notify-send khal pavucontol feh psutil
# \__\_\\__|_|_|\___| Backgrounds should go in ~/.local/share/backgrounds
# A Link to the acompanying scripts and start page is in the readme.
import os
import subprocess
import json
from typing import List
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, KeyChord, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# contants
city_weather_code = "3688689"

# Functions
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([home])
    
@hook.subscribe.startup
def autorestart():
    home = os.path.expanduser("~/.config/qtile/autorestart.sh")
    subprocess.call([home])
    
def htop():
    qtile.spawn("urxvtc -e htop")
    
def powermenu():
    qtile.spawn("powermenu")
    
def weather():
    qtile.spawn(f"xdg-open https://openweathermap.org/city/{city_weather_code}")

def sound():
    qtile.spawn("outputmenu")

def calendar():
    qtile.spawn("urxvtc -e khal interactive")

def launcher():
    qtile.spawn("rofi -show drun -show-icons -location 7 -yoffset -22")

def timer():
    qtile.spawn("timermenu")

def quake():
    qtile.spawn("qtile cmd-obj -o group scratchpad  -f  dropdown_toggle -a term")

def metamenu():
    qtile.spawn("metamenu")


#Pywal Colors
colors = os.path.expanduser("~/.cache/wal/colors.json")
colordict = json.load(open(colors))
ColorZ=(colordict["colors"]["color0"])
ColorA=(colordict["colors"]["color1"])
ColorB=(colordict["colors"]["color2"])
ColorC=(colordict["colors"]["color3"])
ColorD=(colordict["colors"]["color4"])
ColorE=(colordict["colors"]["color5"])
ColorF=(colordict["colors"]["color6"])
ColorG=(colordict["colors"]["color7"])
ColorH=(colordict["colors"]["color8"])
ColorI=(colordict["colors"]["color9"])

#Hotkeys
mod = "mod4"
terminal = guess_terminal()

keys = [
    #Navigation
    Key([mod], "j", lazy.layout.down(), desc="Mover Foco a Abajo"),
    Key([mod], "k", lazy.layout.up(), desc="Mover Foco a Arriba"),
    Key([mod], "h", lazy.layout.left(), desc="Mover Foco a la Izquierda"),
    Key([mod], "l", lazy.layout.right(), desc="Mover Foco a la Derecha"),
  
    #Movement
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Mover Ventana Abajo"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Mover Ventana Arriba"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Mover Ventana a la Izquierda"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Mover Ventana a la Derecha"),
    Key([mod, "mod1"], "j", lazy.layout.flip_down(), desc="Mover Ventana abajo de la caja"),
    Key([mod, "mod1"], "k", lazy.layout.flip_up(), desc="Mover Ventana arriba de la caja"),
    Key([mod, "mod1"], "h", lazy.layout.flip_left(), desc="Mover Ventana a la izquierda de la caja"),
    Key([mod, "mod1"], "l", lazy.layout.flip_right(), desc="Mover Ventana a la derecha de la caja"),
    Key([mod, "mod1"], "n", lazy.layout.normalize(), desc="Reiniciar Tamaño de las Ventanas"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Mover entre split y no split"),
    
    #Size
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Expandir Ventana actual Abajo"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Expandir Ventana actual Arriba"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Expandir Ventana actual a la Izquierda"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Expandir Ventana actual a la Derecha"),
    
    #Layout1
    Key([mod], "space", lazy.layout.next(), desc="Mover foco a otra ventana"),
    Key([mod], "Right", lazy.next_layout(), desc="Mover entre Cajas"),
    Key([mod], "Left", lazy.prev_layout(), desc="Mover entre Cajas"),
    
    #Windows
    Key([], "F11", lazy.window.toggle_fullscreen(), desc="Aun no lo he hecho funcionar"),
    Key([], "F10", lazy.window.toggle_floating(), desc="Aun no lo he hecho funcionar"),
    Key(["mod1"], "x", lazy.spawn("xkill"), desc="Aun no lo he hecho funcionar"),
    Key([mod], "x", lazy.window.kill(), desc="Matar ventana enfocada"),
    
    #Qtile
    Key([mod], "Return", lazy.spawn(terminal), desc="Lanzar Terminal"),
    Key([mod], "grave", lazy.group["scratchpad"].dropdown_toggle("term"), desc="Aun no lo he hecho funcionar"),
    KeyChord([mod], "q", [
        Key([], "b", lazy.spawn("bartoggle"), desc="?? quitar barra"),
        Key([], "w", lazy.spawn("walp"), desc="Activar pywalp, selecciona color de paleta y fondo de pantalla"),
        Key([], "c", lazy.spawn("clipmenu"), desc="Mostrar menu del clibboard"),
        Key([], "Delete", lazy.spawn("clipdel -d \".*\" "), desc="Eliminar todo lo que hay en el clipboard"),
        Key([], "r", lazy.restart(), desc="Reiniciar Computador"),
        Key([], "q", lazy.shutdown(), desc="Apagar Computador"),
    ]),
    
    #Audio and Media
    Key([mod], "minus", lazy.spawn("amixer -q sset Master 3%-"), desc="Bajar el Volumen"),
    Key([mod], "plus", lazy.spawn("amixer -q sset Master 3%+"), desc="Subir el Volumen"),
    Key([mod], "0", lazy.spawn("amixer -q sset Master toggle"), desc="Mute"),
    Key([mod], "comma", lazy.spawn("playerctl previous"), desc="Anterior Cancion"),
    Key([mod], "period", lazy.spawn("playerctl next"), desc="Siguiente Cancion"),
    Key([mod], "dead_acute", lazy.spawn("playerctl play-pause"), desc="Pausar/Reproducir"),
    
    #Applications
    Key(["mod1", "control"], "Delete", lazy.spawn ("urxvtc -e htop"), desc="Monitor de Recursos"),
    Key([], "XF86Launch2", lazy.spawn("scrot $HOME/Pictures/scrots/"), desc="Tomar Captura de Pantalla"),
    # Key([mod], "w", lazy.spawn("qutebrowser")),
    Key([mod], "e", lazy.spawn("emacsclient -c "), desc="Cargar Emacs"),
    Key([mod], "r", lazy.spawn("liferea"), desc="Cargas Liferea"),
    Key([mod], "o", lazy.spawn("pavucontrol"), desc="Cargar Control de Volumen"),
    # Key([mod], "c", lazy.spawn("qalculate-gtk")),
    # Key([mod], "g", lazy.spawn("gpodder")),
    Key([mod], "t", lazy.spawn("urxvtc")),
    Key([mod], "m", lazy.spawn("thunderbird")),
    Key([mod], "v", lazy.spawn("vlc")),
    Key([mod], "f", lazy.spawn("nautilus"), desc="Gestor de Archivos"),
    KeyChord([mod], "a", [
        Key([], "d", lazy.spawn("discord")),
        Key([], "w", lazy.spawn("firefox"), desc="Cargar Firefox"),
        Key([], "c", lazy.spawn("gcolor3")),
        Key([], "t", lazy.spawn("xterm")),
        Key([], "p", lazy.spawn("bitwarden-desktop"), desc="Cargas Pass Manager")
    ]),
    
    #Launcher
    Key([mod], "d", lazy.spawn("dmen"), desc="Cargas Menu Rapido"),
    Key(["mod1"], "Tab", lazy.spawn("rofi -show window -show-icons"), desc="Seleccionar Ventana Abierta a partir de menu"),
    Key([mod], "s", lazy.spawn("dmsearch"), desc="Buscar en Internet"),
    
    #Scripts
    Key(["mod1", "control"], "o", lazy.spawn("outputmenu"), desc="Activating listening"),
    Key(["mod1", "control"], "c", lazy.spawn("comptonmenu"), desc="Activar/Desactivar bloqueo de pantalla"),
    Key(["mod1", "control"], "p", lazy.spawn("powermenu"), desc="Ver Menu de Apagado y mas"),
    Key(["mod1", "control"], "l", lazy.spawn("xautolockmenu"), desc="Menu de bloqueo"),
    Key(["mod1", "control"], "s", lazy.spawn("sensornote"), desc="Notificacion del sistema"),
    Key(["mod1", "control"], "g", lazy.spawn("gamesmenu"), desc="Menu de juegos"),
    KeyChord([mod], "space", [
        Key([], "space", lazy.spawn ("rofi -show drun -show-icons -location 7 -yoffset -22"), desc="cargar menu"),
        Key([], "h", lazy.spawn ("hotkey"), desc="Resumen de Teclas de Acceso"),
        Key([], "s", lazy.spawn ("scrotmenu"), desc="Tomar Captura"),
        Key([], "l", lazy.spawn ("libmenu"), desc="Menu de Opciones de Libreria"),
        Key([], "c", lazy.spawn ("calendarmenu"), desc="Menu de Calendario"),
        Key([], "m", lazy.spawn ("chatmenu"), desc="Chat"),
        Key([], "t", lazy.spawn ("timermenu"), desc="Opciones de Tiempo"),
        Key([], "g", lazy.spawn ("graphicsmenu"), desc="Opciones de Graficos")
    ])
]

#Workspace Groups
group_names = [
    ("I", {}),
    ("II", {}),
    ("III", {}),
    ("IV", {}),
    ("V", {}),
    ("VI", {}),
    ("VII", {}),
    ("VIII", {}),
    ("IX", {}),
]
groups = [Group(name, **kwargs) for name, kwargs in group_names]
for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

groups = [
    ScratchPad("scratchpad", [
        DropDown("term", "urxvt", opacity=0.95)
    ]),
    Group("I", layout="monadtall", matches=[
        Match(wm_class=[
            "qutebrowser",
            "Thunderbird",
            "liferea",
        ])
    ]),
    Group("II", layout="monadtall", matches=[
        Match(wm_class=[
            "vlc",
            "gpodder"
        ])
    ]),
    Group("III", layout="bsp", matches=[
        Match(wm_class=[
            "Steam",
            "Lutris",
            "RetroArch",
            "dosbox"
        ])
    ]),
    Group("IV", layout="max", matches=[
        Match(wm_class=[
            "VirtualBox Machine",
            "virt-manager",
            "VirtualBox Manager",
            "VirtualBoxVM"
        ])
    ]),
    Group("V", layout="max", matches=[
        Match(wm_class=[
            "gimp",
            "Inkscape",
            "krita",
            "darktable",
            "shotwell",
            "scribus",
            "Blender"
        ])
    ]),
]

layouts = [
     layout.Bsp(
         margin=5,
         border_focus=ColorE,
         border_normal=ColorA
    ),
    layout.MonadTall(
        margin=5,
        border_focus=ColorE,
        border_normal=ColorA
    ),
    layout.Max(),
]

#Widget Defaults
widget_defaults = dict(
    font="Noto Sans",
    fontsize=13,
    padding=5,
    foreground=ColorG
)
extension_defaults = widget_defaults.copy()

#Screens
screens = [
    Screen(
        top=bar.Bar(
            widgets=[
                widget.GroupBox(
                    highlight_method="line",
                    urgent_border=ColorF,
                    active=ColorG,
                    inactive=ColorB,
                    this_screen_border=ColorB,
                    this_current_screen_border=ColorC,
                ),
                widget.Spacer(length = bar.STRETCH),
                widget.TextBox(
                    text="",
                    mouse_callbacks = {"Button1": quake}
                ),
                widget.Clock(
                    format="%a %b %d",
                    font="Noto Sans Bold",
                    padding=0,
                    mouse_callbacks={"Button1": calendar}
                ),
                widget.Clock(
                    format="%I:%M %p",
                    font="Noto Sans Bold",
                    mouse_callbacks={"Button1": timer}
                ),
                widget.Spacer(length = bar.STRETCH),
                widget.KhalCalendar(
                    foreground="#282828",
                    remindertime=1440,
                    reminder_color=ColorG,
                    mouse_callbacks={"Button1": calendar}
                ),
                widget.Battery(
                    format="{char} {percent:2.0%} {hour:d}:{min:02d}"
                ),
                widget.OpenWeather(
                    cityid=int(city_weather_code),
                    metric=True,
                    format=" {main_temp}°{units_temperature}",
                    mouse_callbacks = {"Button1": weather}
                ),
                widget.TextBox(
                    text="",
                    mouse_callbacks = {"Button1": sound}
                ),
                widget.Volume(),
                widget.TextBox(
                    mouse_callbacks = {"Button1": powermenu},
                    text="",
                ),
                widget.Spacer(length=5)
            ],
            size=22,
            background ="#282828",
        ),
        bottom=bar.Bar(
            widgets=[
                widget.TextBox(
                    text="",
                    foreground=ColorB,
                    mouse_callbacks = {"Button1": launcher}
                ),
                widget.WindowName(font="Noto Sans Bold"),
                widget.Cmus(
                    play_color=ColorG,
                    noplay_color=ColorB
                ),
                widget.CPU(mouse_callbacks = {"Button1": htop}),
                widget.Memory(
                    format="MEM{MemUsed: .0f}{mm}",
                    mouse_callbacks = {"Button1": htop}
                ),
                widget.Systray(),
                widget.CurrentLayoutIcon(scale=.65),            
                widget.TextBox(
                    text="",
                    mouse_callbacks = {"Button1": metamenu}
                )
            ],
            size=22,
            background="#282828",
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", 
         lazy.window.set_position_floating(),
         start=lazy.window.get_position()
    ),
    Drag([mod], "Button3", 
         lazy.window.set_size_floating(),
         start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=ColorE,
    border_normal=ColorA,
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
        Match(title="khal"),
        Match(title="Volume Control"),
        Match(title="Library"),
        Match(title="Unlock Login Keyring"),
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="lxpolkit"),
        Match(wm_class="error"),
        Match(wm_class="pamac-manager"),
        Match(wm_class="lxappearance"),
        Match(wm_class="kvantummanager"),
        Match(wm_class="file_progress"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="gcolor3"),
        Match(wm_class="qalculate-gtk"),
        Match(wm_class="qt5ct"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = False
wmname = "LG3D"
