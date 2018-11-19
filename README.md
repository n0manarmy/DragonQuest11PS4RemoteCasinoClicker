Dragon Quest 11 Clicker for the Casinos using PS4 Remote Play

This utility is a way to click through the casino selections when playing Dragon Quest 11 on the PS4. You do not need to configure the controller for remote play and can keep it connected to the PS4. The remote play software initializes the enter key similar to the "x" button, allowing us to smash enter. This script does that for us.

I did some digging and was trying to find the best way to auto play the slots in DQ11 on the PS4. There were comments about rapid fire on controllers, but I didn't have one. I saw a github project about using PS4 remote play and writing complex macros which I didn't have much success with. I had a "Duh!" moment and realized I could write a simple python app that would run and just hit the enter key during random intervals for me using the PS4 remote play.

Your system will need to be able to run the PS4 remote play application here: https://remoteplay.dl.playstation.net/remoteplay/lang/en/index.html

I wrote this with python 3.6 which will also need to be installed. I needed to install the pypiwin32 libraries to have Windows key command capabilities. This was done by running the below commands. Pip needed to be updated too.

python -m pip install pip
  
python -m pip install pypiwin32

Directions: Load up your PS4, run to the slots, set yourself at the slot machine you want to run, and load up the max amount of bets you want to use.

From the command prompt run the below script as "python script.py"

The script will run continously until you "ctrl + c" the command line that's running the script

Current release is version 1.0
