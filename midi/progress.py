# thank you to tempookian for the script
# https://github.com/Textualize/rich/discussions/482#discussioncomment-9353238

from collections import deque

from rich.console import ConsoleRenderable, Group, RichCast
from rich.progress import Progress
from rich.table import Table


class CustomProgress(Progress):
    def __init__(self, table_max_rows: int, *args, **kwargs) -> None:
        self.results = deque(maxlen=table_max_rows)
        self.update_table()
        super().__init__(*args, **kwargs)

    def update_table(self, result: tuple[str] | None = None):
        if result is not None:
            self.results.append(result)
        table = Table()
        table.add_column("Row ID")
        table.add_column("Result", width=20)

        for row_cells in self.results:
            table.add_row(*row_cells)

        self.table = table

    def get_renderable(self) -> ConsoleRenderable | RichCast | str:
        renderable = Group(self.table, *self.get_renderables())
        return renderable
