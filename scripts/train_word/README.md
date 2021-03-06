## train_word.py

---

使用: `train_word <list_path>`

功能: 训练用户掌握词汇表里的所有单词

词汇表格式:

(1) 单词 + 解释

	dream # 梦想

(2) 包含在句子中的单词(用[]指定) + 解释
	
	what's your [name]? # 你叫什么名字?

训练方式:

(1) 纯单词

	假设需要训练的单词为: dream # 梦想
    >> (系统朗读单词), 请输入你听到的单词, 输 # 重听; 输 ? 获得更多提示.
    >> ding
    >> 错误，提示: [梦想]
    >> dreaming
    >> 错误, 提示: [ 给出 dream 的完整解释 ]
    >> dreamer
    >> 错误, 正确答案为 [ dream ]
    >> dream
    >> 棒棒哒！下一个～
    

(2) 句子中的单词

	假设需要训练的单词为: what's your [name]? # 你叫什么名字?
    >> (系统朗读单词), 请填入你听到的单词, 输 # 重听; 输 ? 获得更多提示.
    >> what's your ______ ?
    >> age
    >> 错误，提示: 你叫什么名字?
    >> size
    >> 错误, 正确答案为 [ name ]
    >> name
    >> 棒棒哒！下一个～

错题记录:

用户如果出错了，需要将错误记录到 [scripts/mistakes]() , 方便以后复习