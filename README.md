# Pomodoro Discord Bot
A discord bot that utilizes the Pomodoro technique to help users stay productive.

# Features
The bot messages the user when to begin working and take a break.
- Messages include timestamps
- If no arguments/incomplete arguments are given, default parameters are used

# Commands
- .timer [minutes work interval] [minutes small break] [minutes long break]

# To Do
- [x] Basic timer function
- [ ] N amount of pomodoro cycles
- [ ] Customizable work/break messages
- [ ] Getting it to production

# Prerequisites
- Python 3+ and pip

# Installation
- Clone this repository `git clone https://github.com/kxvxnc/Pomodoro-Discord-Bot.git`
- Change directories to the project folder `cd /to/your/directory/Pomodoro-Discord-Bot`
- Install dependencies pip install -r requirements.txt
- Create an application at the [Discord Developer Portal](https://discord.com/developers/applications)
- Edit line 6 in main.py with your own bot token and save
- Run main.py `python main.py`