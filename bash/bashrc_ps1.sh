# Add lines below to ~/.bashrc
# PS1 Prompt
White="\[\033[0;37m\]"
Red="\[\033[0;31m\]"
Green="\[\033[0;32m\]"
Blue="\[\033[0;34m\]"
Cyan="\[\033[0;36m\]"

ps1_prompt() {
    local __last_exit=$?
    [[ -f ~/.colors ]] && source ~/.colors

    local _decorator=${Blue}
    local _git=${Green}
    local _directory=${Blue}
    local _hostname=${Cyan}
    local _tty=${Cyan}
    local __prompt="${_color1}─▶ ${White}"

    PS1="\n${_decorator}╭─┤${_tty}\l${_decorator}├─ ${_hostname}\u@\h:${_directory}[\w]${_decorator}${_git}$(__git_ps1)${_decorator}\n${_decorator}╰${__prompt}"
}
export PROMPT_COMMAND=ps1_prompt