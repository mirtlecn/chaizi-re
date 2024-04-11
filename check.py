import opencc

# 初始化 OpenCC
converter_tw = opencc.OpenCC('s2twp.json')  # 简体转台湾繁体
converter_hk = opencc.OpenCC('s2hk.json')   # 简体转香港繁体
converter_cn = opencc.OpenCC('t2s.json')    # 台湾繁体转简体
converter_t = opencc.OpenCC('s2t.json')    # 台湾繁体转简体

# 读取 radical.yaml 文件
with open('radical.yaml', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 打开 temp.txt 文件准备写入
with open('temp.txt', 'w', encoding='utf-8') as temp_file:
    for line in lines:
        # 取第一个字符（汉字）
        first_char = line[0]
        
        # 使用 OpenCC 将第一个字符转换为台湾繁体、香港繁体和简体
        tw_char = converter_tw.convert(first_char)
        hk_char = converter_hk.convert(first_char)
        cn_char = converter_cn.convert(first_char)
        t_char = converter_t.convert(first_char)
        
        # 如果这一行的最后一个字和第一个字符，或者其转换后的台湾繁体、简体、香港繁体相同，则输出到 temp.txt
        if line[-2] in (first_char, tw_char, hk_char, cn_char, t_char):
            temp_file.write(line)

print("处理完成，已将符合条件的行写入到 temp.txt 文件中。")
