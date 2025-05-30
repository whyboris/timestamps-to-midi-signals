# Timestamps to MIDI signals

**Send MIDI notes based on a timestamp table**

Ingest a tab-separated text file formatted thus:

```txt
Position	Name
00:00:03.50	2
00:00:04.20	3
00:00:20.25	2
```

And send notes over MIDI at the precise positions found in time.

## Use case

A VJ can play pre-determined precisely timed video effects inside _Resolume Avenue_ or _Resolume Arena_ over an audio track while still retaining creative control and improvisation ability of using the software.

### Generating markers with _Vegas Pro_

You can use the _Vegas Pro_ video editing software to insert markers wherever (in a video or audio) and then copy the table of times and marker names to a text file. This script will then play midi notes depending on the marker names (as defined in the script).

In _Vegas Pro_ click on _Tools_ in the file menu (or _View_ then _Window_), then _Edit Details_ (shortcut _Alt_ + _6_) and then under _Show_ dropdown select _Markers_. Either click the _save_ icon to save, or click on the top-left square in the table to copy the table into your clipboard (then paste into `markers.txt` in this folder).

## Requirements

You'll need to install _Python_ (and [`uv`](https://github.com/astral-sh/uv) recommended for a better experience)

You'll need to have an available virtual MIDI port open. On _Windows_ you can download [loopMIDI](https://www.tobias-erichsen.de/software/loopmidi.html) to create a port hassle-free. On _Mac_ it seems possible to do without downloading anything, please see a tutorial online.

## Use

I recommend you use [`uv`](https://github.com/astral-sh/uv) to install the _Python_ dependencies and run the script, though feel free to use _Python_ however you'd like.

Make sure the `MIDI_PORT_NAME` in `midi.py` coincides with the available MIDI port you have.

```sh
uv run main.py
```

Update the `markers.txt` with your own timestamps and note numbers.

## Notes

Code is formatted with [black](https://github.com/psf/black). Run `uvx black .` to format after edits. You can also run `uvx ruff format` to format or `uvx ruff check` to see _lint_ errors.

The quality of code in this repository isn't excellent, but it gets the job done and should be easy to modify. Feel free to offer a _PR_ with improvements.
