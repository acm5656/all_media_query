#!/usr/bin/env python
import os
import sys
import py_eureka_client.eureka_client as eureka_client
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "all_media.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    your_rest_server_host = "223.3.83.187"
    your_rest_server_port = 8000
    # The flowing code will register your server to eureka server and also start to send heartbeat every 30 seconds
    eureka_client.init_registry_client(eureka_server="http://223.3.65.243:8761/eureka/",
                                       app_name="cmai_search",
                                       instance_host=your_rest_server_host,
                                       instance_port=your_rest_server_port)
    execute_from_command_line(sys.argv)
