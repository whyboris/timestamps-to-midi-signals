import datetime
import time

from loader import get_markers
from midi import send_midi
from progress import CustomProgress

MARKER_FILE = "markers.txt"  # Edit the filename if you prefer something different

markers = get_markers(MARKER_FILE)
sequence = iter(markers)  # convert to iterator


def get_time_from(initial):
    current_moment = time.time()
    return "{:.3f}".format(round(current_moment - initial, 3))


def main():
    start = time.time()

    initial_time = datetime.datetime.now()
    next_time = datetime.datetime.now()
    next_event = "START"

    time1, event = next(sequence)
    next_time = initial_time + datetime.timedelta(milliseconds=time1)

    with CustomProgress(table_max_rows=10) as progress:

        task = progress.add_task("MIDI", visible=False)

        while True:
            current_time = datetime.datetime.now()

            if current_time >= next_time:

                send_midi(next_event)

                progress.update(task, advance=1)

                progress.update_table((get_time_from(start), next_event))

                try:
                    time1, event = next(sequence)
                except:
                    progress.console.print(f"\tMIDI notes done playing!")
                    exit()

                next_time = initial_time + datetime.timedelta(milliseconds=time1)
                next_event = event

                # TODO: sleep here for duration until next beat instead

            time.sleep(0.05) # crappy hack for now


main()
