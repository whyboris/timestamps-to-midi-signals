import mido
from rich import print

MIDI_PORT_NAME = "loopMIDIPort 1"

print("")
print("Available MIDI devices")
print(mido.get_output_names())
print("")

try:
    output_port = mido.open_output(MIDI_PORT_NAME)
except:
    print("[red bold]error[/red bold]: midi port [green]" + MIDI_PORT_NAME + "[/green] not found")
    print("are you running loopMIDI with this port name?")
    exit()


def send_midi(marker_name: str):
    """
    str marker_name - to send over to midi

    Can be anything between 0 and 127 (inclusive)
    """
    if marker_name == "START":
        midi_note = 0
    else:
        midi_note = int(marker_name)
    play_midi_note(midi_note)


def play_midi_note(note_number: int):
    if note_number is not None:
        msg = mido.Message(
            "note_on", note=note_number, velocity=64
        )  # velocity is between 0 and 127 (inclusive)
        output_port.send(msg)
