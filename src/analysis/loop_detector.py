def detect_loops(code):
    loops = []

    lines = code.split("\n")

    for line in lines:
        line = line.strip()

        if line.startswith("for"):
            loops.append({"type": "for", "line": line})

        elif line.startswith("while"):
            loops.append({"type": "while", "line": line})

    return loops