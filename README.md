# repositories-sortby-start
Get Repositories and sort by starts

新增本地环境变量文件 `.env`
并配置`Github` `OAuth App`的授权信息
> [Creating an OAuth App](https://docs.github.com/en/developers/apps/creating-an-oauth-app)
```env
client_id=xxxxx
client_secret=xxxxx
```
使用
```shell
python main.py
```
或者
```shell
# 增加执行权限
chmod +x ./main.py
# 执行
./mian.py
```