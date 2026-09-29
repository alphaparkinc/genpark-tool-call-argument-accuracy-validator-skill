from client import ToolArgumentValidator

expected = {"symbol": "NVDA", "quantity": 100}
actual = {"symbol": "NVDA", "quantity": 100}

res = ToolArgumentValidator.validate_args(expected, actual)
print("Tool Argument Match Result:", res)
