#!/bin/bash

DOTFILES_DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Installing dotfiles from $DOTFILES_DIR"

CONFIGS=(qtile ghostty alacritty fish fontconfig nvim rofi fastfetch)

for app in "${CONFIGS[@]}"; do
    target="$HOME/.config/$app"
    source="$DOTFILES_DIR/$app"

    # Skip if source doesn't exist (e.g. qtile points to whole repo)
    if [ "$app" = "qtile" ]; then
        source="$DOTFILES_DIR"
    fi

    # Backup if exists and not already a symlink
    if [ -d "$target" ] && [ ! -L "$target" ]; then
        echo "Backing up $target to $target.bak"
        mv "$target" "$target.bak"
    fi

    ln -sfn "$source" "$target"
    echo "Symlinked $target -> $source"
done
