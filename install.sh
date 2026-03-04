#!/bin/bash

DOTFILES_DIR="$(cd "$(dirname "$0")" && pwd)"
CONFIG_DIR="$HOME/.config/qtile"

echo "Installing Qtile dotfiles from $DOTFILES_DIR"

# Backup existing config if it's not already a symlink
if [ -d "$CONFIG_DIR" ] && [ ! -L "$CONFIG_DIR" ]; then
    echo "Backing up existing config to $CONFIG_DIR.bak"
    mv "$CONFIG_DIR" "$CONFIG_DIR.bak"
fi

# Create symlink
ln -sfn "$DOTFILES_DIR" "$CONFIG_DIR"
echo "Symlinked $CONFIG_DIR -> $DOTFILES_DIR"
