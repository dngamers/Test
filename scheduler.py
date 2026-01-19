#!/usr/bin/env python3
"""
定时任务调度器
每天定时运行 XR 帖子抓取任务
"""

import asyncio
import schedule
import time
import os
from datetime import datetime
from dotenv import load_dotenv
from xr_scraper import XRScraper

# 加载环境变量
load_dotenv()


def run_scraper_sync():
    """同步包装器，用于 schedule 库调用"""
    print(f"\n{'='*80}")
    print(f"⏰ 定时任务触发 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*80}\n")

    asyncio.run(run_scraper())


async def run_scraper():
    """运行抓取器"""
    try:
        scraper = XRScraper()
        await scraper.run()
    except Exception as e:
        print(f"❌ 抓取失败: {e}")
        import traceback
        traceback.print_exc()


def main():
    """主函数"""
    # 获取推送时间设置
    push_time = os.getenv('DAILY_PUSH_TIME', '09:00')

    print("=" * 80)
    print("🤖 XR 热门帖子定时抓取服务")
    print("=" * 80)
    print(f"\n⏰ 定时设置: 每天 {push_time} 自动抓取")
    print(f"📊 当前时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("\n按 Ctrl+C 停止服务\n")
    print("-" * 80)

    # 设置定时任务
    schedule.every().day.at(push_time).do(run_scraper_sync)

    # 询问是否立即运行一次
    try:
        print("\n是否立即运行一次抓取? (按 Enter 立即运行，或输入 n 跳过): ", end='')
        response = input().strip().lower()

        if response != 'n':
            print("\n立即执行抓取任务...")
            run_scraper_sync()
    except KeyboardInterrupt:
        print("\n已取消")
        return

    print(f"\n✓ 定时任务已启动，等待下次运行时间 ({push_time})...")

    # 运行调度器
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # 每分钟检查一次
    except KeyboardInterrupt:
        print("\n\n👋 定时任务已停止")


if __name__ == "__main__":
    main()
