def get_cli_args():
    """
    Returns a dictionary of arguments passed to through the CLI.
    """
    import re
    import sys

    args = {}

    for arg in sys.argv[1:]:
        var = re.search('\-\-([A-Za-z]*)', arg)
        var = var.group(1)
        value = re.search('\=(.*)', arg)
        value = value.group(1) if value else None
        args[var] = value

    return args
