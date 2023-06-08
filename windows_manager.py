from typing import Dict, List
import os
import sys
import shutil
from window import Window


class WindowsManager:
    total_windows: Dict[int, Window] = {}
    vbuffer: List[List[str]] = []
 
    def __init__(self, heigth: int, width: int) -> None:
        os.system('cls')
        self.heigth: int = 0 if heigth < 0 else heigth
        self.width: int = 0 if width < 0 else width

        for i in range(self.heigth):
            self.vbuffer.append([' '] * self.width)

    def add_window(self, title: str, background: str = ' ') -> int:
        window: Window = Window(
            title=title,
            x_pos=5+((len(self.total_windows))*4),
            y_pos=5+((len(self.total_windows))*4),
            heigth=30,
            width=60,
            background=background[0]
        )

        self.total_windows[id(window)] = window
        return id(window)

    def find_window_by_id(self, id: int) -> Window:
        return self.total_windows[id]

    def refresh_vbuffer(self) -> None:
        for window in self.total_windows.values():
            if not window.is_show:
                continue

            # TODO: 处理边界情况

            for line_num in range(window.heigth):
                self.vbuffer[window.y_pos + line_num][window.x_pos:window.x_pos + window.width] = window.vbuffer[line_num]
                # print(''.join(self.vbuffer[window.y_pos + line_num]))


    def show(self) -> None:
        self.refresh_vbuffer()

        os.system('cls')

        # start
        sys.stdout.write('┌' + '─' * self.width + '┐' + '\n')
        
        # content
        for line in self.vbuffer:
            sys.stdout.write('│')
            for char in line[:self.width]:
                sys.stdout.write(char)
            sys.stdout.write('│' + '\n')
        
        # end
        sys.stdout.write('└' + '─' * self.width + '┘')

        sys.stdout.flush()

rows, columns = shutil.get_terminal_size()
windows_manager = WindowsManager(width=rows-2, heigth=columns-2)
