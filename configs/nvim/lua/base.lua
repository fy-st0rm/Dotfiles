local g = vim.g
local o = vim.o
local opt = vim.opt

-- cmd('syntax on')
-- vim.api.nvim_command('filetype plugin indent on')

-- Enabled for nvim-tree
g.loaded_netrw = 1
g.loaded_netrwPlugin = 1

-- Shell
o.shell = "bash"

o.termguicolors = true
-- o.background = 'dark'

-- Decrease update time
o.timeoutlen = 500
o.updatetime = 200

-- Number of screen lines to keep above and below the cursor
o.scrolloff = 8

-- Better editor UI
o.number         = true
o.numberwidth    = 2
o.relativenumber = true
o.signcolumn     = "yes"
o.cursorline     = true

-- Some basic features
opt.mouse     = "a"
o.expandtab   = true
o.hlsearch    = false
o.smarttab    = true
o.cindent     = true
o.autoindent  = true
o.wrap        = true
o.textwidth   = 300
o.tabstop     = 4
o.shiftwidth  = 4
o.softtabstop = -1 -- If negative, shiftwidth value is used
o.list        = true
o.listchars   = "trail:·,nbsp:◇,tab:┊ ,extends:▸,precedes:◂"

-- Setting tabs instead of spaces
vim.cmd("autocmd FileType * setlocal noexpandtab")

-- Makes neovim and host OS clipboard play nicely with each other
o.clipboard = "unnamedplus"

-- Case insensitive searching UNLESS /C or capital in search
o.ignorecase = true
o.smartcase  = true

-- Undo and backup options
o.backup      = false
o.writebackup = false
o.undofile    = true
o.swapfile    = false

-- Remember 50 items in commandline history
o.history = 50

-- Better buffer splitting
o.splitright = true
o.splitbelow = true

-- Map <leader> to space
g.mapleader      = " "
g.maplocalleader = " "