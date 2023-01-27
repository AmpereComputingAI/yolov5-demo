import logging

def set_logging(name=None, verbose=True):
    # Sets level and returns logger
    level = logging.DEBUG if verbose else logging.INFO
    log = logging.getLogger(name)
    log.setLevel(level)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(module)s:%(funcName)s:%(message)s"))
    handler.setLevel(level)
    log.addHandler(handler)

set_logging()  # run before defining LOGGER
LOGGER = logging.getLogger("yolov5")  # define globally (used in other modules)
FPS: float = 1./30