# X (Twitter) XR 热门帖子自动抓取器

自动抓取 X (Twitter) 平台上关于 XR/VR/AR 的热门帖子，每天定时推送 Top 3。

## 功能特点

- 🔍 **智能搜索**: 自动搜索 XR、VR、AR、虚拟现实、增强现实、混合现实等相关话题
- 📊 **热度排序**: 基于浏览量、点赞数、转发数、回复数综合计算热度
- 📈 **详细数据**: 展示每条帖子的完整统计数据和链接
- ⏰ **定时推送**: 支持每天定时自动抓取，无需手动运行
- 💾 **结果保存**: 自动保存抓取结果到本地文件
- 🔐 **安全可靠**: 使用 twscrape 库，支持多账号，稳定可靠

## 技术方案

经过深入调研，本项目采用了目前最佳的 Twitter/X 抓取方案：

- **核心库**: [twscrape](https://github.com/vladkens/twscrape) - 2025 年最活跃维护的 Twitter 抓取库
- **优势**:
  - ✅ 支持授权登录，稳定性高
  - ✅ 可按热度(Top)排序搜索
  - ✅ 获取完整的帖子数据（浏览量、点赞、转发等）
  - ✅ 支持多账号池，避免限流
  - ✅ 开源免费

## 安装

### 1. 克隆仓库

```bash
git clone <仓库地址>
cd Test
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置环境变量（可选）

复制 `.env.example` 到 `.env` 并根据需要修改配置：

```bash
cp .env.example .env
```

可配置项：
- `DAILY_PUSH_TIME`: 每日推送时间（默认 09:00）
- `XR_KEYWORDS`: 搜索关键词（默认包含 XR, VR, AR 等）
- `TOP_POST_COUNT`: 抓取数量（默认 3）

## 使用方法

### 首次使用：设置账号

在首次使用前，需要添加至少一个 Twitter/X 账号：

```bash
python setup_accounts.py
```

按提示输入账号信息：
- 用户名
- 密码
- 邮箱
- 邮箱密码

> **注意**: 账号信息会加密保存在本地 `accounts.db` 文件中，请勿分享此文件。

### 方式一：手动运行

直接运行抓取脚本：

```bash
python xr_scraper.py
```

### 方式二：定时自动运行

启动定时任务服务：

```bash
python scheduler.py
```

程序会在每天设定的时间（默认 09:00）自动运行抓取任务。

### 方式三：使用 cron (Linux/Mac)

编辑 crontab：

```bash
crontab -e
```

添加定时任务（每天 9:00 运行）：

```
0 9 * * * cd /path/to/Test && python xr_scraper.py
```

## 输出示例

```
================================================================================
📊 X 平台 XR 热门帖子 TOP 3
⏰ 抓取时间: 2026-01-19 09:00:00
================================================================================

🏆 第 1 名
👤 作者: Meta Quest (@MetaQuestVR)
📅 发布时间: 2026-01-18 15:30:00

📝 内容:
   Introducing the all-new Quest 4 with unprecedented XR capabilities...

📈 数据统计:
   👁️  浏览量: 2,500,000
   ❤️  点赞数: 45,000
   🔄 转发数: 12,000
   💬 回复数: 3,500

🔗 链接: https://twitter.com/MetaQuestVR/status/1234567890
```

## 文件结构

```
Test/
├── xr_scraper.py           # 主抓取脚本
├── scheduler.py            # 定时任务调度器
├── setup_accounts.py       # 账号设置脚本
├── requirements.txt        # Python 依赖
├── .env.example           # 环境变量示例
├── .gitignore            # Git 忽略文件
├── README.md             # 说明文档
├── accounts.db           # 账号数据库（自动生成，勿提交）
└── output/               # 输出目录（自动生成）
    └── xr_top_posts_*.txt
```

## 常见问题

### Q: 为什么需要 Twitter/X 账号？

A: Twitter/X 在 2023 年取消了免费 API。目前最可靠的抓取方式是通过账号登录后进行数据抓取。twscrape 库会模拟真实用户行为，确保稳定性。

### Q: 账号安全吗？

A: 账号信息加密保存在本地 `accounts.db` 文件中，不会上传到任何服务器。建议使用小号进行抓取。

### Q: 多久抓取一次比较合适？

A: 建议每天抓取 1-2 次。过于频繁可能导致账号被限流。

### Q: 可以自定义搜索关键词吗？

A: 可以！修改 `.env` 文件中的 `XR_KEYWORDS` 变量，用逗号分隔多个关键词。

### Q: 如何获取更多帖子？

A: 修改 `.env` 文件中的 `TOP_POST_COUNT` 变量，或者直接修改 `xr_scraper.py` 中的 `top_count` 参数。

## 调研说明

在开发这个工具时，我调研了多个 Twitter/X 抓取方案：

### 商业 API 服务
- **ScrapFly**: 自动处理 guest tokens，提供 Python/TypeScript SDK
- **Scrapingdog**: 提供免费试用额度，有现成 Python 代码
- **Bright Data**: 专业数据采集平台，但价格较高
- **X Scraper API**: 支持多语言 SDK

### 开源库对比
- **twscrape** ✅: 2025 年最活跃维护，支持授权和热度排序（本项目采用）
- **tweepy**: 需要官方 API 密钥，免费版限制严格
- **twint**: 已停止维护，不再可用

## 技术栈

- **Python 3.7+**
- **twscrape**: Twitter 数据抓取
- **schedule**: 定时任务
- **python-dotenv**: 环境变量管理

## 参考资料

- [twscrape GitHub](https://github.com/vladkens/twscrape)
- [Best Twitter Scraper Tools 2026](https://www.scrapingdog.com/blog/best-twitter-scraper/)
- [How to Scrape Twitter in 2026](https://scrapfly.io/blog/posts/how-to-scrape-twitter)
- [XR Trends 2026](https://yordstudio.com/xr-trends-2026-the-future-of-ar-and-vr-for-business/)

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

---

**免责声明**: 本工具仅供学习和研究使用。使用时请遵守 Twitter/X 的服务条款和相关法律法规。
