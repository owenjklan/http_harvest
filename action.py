import time


class ScanAction(object):
    next_id = 1

    def __init__(self, ip, port, protocol, status_code=None,
                 status_string=None):
        self.id = ScanAction.next_id
        self.ip = ip
        self.port = port
        self.protocol = protocol
        self.status_code = status_code
        self.status_string = status_string
        self.start_time = time.time()
        self.end_time = 0
        self.server = "???"
        self.country = "???"
        self.auth_realm = None
        self._response = None

        @property
        def response(self):
            return self._response

        @response.setter
        def response(self, val):
            self._response = val
            if self._response is None:
                return
            self.status_string = val.reason
            self.status_code = val.status_code
        

        self.plugin_output = None
        ScanAction.next_id += 1
