class Window:
    def __init__(self, title, x_pos, y_pos, width, heigth, background, set_bar=True) -> None:
        self.title = title
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.set_bar = set_bar

        if not self.set_bar:
            self.width = width
            self.heigth = heigth

            self.is_show = False
            self.vbuffer = []
            for i in range(self.heigth):
                self.vbuffer.append([background] * self.width)

        else:
            self.width = width+2
            self.heigth = heigth+4

            self.is_show = False
            self.vbuffer = []
            for i in range(self.heigth):
                if i == 0 :
                    self.vbuffer.append(['┌'] + ['─'] * (self.width-2) + ['┐'])
                elif i == 1:
                    if len(title) > self.width - 7:
                        show_title = list(title[:self.width - 10]) + ['.','.','.']
                    else:
                        show_title = list(title)
                    
                    self.vbuffer.append(['│'] + show_title + [' ']*(self.width-len(show_title)-7) + list('- * x│'))
                elif i == 2:
                    self.vbuffer.append(['├'] + ['─'] * (self.width-2) + ['┤'])
                elif i == self.heigth - 1:
                    self.vbuffer.append(['└'] + ['─'] * (self.width-2) + ['┘'])
                else:
                    self.vbuffer.append(['│'] + [background] * (self.width-2) + ['│'])

    def show(self):
        self.is_show = True

    def hide(self):
        self.is_show = False

    def draw_line(self, start_pos, end_pos, char='*'):
        x1, y1 = start_pos
        x2, y2 = end_pos
        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        x, y = x1, y1
        sx = -1 if x1 > x2 else 1
        sy = -1 if y1 > y2 else 1

        if dx > dy:
            err = dx / 2.0
            while x != x2:
                self.vbuffer[y][x] = char
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != y2:
                self.vbuffer[y][x] = char
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy

