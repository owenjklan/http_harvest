import sys


class OutputHandler(object):
    def __init__(self):
        pass

    def start_scan(self, scan):
        pass

    def update_scan(self, scan):
        pass

    def finish_scan(self, secs_taken, code):
        pass

    def bulk_scan_start(self, ip_parts, location=None):
        pass

    def bulk_scan_end(self, secs_taken, hosts_list=None):
        pass


class DefaultOutput(OutputHandler):
    def __init__(self):
        super(DefaultOutput, self).__init__()

    def start_scan(self, ip_parts, base_url, port):
        print (u"{:>16}:{:<5}  |  ".format(".".join(ip_parts), port), end="")
        sys.stdout.flush()

    def update_scan(self, scan):
        pass

    def finish_scan(self, scan, used_plugins=True):

        print("{:5s}  {:>2.2f}s [{:^20}] ({})".format(
            scan.status_string, scan.end_time - scan.start_time,
            scan.server, scan.country,))

        if used_plugins and scan.plugin_output:
            print(scan.plugin_output)


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


# Helper functions for colour
def red_text(text, html=False):
    outtext = "\033[31m\033[1m{}\033[0m".format(text)
    return outtext


def green_text(text, html=False):
    outtext = "\033[32m\033[1m{}\033[0m".format(text)
    return outtext


def yellow_text(text, html=False):
    outtext = "\033[33m\033[1m{}\033[0m".format(text)
    return outtext


def blue_text(text, html=False):
    outtext = "\033[34m\033[1m{}\033[0m".format(text)
    return outtext


def magenta_text(text, html=False):
    outtext = "\033[35m\033[1m{}\033[0m".format(text)
    return outtext


def cyan_text(text, html=False):
    outtext = "\033[36m\033[1m{}\033[0m".format(text)
    return outtext


def info_banner(text, html=False):
    outtext = "\033[35m\033[1m{}\033[0m".format(text)
    return outtext


def title_banner(text, html=False):
    outtext = "\033[44;33;1m{}\033[0m".format(text)
    return outtext


def warning_banner(text, html=False):
    outtext = "\033[35m\033[1m{}\033[0m".format(text)
    return outtext


def error_banner(text, html=False):
    outtext = "\033[35m\033[1m{}\033[0m".format(text)
    return outtext


def debug_banner(text, html=False):
    outtext = "\033[35m\033[1m{}\033[0m".format(text)
    return outtext


# Format to dotted-quad
def format_ip_from_parts(parts_list):
    return ".".join(parts_list)
