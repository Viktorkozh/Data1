#!/usr/bin/env python3
# coding: utf-8 -*-

import os
import shutil

source_folder = "Data1\\doc"
source_file = "Лр 1 Кожуховский.docx"

if __name__ == "__main__":
    os.chdir("C:\\Users\\viktor\\Desktop\\cкфу\\DataAnalysis")

    for i in range(2, 8):
        target_folder = f"Data{i}\\doc"
        os.makedirs(target_folder, exist_ok=True)
        target_file = f"Лр {i} Кожуховский.docx"
        source_path = os.path.join(source_folder, source_file)
        target_path = os.path.join(target_folder, target_file)
        shutil.copy2(source_path, target_path)
