import time
from window import Window
from windows_manager import windows_manager

def main():
    
    test_window_id: int = windows_manager.add_window('Test Window')
    windows_manager.find_window_by_id(test_window_id).show()

    new_window_id: int = windows_manager.add_window('New Window')
    new_window: Window = windows_manager.find_window_by_id(new_window_id)
    new_window.draw_line((5,3), (48,12), char='*')
    new_window.show()

    windows_manager.show()


if __name__ == '__main__':
    main()

    while True:
        time.sleep(1)
        pass