#!/usr/bin/zsh

TRAPEXIT() {
	rm -rf $TMP
}

TMP=$(mktemp -d mpv.update.XXXXXXXX)

plugins=('modernx.lua' 'Thumbnailer.lua' 'Thumbnailer_Worker.lua')

for plugin in $plugins; do
	curl -L -o "$TMP/$plugin" "https://github.com/dexeonify/mpv-config/raw/main/scripts/$plugin"
done

mv -t $1/scripts "$TMP"/*

fonts=('modernx-osc-icon.ttf')

for font in $fonts; do
	curl -L -o "$TMP/$font" "https://github.com/dexeonify/mpv-config/raw/main/fonts/$font"
done

mv -t $1/fonts "$TMP"/*
