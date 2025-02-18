#!/bin/bash
. "${HOME}/.cache/wal/colors.sh"
query=$(echo '' | dmenu -p "Ask:" -nb "#282828" -nf "$color15" -sb "$color2" -sf "$color15" -h '22' -fn "Jetbrains Mono")
if [ -n "$query" ]; then
    urxvt tgpt "${query}"
fi
