def suggest_optimization(loop, is_vectorizable):
    suggestions = []

    if is_vectorizable:
        suggestions.append("Use SIMD vectorization")
        suggestions.append("Apply loop unrolling")
    else:
        suggestions.append("Cannot vectorize due to dependencies")

    return suggestions