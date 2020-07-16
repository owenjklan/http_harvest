class ScanAction(object):
    next_id = 1

    def __init__(self, ip, port, protocol, status_code, status_string):
        self.id = ScanAction.next_id
        self.ip = ip
        self.port = port
        self.protocol = protocol
        self.status_code = status_code
        self.status_string = status_string
        self.start_time = time.time()

        ScanAction.next_id += 1
