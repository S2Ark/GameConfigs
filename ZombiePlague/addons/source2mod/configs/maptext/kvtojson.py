import json
import os
from valve_keyvalues_python.keyvalues import KeyValues # https://github.com/gorgitko/valve-keyvalues-python

def convert_cfg_files(directory):
    # 遍历指定目录及其子目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 检查文件扩展名是否为 .cfg
            if file.endswith(".cfg"):
                file_path = os.path.join(root, file)
                j = {}
                kv = KeyValues(filename=file_path)
                if 'ConsoleMessage' in kv:
                    for k in kv["ConsoleMessage"].keys():
                        if 'default' in kv["ConsoleMessage"][k]:
                            s = {}
                            s["chi"] = kv["ConsoleMessage"][k]["default"]
                            j[k] = s
                
                    print(j)

                    out_path = file_path.replace(".cfg", ".jsonc")
                    with open(out_path, "w", encoding='utf-8') as f:
                        json.dump(j, f, indent=4, ensure_ascii=False)

# 指定你的源文件目录
source_directory = r"E:/GOCommunity-ZEConfigs/console-mannager"
convert_cfg_files(source_directory)