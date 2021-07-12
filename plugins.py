import requests
import textwrap


PLUGIN_INDENT_WIDTH = 8


def dictify_cookies(session):
    if session and session.cookies:
        session_cookies = session.cookies
        return session_cookies.get_dict()
    else:
        return {}


def plugin_test_main(scan, session):
    cookies = dictify_cookies(session)
    output_string = " ({}:{}) {} Cookies".format(
        scan.ip, scan.port, len(dictify_cookies(session)))
    return output_string


def plugin_status_main(scan, session):
    output_string = " [{} - {}]".format(scan.status_code, scan.status_string) if scan.response else ""
    return output_string


PLUGINS = {
    "test": plugin_test_main,
    "status": plugin_status_main,
}


def run_all_plugins(scan, session, multiline=True):
    """
    'scan' is the current ScanAction
    'session' is the current requests.Session, after an initial GET
    """
    plugin_output = ""
    for plugin in PLUGINS:
        plugin_output += PLUGINS[plugin](scan, session)
    plugin_output = textwrap.indent(plugin_output, PLUGIN_INDENT_WIDTH * " ")
    return plugin_output
