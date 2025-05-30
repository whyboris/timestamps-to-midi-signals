import datetime
import time

from loader import get_markers
from midi import send_midi
from progress import CustomProgress

MARKER_FILE = "markers.txt"  # Edit the filename if you prefer something different

sequence = iter(get_markers(MARKER_FILE))  # convert to iterator


def print_time_from(initial):
    current_moment = time.time()
    print(round(current_moment - initial, 3))


def main():
    start = time.time()

    print("")
    print("Starting sequence")
    print("")

    initial_time = datetime.datetime.now()
    next_time = datetime.datetime.now()
    next_event = "START"

    print(initial_time.strftime("%M:%S.%f")[:-3], next_event)
    print("")

    time1, event = next(sequence)
    next_time = initial_time + datetime.timedelta(milliseconds=time1)

    # print("exiting")
    # exit()

    with CustomProgress(table_max_rows=10) as progress:
        task = progress.add_task("Task", total=100)
        for row in range(100):
            time.sleep(0.1)
            progress.update(task, advance=1)
            progress.update_table((f"{row}", f"Result for row {row}"))

    while True:
        current_time = datetime.datetime.now()

        if current_time >= next_time:
            print_time_from(start)

            send_midi(next_event)
            print(next_time.strftime("%M:%S.%f")[:-3], "\t", next_event)

            try:
                time1, event = next(sequence)
            except:
                print("DONE!")
                exit()

            next_time = initial_time + datetime.timedelta(milliseconds=time1)
            next_event = event

            # TODO: sleep here for duration until next beat instead

        time.sleep(0.05) # crappy hack for now



main()
