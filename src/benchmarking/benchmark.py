import subprocess
import time
import os

def benchmark_gcc(file_path):
    exe_file = "a.exe"

    # Compile
    compile_process = subprocess.run(
    ["gcc", file_path, "-std=c99", "-O2", "-o", exe_file],
    capture_output=True,
    text=True
)

    # 🔴 Check if compile failed
    if compile_process.returncode != 0:
        print("Compilation Error:")
        print(compile_process.stderr)
        return None

    # 🔴 Check if exe exists
    if not os.path.exists(exe_file):
        print("Executable not created")
        return None

    # Run and measure time
    start = time.time()
    subprocess.run([exe_file])
    end = time.time()

    return end - start