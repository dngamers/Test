@echo off
chcp 65001 >nul
echo ================================================================================
echo XR 热门帖子抓取器 - Windows 快速安装
echo ================================================================================
echo.

:: 检查 Python
echo [1/4] 检查 Python 安装...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 未检测到 Python，请先安装 Python 3.7+
    echo    下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)
python --version
echo ✓ Python 已安装
echo.

:: 安装依赖
echo [2/4] 安装 Python 依赖包...
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ 依赖安装失败
    pause
    exit /b 1
)
echo ✓ 依赖安装完成
echo.

:: 创建配置文件
echo [3/4] 创建配置文件...
if not exist .env (
    copy .env.example .env >nul 2>&1
    echo ✓ 已创建 .env 配置文件
) else (
    echo ✓ .env 配置文件已存在
)
echo.

:: 提示添加账号
echo [4/4] 添加 Twitter 账号
echo.
echo 请输入你的 Twitter 账号信息：
set /p username="Twitter 用户名: "
set /p password="Twitter 密码: "
set /p email="邮箱: "
set /p email_password="邮箱密码: "

echo.
echo 正在添加账号...
python add_account.py %username% %password% %email% %email_password%

if %errorlevel% neq 0 (
    echo.
    echo ⚠️  账号添加可能遇到问题，但可以稍后重试
)

echo.
echo ================================================================================
echo ✅ 设置完成！
echo ================================================================================
echo.
echo 你现在可以运行：
echo   • python xr_scraper.py        立即抓取 XR 热门帖子
echo   • python scheduler.py         启动每日定时任务
echo   • python realistic_demo.py    查看演示效果
echo.
pause
