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

# anything between 0 and 127 (inclusive)
note_to_midi = {
    "START": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
}


def send_midi(event):
    """
    str event - to send over to midi
    """
    print("sending", event)
    play_midi_note(event)


def play_midi_note(note_number):
    midi_note = note_to_midi.get(note_number)
    if midi_note is not None:
        msg = mido.Message(
            "note_on", note=midi_note, velocity=64
        )  # velocity is between 0 and 127 (inclusive)
        output_port.send(msg)
