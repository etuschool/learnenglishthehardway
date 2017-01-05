## mistakes.py

---

使用: `mistakes [today/yesterday/(number)/top]`

功能: 可以添加错题、查看错题统计。会在 `~/.learnenglishthehardway/` 目录下生成 `.mistakes` 文本文件用于保存错题记录。

参数:

(1) today/yesterday

列出今天/昨天的错题

(2) 数字

列出最近[数字]这么多天的错题

(3) top

列出最频繁的20个错误

错题本格式:

    Question type | Question | Correct answer | User input | Error count
    
    2 | what's your [name]? | name | age | 3
    1 | dream # 梦想 | dream | dreaming | 1
    3 | 2017 | 2017 | 2070 | 8