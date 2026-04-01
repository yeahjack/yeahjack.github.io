require "rbconfig"

# Some local Ruby builds on macOS expose CXX as "false", which breaks
# native gems with C++ sources such as eventmachine.
RbConfig::CONFIG["CXX"] = "clang++"
RbConfig::MAKEFILE_CONFIG["CXX"] = "clang++"
RbConfig::CONFIG["LDSHAREDXX"] = "clang++ -dynamic -bundle"
RbConfig::MAKEFILE_CONFIG["LDSHAREDXX"] = "clang++ -dynamic -bundle"
RbConfig::CONFIG["LDSHARED"] = "clang++ -dynamic -bundle"
RbConfig::MAKEFILE_CONFIG["LDSHARED"] = "clang++ -dynamic -bundle"
