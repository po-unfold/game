# Pushing Outshoot Unfold

*remembering the pandemic*

### Install:
[go here](https://pounfold.netlify.app/)

### File Structure:
basically just ignore all folders except `pushing_outshoot_unfold`
```text
./
├───...
├───pushing_outshoot_unfold/     #(the main source )
│   ├───days/                    # The only days folder.
│   │   ├───001a.toml            # Day 1 version A
│   │   └───001b.toml            # Day 1 version B
│   ├───sounds/                  # Sound files
│   ├───__init__.py              # Contains metadata, just ignore
│   ├───__main__.py              # Entrypoint for the project, main code here
│   ├───ascii.py                 # Dynamic ASCII art functions
│   ├───banner.py                # Title screen ASCII stuff
│   ├───eng.py                   # English questions
│   ├───math.py                  # Math questions
│   ├───sci.py                   # English questions
│   ├───sound.py                 # Code to run cross-platform sound files
│   └───interactions.py          # Main code for each day, plus utility funcs for stories
├───sailboat.toml                # Config file for distribution
├───icon.*                       # Icons
└───run.py2                      # repl.it script to run project easily with run button
```
