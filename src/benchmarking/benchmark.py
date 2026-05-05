import subprocess
import time
import os


# ----------- C -----------
def benchmark_gcc(file_path):
    exe_file = "a.exe"

    # Compile
    compile = subprocess.run(
        ["gcc", file_path, "-o", exe_file],
        capture_output=True,
        text=True
    )

    if compile.returncode != 0:
        return None, compile.stderr

    # Execute
    start = time.time()
    run = subprocess.run(
        [exe_file],
        capture_output=True,
        text=True
    )
    end = time.time()

    return end - start, run.stdout


# ----------- C++ -----------
def benchmark_cpp(file_path):
    exe_file = "a.exe"

    compile = subprocess.run(
        ["g++", file_path, "-o", exe_file],
        capture_output=True,
        text=True
    )

    if compile.returncode != 0:
        return None, compile.stderr

    start = time.time()
    run = subprocess.run(
        [exe_file],
        capture_output=True,
        text=True
    )
    end = time.time()

    return end - start, run.stdout


# ----------- Java -----------
def benchmark_java(file_path):
    dir_path = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)
    class_name = file_name.replace(".java", "")

    # Compile
    compile = subprocess.run(
        ["javac", file_path],
        capture_output=True,
        text=True
    )

    if compile.returncode != 0:
        return None, compile.stderr

    # Run
    start = time.time()
    run = subprocess.run(
        ["java", "-cp", dir_path, class_name],
        capture_output=True,
        text=True
    )
    end = time.time()

    return end - start, run.stdout

def benchmark_python(file_path):
    import subprocess, time

    start = time.time()
    run = subprocess.run(
        ["python", file_path],
        capture_output=True,
        text=True
    )
    end = time.time()

    return end - start, run.stdout if run.returncode == 0 else run.stderr