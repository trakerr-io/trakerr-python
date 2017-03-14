﻿
import sys

"""
#Normal automatic instantiation
from trakerr import Trakerr
"""

"""
#With handler, manual init
import logging
from trakerr import TrakerrHandler
"""


# Without handler custom peramiters
from trakerr import TrakerrClient
from trakerr_client.models import CustomData, CustomStringData


def main(argv=None):
    """
    Main method.
    """
    """
    if argv is None:
        argv = sys.argv

    logger = Trakerr.getLogger("ca6b942a89e04069ec96fa2b3438efb310995233724595", "1.0", "newlogger")
    try:
        error()
    except:
        logger.exception("Bad math.")
    """

    """
    #Manual instantiation of the logger.
    logger = logging.getLogger("Logger name")
    th = TrakerrHandler("API KEY", "App Version number here")
    logger.addHandler(th)

    try:
        raise ArithmeticError()
    except:
       logger.exception("Bad math.")

    """

    client = TrakerrClient("API KEY", "App Version number here")

    try:
        raise IndexError("Bad Math")
    except:
        appevent = client.create_new_app_event("ERROR", "Index Error", "Math")
        #appevent = client.create_new_app_event("ERROR", "Index Error", "Math")
        #  #You can use this call to create an app event without a stacktrace,
        # in case you do don't have a stacktrace or you're not sending a crash.

        # Populate any field with your own data, or send your own custom data
        appevent.context_app_os = "Windows 8"
        # Can support multiple ways to input data
        appevent.custom_properties = CustomData("Custom Data holder!")
        appevent.custom_properties.string_data = CustomStringData("Custom String Data 1",
                                                                  "Custom String Data 2")
        appevent.custom_properties.string_data.custom_data3 = "More Custom Data!"
        appevent.event_user = "john@traker.io"
        appevent.event_session = "6"

        # send it to trakerr
        client.send_event_async(appevent)

    return 0


def error():
    raise EOFError()


if __name__ == "__main__":
    # main()
    sys.exit(main())
