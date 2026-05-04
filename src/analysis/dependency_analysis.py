def is_vectorizable(loop):
    line = loop["line"]

    # simple assumption: for loops are vectorizable
    if loop["type"] == "for":
        return True

    return False