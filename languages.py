# coding=utf-8
from __future__ import unicode_literals

c_lang_config = {
    "name": "c",
    "compile": {
        "src_name": "main.c",
        "exe_name": "main",
        "max_cpu_time": 3000,
        "max_real_time": 5000,
        "max_memory": 128 * 1024 * 1024,
        "compile_command": "/usr/bin/gcc -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c99 -static {src_path} -lm -o {exe_path}",
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": "c_cpp",
        "max_process_number": 5
    }
}


c_lang_spj_config = {
    "src_name": "spj-{spj_version}.c",
    "exe_name": "spj-{spj_version}",
    "max_cpu_time": 10000,
    "max_real_time": 20000,
    "max_memory": 1024 * 1024 * 1024,
    "compile_command": "/usr/bin/gcc -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c99 {src_path} -lm -o {exe_path}",
    # server should replace to real info
    "version": "1",
    "src": ""
}


cpp_lang_config = {
    "name": "cpp",
    "compile": {
        "src_name": "main.cpp",
        "exe_name": "main",
        "max_cpu_time": 3000,
        "max_real_time": 5000,
        "max_memory": 128 * 1024 * 1024,
        "compile_command": "/usr/bin/g++ -DONLINE_JUDGE -O2 -w -fmax-errors=3 -std=c++11 {src_path} -lm -o {exe_path}",
    },
    "run": {
        "command": "{exe_path}",
        "seccomp_rule": "c_cpp",
        "max_process_number": 5
    }
}


java_lang_config = {
    "name": "java",
    "compile": {
        "src_name": "Main.java",
        "exe_name": "Main",
        "max_cpu_time": 3000,
        "max_real_time": 5000,
        "max_memory": -1,
        "compile_command": "/usr/bin/javac {src_path} -d {exe_dir} -encoding UTF8"
    },
    "run": {
        "command": "/usr/bin/java -cp {exe_dir} -Xss1M -XX:MaxPermSize=16M -XX:PermSize=8M -Xms16M -Xmx{max_memory}k -Djava.security.manager -Djava.security.policy==/etc/java_policy -Djava.awt.headless=true Main",
        "seccomp_rule": None,
        "max_process_number": -1
    }
}