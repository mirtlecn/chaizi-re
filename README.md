# 汉字拆字字典（修订）

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

源自开放词典的 chaizi 项目。原字典已经不再维护，且有缺字、缺少拆法等问题，故有此项目。

## 说明

`radical.yaml` 内每一行为某个汉字的一种拆法。一个汉字可能有多个拆法。

汉字 | 拆法 (一) | 拆法 (二) | 拆法 (三)
--- | -------- | -------- | --------
拆 | 手 斥 | 扌 斥 | 才 斥
字 | 宀 子
驠 | 馬 燕
鳢 | 鱼 豊
馦 | 香 兼
覗 | 司 見
馫 | 香 香 香
靐 | 雷 雷 雷

拆字时以容易打出来的字为先，然后尽量列出其余所有不同拆法，包括正确部首和部件（若包含于统一汉字表内）和异体字。

拆字字典可用于汉字教学、[输入法码表](https://github.com/mirtlecn/rime-radical-pinyin) 等方面。

## 参与

如果此字典对您有帮助，您可以在以下方面帮助完善本项目：

- 纠正拆字错误：字典有大量拆字错误，比如简体字按繁体字拆，格式错误，异体字标注错误……
- 添补漏字：项目内的 `缺字.yaml` 是比照 Unihan 数据得出的目前缺少的 20,000 多汉字……
- 规范拆字部件：汉字同一部首、部件有许多不同的写法，需要统一规范以方便机器处理……
- 您注意到的其他不足

本项目部分文件说明如下：

- `radical.yaml`: 拆字数据，每一行的格式如下
```yaml
<汉字><tab><部件甲><space><部件乙>……
```
- `叠字.yaml`：叠字数据，这些字在机器处理可能要特别注意（例如注音时其部件应当统一注同一个音，而不是随意组合）
- `缺字.yaml`：比照 Unihan 数据，得出的当前字库缺少的汉字
- `lint.py`: 一个 Python 脚本，用于排序、去重、规范写法。在本文件夹内，执行 `python lint.py` 即可。

## 修订记录

- 合并了繁简两份码表，合入了 [henrysting](https://github.com/henrysting/chaizi/) 的添补
- 加入了 200 多未收录的常用字，日常缺字补漏。
- 更正、添加了大量拆法
- 删除了编码不正确的汉字；

## Credit

原码表版权归属 ©开放词典，采用 [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/) 协议。

本仓库修订过的码表使用 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0) 协议。
