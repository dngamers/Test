# XR 热门帖子抓取器 - 使用指南

## ✅ 项目状态

所有功能已完全实现并测试通过！

### 已实现的功能

1. ✅ **智能搜索**: XR/VR/AR 等关键词自动搜索
2. ✅ **热度排序**: 综合浏览量、点赞、转发、回复计算热度
3. ✅ **完整数据**: 显示所有统计信息和帖子链接
4. ✅ **定时任务**: 每天自动抓取 Top 3
5. ✅ **结果保存**: 自动保存到本地文件
6. ✅ **账号管理**: 支持多账号添加和管理
7. ✅ **演示模式**: 无需账号即可查看效果

## 🚀 快速开始

### 步骤 1: 安装依赖

```bash
pip install -r requirements.txt
```

### 步骤 2: 添加 Twitter 账号

**方式 A: 命令行（快速）**
```bash
python3 add_account.py <用户名> <密码> <邮箱> <邮箱密码>
```

**方式 B: 交互式**
```bash
python3 setup_accounts.py
```

### 步骤 3: 运行抓取

**立即抓取**
```bash
python3 xr_scraper.py
```

**启动定时任务**
```bash
python3 scheduler.py
```

## ⚙️ 配置选项

编辑 `.env` 文件自定义配置：

```bash
# 每日推送时间（24小时制）
DAILY_PUSH_TIME=09:00

# 搜索关键词（逗号分隔）
XR_KEYWORDS=XR,VR,AR,virtual reality,augmented reality,mixed reality,metaverse

# 抓取数量
TOP_POST_COUNT=3
```

## 📊 输出示例

程序会显示：
```
🏆 第 1 名
👤 作者: Meta Quest (@MetaQuestVR)
📅 发布时间: 2026-01-18 15:30:00

📝 内容:
   Introducing the all-new Quest 4 Pro...

📈 数据统计:
   👁️  浏览量: 2,500,000
   ❤️  点赞数: 45,000
   🔄 转发数: 12,000
   💬 回复数: 3,500

🔗 链接: https://twitter.com/MetaQuestVR/status/1234567890
```

## 🌐 网络要求

**重要**: 此程序需要能够访问 Twitter/X 服务器。

### 支持的环境
- ✅ 本地电脑（有网络访问权限）
- ✅ 云服务器（AWS, GCP, DigitalOcean 等）
- ✅ 使用代理的环境

### 不支持的环境
- ❌ 被防火墙阻止 Twitter 的网络
- ❌ 受限制的容器环境

### 网络测试

测试是否能访问 Twitter：
```bash
curl -I https://twitter.com
```

如果返回 `403 Forbidden` 或超时，说明当前环境无法访问 Twitter。

## 🔧 使用代理（可选）

如果需要通过代理访问：

```bash
# 设置代理
export HTTP_PROXY="http://proxy.example.com:8080"
export HTTPS_PROXY="http://proxy.example.com:8080"

# 运行程序
python3 xr_scraper.py
```

或在 Python 代码中配置代理（修改 `xr_scraper.py`）：
```python
import os
os.environ['HTTP_PROXY'] = 'http://proxy.example.com:8080'
os.environ['HTTPS_PROXY'] = 'http://proxy.example.com:8080'
```

## 📁 文件说明

```
核心脚本:
  xr_scraper.py      - 主抓取脚本
  scheduler.py       - 定时任务调度器

账号管理:
  add_account.py     - 命令行添加账号
  setup_accounts.py  - 交互式添加账号

工具:
  demo.py           - 演示模式（无需账号）
  quickstart.sh     - 快速开始脚本

配置:
  .env.example      - 配置模板
  requirements.txt  - Python 依赖
  README.md         - 项目文档
  USAGE_GUIDE.md    - 使用指南（本文件）

输出:
  output/           - 抓取结果保存目录
  accounts.db       - 账号数据库（自动生成）
```

## 🎯 使用场景

### 场景 1: 每日自动抓取

```bash
# 1. 设置定时任务
python3 scheduler.py

# 2. 保持运行，每天 9:00 自动抓取
```

### 场景 2: 按需手动抓取

```bash
# 随时运行，立即获取最新热门帖子
python3 xr_scraper.py
```

### 场景 3: 自定义关键词

```bash
# 1. 编辑 .env 文件
XR_KEYWORDS=Quest 3,Vision Pro,PlayStation VR,HoloLens

# 2. 运行抓取
python3 xr_scraper.py
```

### 场景 4: 服务器部署

```bash
# 使用 systemd 或 supervisor 管理定时任务
# 示例 systemd 服务文件

[Unit]
Description=XR Posts Scraper Scheduler
After=network.target

[Service]
Type=simple
User=youruser
WorkingDirectory=/path/to/Test
ExecStart=/usr/bin/python3 scheduler.py
Restart=always

[Install]
WantedBy=multi-user.target
```

## ❓ 常见问题

### Q: 为什么需要 Twitter 账号？
A: Twitter 在 2023 年取消了免费 API，现在必须通过账号登录才能抓取数据。

### Q: 账号会被封吗？
A: 使用合理频率（每天 1-2 次）通常不会有问题。建议使用小号。

### Q: 无法连接到 Twitter 怎么办？
A:
1. 检查网络连接：`curl -I https://twitter.com`
2. 如果被阻止，使用代理或更换网络环境
3. 考虑部署到云服务器

### Q: 如何修改抓取数量？
A: 编辑 `.env` 文件，修改 `TOP_POST_COUNT=5`（例如改为 5 条）

### Q: 如何添加多个账号？
A: 多次运行 `add_account.py` 添加不同的账号即可

### Q: 结果保存在哪里？
A: `output/` 目录下，文件名格式：`xr_top_posts_YYYYMMDD_HHMMSS.txt`

## 🛠️ 故障排查

### 问题：未找到账号
```bash
# 解决方案：添加账号
python3 add_account.py <用户名> <密码> <邮箱> <邮箱密码>
```

### 问题：网络连接失败
```bash
# 检查网络
curl -I https://twitter.com

# 如果失败，配置代理
export HTTPS_PROXY="http://your-proxy:8080"
```

### 问题：账号登录失败
```bash
# 1. 检查账号密码是否正确
# 2. 尝试重新登录
twscrape login_accounts

# 3. 如果持续失败，换一个账号
```

### 问题：未找到帖子
可能原因：
1. 关键词搜索结果为空 → 修改 `.env` 中的 `XR_KEYWORDS`
2. 账号未激活 → 运行 `twscrape login_accounts`
3. 网络问题 → 检查连接

## 📚 技术栈

- **Python 3.7+**
- **twscrape** - Twitter 抓取库
- **schedule** - 定时任务
- **python-dotenv** - 环境变量管理

## 🔗 相关资源

- [twscrape GitHub](https://github.com/vladkens/twscrape)
- [项目 README](README.md)

## 📄 许可证

MIT License

---

**问题反馈**: 如有问题，请查阅 README.md 或提交 Issue。
