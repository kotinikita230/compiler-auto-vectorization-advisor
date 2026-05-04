from src.benchmarking.benchmark import benchmark_gcc
from src.optimization.suggester import suggest_optimization
from src.analysis.dependency_analysis import is_vectorizable
from src.analysis.loop_detector import detect_loops

def main():
    # read your sample C file
    with open("data/input_code/sample1.c", "r") as f:
        code = f.read()

    loops = detect_loops(code)

    if len(loops) == 0:
        print("No loops detected")
    else:
        print("Loops found:")
       
        for loop in loops:
          print("\nLoop detected: YES")
          print("Type:", loop["type"])
          print("Code:", loop["line"])

          vectorizable = is_vectorizable(loop)

          print("Vectorizable:", "YES" if vectorizable else "NO")

          suggestions = suggest_optimization(loop, vectorizable)

          print("Suggestions:")
          for s in suggestions:
           print("-", s)
print("\n--- Benchmarking GCC ---")
time_taken = benchmark_gcc("data/input_code/sample1.c")
print("Execution Time:", time_taken, "seconds")
if __name__ == "__main__":
    main()