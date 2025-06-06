IMPORT_HELPER = {
    "python": [
        "import math",
        "import re",
        "import sys",
        "import copy",
        "import datetime",
        "import itertools",
        "import collections",
        "import heapq",
        "import statistics",
        "import functools",
        "import hashlib",
        "import numpy",
        "import numpy as np",
        "import string",
        "from typing import *",
        "from collections import *",
    ],
    "cpp": [
        "using namespace std;",
        "#include<optional>",
        "#include<cassert>",
        "#include<stdlib.h>",
        "#include<algorithm>",
        "#include<cmath>",
        "#include<math.h>",
        "#include<numeric>",
        "#include<stdio.h>",
        "#include<vector>",
        "#include<set>",
        "#include<map>",
        "#include<queue>",
        "#include<stack>",
        "#include<list>",
        "#include<deque>",
        "#include<boost/any.hpp>",
        "#include<string>",
        "#include<climits>",
        "#include<cstring>",
        "#include<iostream>",
        "#include<sstream>",
        "#include<fstream>",
    ],
    "java": [
        "import java.util.*;",
        "import java.lang.reflect.*;",
        "import org.javatuples.*;",
        "import java.security.*;",
        "import java.math.*;",
        "import java.io.*;",
        "import java.util.stream.*;",
    ],
    "csharp": [
        "using System;",
        "using System.Numerics;",
        "using System.Diagnostics;",
        "using System.Collections.Generic;",
        "using System.Linq;",
        "using System.Text;",
        "using System.Security.Cryptography;",
        "using System.Collections.Generic;",
    ],
    "go": ["import (\"fmt\")"],
    "d": ["import std.array;", "import std.algorithm;"]
}

END_TOKENS = {
    'julia': ['\nend'],
    'lua': ['\nend'],
    'ruby': ['\nend'],
    'cpp': ['\n}'],
    'csharp': ['\n}'],
    'typescript': ['\n}'],
    'perl': ['\n}'],
    'r': ['\n}'],
    'd': ['\n}'],
    'go': ['\n}'],
    'js': ['\n}'],
    'php': ['\n}'],
}
