# Windows 使用指南

## 🚀 快速开始（3 分钟搞定）

### 准备工作

1. **确保已安装 Python**
   - 按 `Win + R`，输入 `cmd`，按回车
   - 在命令提示符中输入：`python --version`
   - 如果显示版本号（如 Python 3.8.x），说明已安装 ✓
   - 如果提示找不到命令，需要先安装 Python（见下方"安装 Python"部分）

### 方式一：使用批处理脚本（最简单）

1. **下载项目代码**
   - 访问你的 GitHub 仓库
   - 点击绿色的 "Code" 按钮
   - 选择 "Download ZIP"
   - 解压到任意位置（如 `C:\Users\你的用户名\Desktop\Test`）

2. **双击运行 `windows_setup.bat`**
   - 找到解压后的文件夹
   - 双击 `windows_setup.bat` 文件
   - 按提示输入你的 Twitter 账号信息
   - 等待安装完成

3. **双击运行 `run.bat`**
   - 双击 `run.bat` 文件
   - 程序会自动抓取 XR 热门帖子
   - 结果会显示在窗口中，并保存到 `output` 文件夹

完成！就这么简单！

---

### 方式二：使用命令行（手动操作）

1. **打开命令提示符**
   - 按 `Win + R`
   - 输入 `cmd`
   - 按回车

2. **进入项目目录**
   ```cmd
   cd C:\Users\你的用户名\Desktop\Test
   ```
   （替换为你实际解压的路径）

3. **安装依赖**
   ```cmd
   pip install -r requirements.txt
   ```

4. **添加 Twitter 账号**
   ```cmd
   python add_account.py dngamer65429 HUMANGAME1 dngamer@gmail.com HUMANGAME1
   ```

5. **运行抓取**
   ```cmd
   python xr_scraper.py
   ```

---

## 🔧 安装 Python（如果还没安装）

### 第 1 步：下载 Python

1. 访问 https://www.python.org/downloads/
2. 点击 "Download Python 3.x.x"（最新版本）
3. 下载完成后运行安装程序

### 第 2 步：安装 Python

**重要**：安装时必须勾选 "Add Python to PATH"！

1. 运行下载的安装程序
2. ✅ **勾选** "Add Python to PATH"（这一步很重要！）
3. 点击 "Install Now"
4. 等待安装完成

### 第 3 步：验证安装

1. 按 `Win + R`，输入 `cmd`，按回车
2. 输入：`python --version`
3. 如果显示版本号，说明安装成功 ✓

---

## 📂 项目文件说明

下载并解压后，你会看到这些文件：

```
Test/
├── windows_setup.bat       ← 双击这个！Windows 一键安装
├── run.bat                 ← 双击这个！运行抓取程序
├── xr_scraper.py          - 主抓取脚本
├── scheduler.py           - 定时任务
├── add_account.py         - 添加账号工具
├── realistic_demo.py      - 演示程序（无需账号）
├── requirements.txt       - 依赖列表
├── .env.example          - 配置模板
└── README.md             - 项目说明
```

---

## 🎯 常用命令（在 cmd 中运行）

### 立即抓取 XR 热门帖子
```cmd
python xr_scraper.py
```

### 启动每日定时任务
```cmd
python scheduler.py
```

### 查看演示效果（无需账号）
```cmd
python realistic_demo.py
```

### 添加额外的 Twitter 账号
```cmd
python add_account.py 用户名 密码 邮箱 邮箱密码
```

---

## ⏰ 设置 Windows 定时任务

如果想让程序每天自动运行：

### 方式 1：使用 scheduler.py（推荐）

1. 打开 cmd
2. 进入项目目录
3. 运行：`python scheduler.py`
4. 保持窗口开启（不要关闭）
5. 程序会在每天早上 9:00 自动运行

### 方式 2：使用 Windows 任务计划程序

1. 按 `Win + R`，输入 `taskschd.msc`，按回车
2. 点击右侧 "创建基本任务"
3. 名称：XR 帖子抓取器
4. 触发器：每日，设置时间（如 09:00）
5. 操作：启动程序
   - 程序或脚本：`C:\path\to\python.exe`
   - 添加参数：`xr_scraper.py`
   - 起始于：`C:\Users\你的用户名\Desktop\Test`
6. 完成

---

## ❓ 常见问题

### Q: 双击 .bat 文件一闪而过？

**A:** 右键点击 .bat 文件，选择"编辑"，检查是否有错误提示。或者：
1. 按 `Win + R`
2. 输入 `cmd`
3. 拖动 .bat 文件到命令提示符窗口
4. 按回车，就能看到错误信息

### Q: 提示 "python 不是内部或外部命令"？

**A:** Python 未正确安装或未添加到 PATH。解决方案：
1. 重新安装 Python
2. 安装时**务必勾选** "Add Python to PATH"
3. 或者使用完整路径：`C:\Python39\python.exe xr_scraper.py`

### Q: pip install 很慢？

**A:** 使用国内镜像源：
```cmd
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Q: 提示 "No module named 'xxx'"？

**A:** 依赖未安装完整，重新运行：
```cmd
pip install -r requirements.txt
```

### Q: 网络连接失败？

**A:**
1. 检查是否能访问 Twitter：在浏览器打开 https://twitter.com
2. 如果不能访问，可能需要配置代理
3. 或者在能访问 Twitter 的网络环境中运行

### Q: 账号登录失败？

**A:**
1. 检查用户名、密码是否正确
2. 确保邮箱和邮箱密码正确
3. Twitter 账号是否正常（未被封禁）
4. 可以尝试换一个账号

### Q: 如何查看结果？

**A:**
- 结果会在命令窗口中显示
- 同时自动保存到 `output` 文件夹
- 用记事本或任何文本编辑器打开 `.txt` 文件

### Q: 如何修改抓取时间？

**A:**
1. 用记事本打开 `.env` 文件
2. 修改 `DAILY_PUSH_TIME=09:00` 为你想要的时间
3. 保存文件

### Q: 如何修改抓取数量？

**A:**
1. 用记事本打开 `.env` 文件
2. 修改 `TOP_POST_COUNT=3` 为你想要的数量（如 5、10）
3. 保存文件

---

## 🎨 自定义配置

编辑 `.env` 文件（用记事本打开）：

```
# 每日推送时间（24小时制）
DAILY_PUSH_TIME=09:00

# 搜索关键词（逗号分隔）
XR_KEYWORDS=XR,VR,AR,virtual reality,augmented reality,mixed reality,Quest,Vision Pro

# 抓取数量
TOP_POST_COUNT=3
```

---

## 📊 查看结果

### 在命令窗口中查看
程序运行后会直接在窗口中显示结果

### 查看保存的文件
1. 打开项目文件夹
2. 进入 `output` 文件夹
3. 找到最新的 `.txt` 文件
4. 双击打开（用记事本）

---

## 🔄 更新项目

如果项目有更新：

1. 删除旧的文件夹
2. 重新下载 ZIP
3. 解压到相同位置
4. 重新运行 `windows_setup.bat`

或者如果使用 Git：
```cmd
cd C:\Users\你的用户名\Desktop\Test
git pull
```

---

## 💡 使用技巧

### 创建桌面快捷方式

1. 右键点击 `run.bat`
2. 选择"发送到" → "桌面快捷方式"
3. 以后只需双击桌面图标即可运行

### 开机自动运行

1. 按 `Win + R`，输入 `shell:startup`
2. 将 `run.bat` 的快捷方式复制到打开的文件夹
3. 重启电脑后会自动运行

---

## 📞 需要帮助？

如果遇到问题：
1. 查看上方的"常见问题"部分
2. 查看项目的 README.md 文件
3. 查看 USAGE_GUIDE.md 文件
4. 在 GitHub 提交 Issue

---

**祝使用愉快！🎉**
