
.PHONY: install update-scripts update

install:
	ln -sf --no-target-directory $(realpath .) ~/.config/mpv

update-scripts:
	./build-aux/update-plugins.zsh .
