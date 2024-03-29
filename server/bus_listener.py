import controller


class BusListener:

    def process_control_event(self, msg):
        print('Method Listener.process_control_event received: ', repr(msg))
        #enumValue = ControlPayload(msg)
        if 'FORWARD' == msg:
            controller.forward()
        if 'STOP' == msg:
            controller.stop()
        if 'BACKWARD' == msg:
            controller.backward()
        if 'LEFT' == msg:
            controller.left()
        if 'RIGHT' == msg:
            controller.right()
        if 'STRAIGHT' == msg:
            controller.straight()

    def process_speed_event(self, msg):
        print('Method Listener.process_speed_event received: ', repr(msg))

    def __call__(self, **kwargs):
        print('BusListener instance received: ', kwargs)