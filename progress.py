# thank you to tempookian for the script
# https://github.com/Textualize/rich/discussions/482#discussioncomment-9353238

from collections import deque

from rich.console import ConsoleRenderable, Group, RichCast
from rich.progress import Progress
from rich.table import Table
from rich import box

class CustomProgress(Progress):
    def __init__(self, table_max_rows: int, *args, **kwargs) -> None:
        self.results = deque(maxlen=table_max_rows)
        self.update_table()
        super().__init__(*args, **kwargs)

    def update_table(self, result: tuple[str] | None = None):
        if result is not None:
            self.results.append(result)
        table = Table(box=box.SIMPLE, padding=(0,2,0,2))
        table.add_column("Timestamp", justify="right", style="cyan")
        table.add_column("MIDI note",  justify="right", style="green", width=10)

        for row_cells in self.results:
            table.add_row(*row_cells)

        self.table = table

    def get_renderable(self) -> ConsoleRenderable | RichCast | str:
        renderable = Group(self.table, *self.get_renderables())
        return renderable
