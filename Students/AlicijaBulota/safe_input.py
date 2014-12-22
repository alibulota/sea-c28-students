def safe_input(string):
    """return None instead of raising exceptions"""
    try:
        out_put = raw_input(string)
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        return out_put
