"""
assert_stmt ::= "assert" expression1 ["," expression2]
"""
# turns to 
if __debug__:
    if not expression1:
        raise AssertionError(expression2)

# before the assert cond, there is an additional check for thr __debug__ global var 
# built in boolean flag that's true under normal circumstances and false if optimizaions are requested
"""
Pitfalls
introducing security risks and bugs
syntax quirk that makes it easy to write useless assertions
"""
# Don't use for data validation
"""
assertions can be globally disables with '-0 and -00' command line switches
as well as PYTHONOPTIMIZE and CPYTHON
can intro bugs and security holes > cause it will be compiled away
"""
PAGE 21
