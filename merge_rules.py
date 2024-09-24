import requests

# 要合并的文件URL列表
file_urls = [
    ## proxy    
    {
        "category": "surge_onlyfan",
        "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/YouTube/YouTube.list"
    },
    {
        "category": "surge_onlyfan",
        "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/YouTubeMusic/YouTubeMusic.list"
    },
    {
        "category": "surge_onlyfan",
        "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Telegram/Telegram.list"
    },
    {
        "category": "surge_onlyfan",
        "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Google/Google.list"
    },
    {
        "category": "surge_onlyfan",
        "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/GitHub/GitHub.list"
    }, 
    {
        "category": "surge_onlyfan",
        "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Twitter/Twitter.list"
    },
    {
        "category": "surge_onlyfan",
        "url": "https://de.xinsichen.com/index.php/s/AkNbLaXqzyeQpws/download/hk.txt"
    },

    ## direct

    {
        "category": "surge_direct",
        "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/WeChat/WeChat.list"
    },    
    {
        "category": "surge_direct",
        "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Tencent/Tencent.list"
    },    
    {
        "category": "surge_direct",
        "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/XiaoHongShu/XiaoHongShu.list"
    },    
    {
        "category": "surge_direct",
        "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/XiaoMi/XiaoMi.list"
    },    
    {
        "category": "surge_direct",
        "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/AliPay/AliPay.list"
    }, 
    {
        "category": "surge_direct",
        "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Alibaba/Alibaba.list"
    },
    {
        "category": "surge_direct",
        "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/MeiTuan/MeiTuan.list"
    },
    {
        "category": "surge_direct",
        "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Weibo/Weibo.list"
    },
    {
        "category": "surge_direct",
        "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/JingDong/JingDong.list"
    },
    {
        "category": "surge_direct",
        "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/DingTalk/DingTalk.list"
    },
    {
        "category": "surge_direct",
        "url": "https://de.xinsichen.com/index.php/s/rsW7TY3E7tYY9cN/download/Douyin.txt"
    },
    {
        "category": "surge_direct",
        "url": "https://de.xinsichen.com/index.php/s/5gXQ8PbCXC7BYTo/download/Xianyu.txt"
    },
    {
        "category": "surge_direct",
        "url": "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/GaoDe/GaoDe.list"
    },
    {
        "category": "surge_direct",
        "url": "https://de.xinsichen.com/index.php/s/cq9JN4tMf9nJAKz/download/Others.txt"
    }

    # 可以在此添加更多的文件URL和对应的分类别
]

# 用于存储合并后的规则
merged_rules = {
    "surge_direct": set(),
    "surge_onlyfan": set(),
    "surge_us": set(),
    "surge_jp": set()
}

# 用于存储拉取失败的文件URL
failed_urls = []

# 遍历每个文件URL
for file_info in file_urls:
    category = file_info["category"]
    url = file_info["url"]
    
    try:
        # 发送HTTP GET请求获取文件内容
        response = requests.get(url)
        
        # 检查请求是否成功
        if response.status_code == 200:
            # 按行分割文件内容
            lines = response.text.split("\n")
            
            # 遍历每一行
            for line in lines:
                # 去除行首尾的空白字符
                line = line.strip()
                
                # 跳过注释行和空行
                if line.startswith("#") or line == "":
                    continue
                
                # 将规则添加到对应分类别的合并集合中
                merged_rules[category].add(line)
        else:
            # 将拉取失败的文件URL添加到失败列表中
            failed_urls.append(url)
            print(f"Failed to retrieve file: {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        # 处理请求异常
        failed_urls.append(url)
        print(f"Error occurred while retrieving file: {url}. Error: {str(e)}")

# 将合并后的规则按行输出到对应的文件中
for category, rules in merged_rules.items():
    file_name = f"{category}_list.txt"
    with open(file_name, "w") as file:
        file.write("\n".join(sorted(rules)))
    print(f"Merge completed for {category}. Output file: {file_name}")

# 输出拉取失败的文件URL列表
if failed_urls:
    print("Failed to retrieve the following files:")
    for url in failed_urls:
        print(url)
else:
    print("All files were successfully retrieved and merged.")
