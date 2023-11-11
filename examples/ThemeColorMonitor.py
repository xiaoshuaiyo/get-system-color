import get_system_color


def my_callback(accent_color):
    # 在这里执行自定义的操作
    print("主题色已更改:", accent_color)


monitor = get_system_color.ThemeColorMonitor(callback=my_callback)
monitor.check_theme_change()
