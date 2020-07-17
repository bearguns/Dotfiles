set -x EDITOR emacs
set -x FISHCONFIG ~/.config/fish/config.fish
set -x TERMINAL alacritty
set -x XDG_CONFIG_HOME ~/.config
set -x VISUAL emacs

# Configure my fancy prompt
set SPACEFISH_PACKAGE_SHOW false
set SPACEFISH_NODE_SHOW true
set SPACEFISH_VI_MODE_SHOW true

if not functions -q fisher
    curl https://git.io/fisher --create-dirs -sLo $XDG_CONFIG_HOME/fish/functions/fisher.fish
    fish -c fisher
end

# Aliases for common operations
# Refer to fishfile for additional plugins that may add aliases
## Docker Aliases
alias dcup 'docker-compose up'
alias dcdown 'docker-compose down'
alias dps 'docker ps'
alias dimages 'docker images'

alias config 'git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'
