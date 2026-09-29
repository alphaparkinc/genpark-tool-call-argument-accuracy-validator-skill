"""Tool Call Argument Accuracy Validator.
100% Python Standard Library.
"""

class ToolArgumentValidator:
    """Validates presence and fidelity of agent tool arguments against expected schemas."""
    @staticmethod
    def validate_args(expected_args, actual_args):
        total_keys = set(expected_args.keys()).union(actual_args.keys())
        matches = 0
        errors = []
        for k in total_keys:
            if k not in actual_args:
                errors.append(f"Missing argument: {k}")
            elif k not in expected_args:
                errors.append(f"Unexpected extra argument: {k}")
            elif expected_args[k] == actual_args[k]:
                matches += 1
            else:
                errors.append(f"Argument '{k}' value mismatch: expected {expected_args[k]}, got {actual_args[k]}")
        accuracy = matches / max(len(total_keys), 1)
        return {
            "accuracy": round(accuracy, 4),
            "passed": accuracy == 1.0,
            "errors": errors
        }
