from src.benchmarking.benchmark import benchmark_gcc, benchmark_cpp, benchmark_java
from src.optimization.suggester import suggest_optimization
from src.analysis.dependency_analysis import is_vectorizable
from src.analysis.loop_detector import detect_loops

def analyze_code(code, file_path):
    from src.analysis.loop_detector import detect_loops
    from src.analysis.dependency_analysis import is_vectorizable
    from src.optimization.suggester import suggest_optimization
    from src.benchmarking.benchmark import benchmark_gcc, benchmark_cpp, benchmark_java

    # Detect language
    if file_path.endswith(".c"):
        language = "C"
    elif file_path.endswith(".cpp"):
        language = "C++"
    elif file_path.endswith(".java"):
        language = "Java"
    elif file_path.endswith(".py"):
        language = "Python"
    else:
        language = "Unknown"

    # Benchmark
    time_taken = None
    if language == "C":
        time_taken = benchmark_gcc(file_path)
    elif language == "C++":
        time_taken = benchmark_cpp(file_path)
    elif language == "Java":
        time_taken = benchmark_java(file_path)

    # Loop detection
    loops = detect_loops(code) or []

    results = []
    for loop in loops:
        vectorizable = is_vectorizable(loop)
        suggestions = suggest_optimization(loop, vectorizable)

        results.append({
            "type": loop["type"],
            "code": loop["line"],
            "vectorizable": vectorizable,
            "suggestions": suggestions
        })

    return {
        "language": language,
        "time": time_taken,
        "loops": results
    }

def detect_language(file_path):
    if file_path.endswith(".c"):
        return "C"
    elif file_path.endswith(".cpp"):
        return "C++"
    elif file_path.endswith(".java"):
        return "Java"
    elif file_path.endswith(".py"):
        return "Python"
    else:
        return "Unknown"
def main():
    # read your sample C file
    file_path = "data/input_code/Sample.java"

    language = detect_language(file_path)
    print("Language detected:", language)

    with open(file_path, "r") as f:
     code = f.read()

    if file_path.endswith(".c"):
     language = "C"
    elif file_path.endswith(".cpp"):
     language = "C++"
    elif file_path.endswith(".java"):
     language = "Java"
    elif file_path.endswith(".py"):
     language = "Python"
    else:
     language = "Unknown"

     

    loops = detect_loops(code)

    

# ✅ ADD THIS HERE
    print("\n--- Benchmarking ---")

    if language == "C":
     time_taken = benchmark_gcc(file_path)

    elif language == "C++":
     time_taken = benchmark_cpp(file_path)

    elif language == "Java":
     time_taken = benchmark_java(file_path)

    else:
     print("Benchmark not supported for", language)
     time_taken = None

    if time_taken is not None:
     print("Execution Time:", time_taken, "seconds")

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
    

if __name__ == "__main__":
    main()