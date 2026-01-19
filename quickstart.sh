#!/bin/bash

# XR 热门帖子抓取器 - 快速开始脚本

echo "=================================="
echo "XR 热门帖子抓取器 - 快速开始"
echo "=================================="
echo ""

# 检查 Python 版本
if ! command -v python3 &> /dev/null; then
    echo "❌ 未找到 Python3，请先安装 Python 3.7 或更高版本"
    exit 1
fi

echo "✓ Python 版本: $(python3 --version)"
echo ""

# 安装依赖
echo "📦 安装 Python 依赖..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ 依赖安装失败"
    exit 1
fi

echo "✓ 依赖安装完成"
echo ""

# 创建 .env 文件
if [ ! -f .env ]; then
    echo "📝 创建配置文件..."
    cp .env.example .env
    echo "✓ 已创建 .env 文件，你可以根据需要修改配置"
    echo ""
fi

# 设置账号
echo "🔐 接下来需要设置 Twitter/X 账号"
echo "按 Enter 继续，或按 Ctrl+C 取消..."
read

python3 setup_accounts.py

if [ $? -ne 0 ]; then
    echo "❌ 账号设置失败"
    exit 1
fi

echo ""
echo "=================================="
echo "✅ 设置完成！"
echo "=================================="
echo ""
echo "你现在可以："
echo "  1. 手动运行抓取: python3 xr_scraper.py"
echo "  2. 启动定时任务: python3 scheduler.py"
echo ""
