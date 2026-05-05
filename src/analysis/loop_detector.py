import re

def detect_loops(code):
    loops = []

    lines = code.split("\n")

    for line in lines:
        line = line.strip()

        # C / C++ / Java for loop
        if re.match(r"for\s*\(.*\)", line):
            loops.append({
                "type": "for",
                "line": line
            })

        # while loop (all languages)
        elif re.match(r"while\s*\(.*\)", line):
            loops.append({
                "type": "while",
                "line": line
            })

        # Python for loop
        elif re.match(r"for\s+.*in\s+.*:", line):
            loops.append({
                "type": "for",
                "line": line
            })

    return loops