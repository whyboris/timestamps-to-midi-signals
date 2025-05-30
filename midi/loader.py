import csv
from rich.table import Table
from rich.console import Console
from rich import box

def get_markers(marker_file):
    """
    Get data from `markers.txt` file
        Two tab-separated columns: "Position" and "Name"
        Position formatted: `00:01:05.17`

    Returns: list of tuples
        (int time_in_milliseconds_from_start, str marker_name)
    """

    events = []
    milliseconds = []
    timestamps = []

    with open(marker_file) as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            timestamps.append(row["Position"])
            milliseconds.append(timestamp_to_milliseconds(row["Position"]))
            events.append(row["Name"])

    full = list(zip(milliseconds, events))

    generate_table(timestamps, milliseconds, events)

    return full


def generate_table(timestamp, milliseconds, event):
    table = Table(title="MIDI timed events", box=box.SIMPLE, padding=(0,2,0,2))

    table.add_column("Timestamp", justify="left", style="cyan")
    table.add_column("milliseconds",  justify="right", style="cyan")
    table.add_column("Marker", justify="right", style="green")

    for i in enumerate(event):
        table.add_row(timestamp[i[0]], str(milliseconds[i[0]]), event[i[0]])

    console = Console()
    console.print(table)

def timestamp_to_milliseconds(timestamp):
    """
    str timestamp formatted `00:01:05.17`

    Returns: int
    """
    hours, minutes, seconds, milliseconds = [
        int(x) for x in timestamp.replace(".", ":").split(":")
    ]

    return milliseconds + 1000 * (seconds + 60 * (minutes + 60 * hours))
