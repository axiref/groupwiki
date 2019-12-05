# Groupwiki

适用于Telegram群的维基百科搜索机器人

# 安装

```bash
pip install -r requirements.txt
cp config.example.py config.py
```

修改`config.py`中的`TOKEN`字段为你的机器人的Token

然后运行机器人:

```bash
python bot.py
```

另外，你可以透过`pm2`来守护本进程，只需在专案目录执行:

```bash
pm2 start
```

即可看到一个名为`groupwiki`的任务

## License
[MIT](https://choosealicense.com/licenses/mit/)