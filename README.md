# pybruh
pybruh is a very epic (pointless) Python script that I made to randomly play loaded sound files at random time intervals. It originated as a simple infinite loop that would occasionally play a bruh sound effect every few minutes while using my computer. I decided to expand it into this project after deciding that I wanted it to be able to play multiple different sound files.

## Running the Program
1. Clone the repository: `git clone https://github.com/jackmj1024/pybruh.git`
2. Run `pybruh.py` in one of two ways:
	- Execute `./pybruh.sh` to run in the Python virtual environment with all dependencies installed (Linux only).
	- Execute `python pybruh.py` directly after installing the following depencies:
		- pydub: `pip install pydub`

## Configuration
- The Python script automatically loads all .wav files within the `sounds/` directory.
	- Only the bruh sound effect is included by default.
	- Place .wav files in the `sounds/` directory to add them to the pool of randomly selected sounds.
	- You can also edit the `SOUND_DIRECTORY` variable if you want to change where the sound files are loaded from (for some reason...).
- The script's main loop will randomely select a delay time (in seconds) before playing the next sound.
	- Edit the `MIN_INTERVAL` value at the top of `pybruh.py` to change the minimum delay time.
	- Edit the `MAX_INTERVAL` value at the top of `pybruh.py` to change the maximum delay time.
- You can enable `USE_SIGMOID` to use an alternative calculation method for the randomized delay.
 	- This feature uses the [sigmoid function](https://en.wikipedia.org/wiki/Sigmoid_function) to calculate the delay. The curve for this function can be viewed on [this Desmos graph](https://www.desmos.com/calculator/rxvvgaqo4x)

## Planned Features (if I feel like it)
- Support for more audio formats.
- Windows bat file to run in virtual environment.
- Binary to run the program as a normal terminal command.
	- Pass in configuration as command arguments.
	- ...or maybe just have a separate config file?
- Support different randomization weights for different sounds.
- An elegant way to exit the loop.
	- AKA don't use `while True` because that's cringe.
- Whatever else comes to mind.

### What if I want to contribute my own features?
- You should consider valuing your time a bit more.
- Just modify it yourself and make a pull request, I'll probably accept it.
