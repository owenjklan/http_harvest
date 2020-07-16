class OutputHandler(object):
    def __init__(self):
        pass

    def update_scan(self, scan):
        pass

    def finish_scan(self):
        pass


class InteractiveConsoleOutput(OutputHandler):
    def __init__(self):
        # super(InteractiveConsoleOutput, self).__init__():
        pass


class GrepConsoleOutput(OutputHandler):
    def __init__(self):
        # super(GrepConsoleOutput, self).__init__():
        pass


class HTMLOutput(OutputHandler):
    def __init__(self):
        # super(HTMLOutput, self).__init__():
        pass


class SQLiteOutput(OutputHandler):
    def __init__(self):
        # super(SQLiteOutput, self).__init__():
        pass

## Helper functions for colour
def yellow_text(text, html=False):
    outtext = "\033[33m\033[1m{}\033[0m".format(text)
    return outtext


def green_text(text, html=False):
    outtext = "\033[32m\033[1m{}\033[0m".format(text)
    return outtext


def red_text(text, html=False):
    outtext = "\033[31m\033[1m{}\033[0m".format(text)
    return outtext


def cyan_text(text, html=False):
    outtext = "\033[36m\033[1m{}\033[0m".format(text)
    return outtext


def magenta_text(text, html=False):
    outtext = "\033[35m\033[1m{}\033[0m".format(text)
    return outtext


def usage(progname):
    print("Usage:   {} webaddress".format(progname))


# Format to dotted-quad
def format_ip_from_parts(parts_list):
    return ".".join(parts_list)