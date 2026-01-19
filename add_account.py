#!/usr/bin/env python3
"""
简单的账号添加脚本
可以通过命令行参数直接添加账号
"""

import asyncio
import sys
from twscrape import API
from twscrape.logger import set_log_level


async def add_account(username, password, email, email_password):
    """添加账号"""
    api = API()
    set_log_level("INFO")

    try:
        # 添加账号
        print(f"⏳ 正在添加账号 {username}...")
        await api.pool.add_account(username, password, email, email_password)
        print(f"✓ 账号 {username} 添加成功!")

        # 尝试登录
        print(f"⏳ 正在登录账号 {username}...")
        await api.pool.login(username)
        print(f"✓ 账号 {username} 登录成功!")

        # 显示账号状态
        accounts = await api.pool.accounts_info()
        print(f"\n✅ 当前共有 {len(accounts)} 个账号")
        for acc in accounts:
            print(f"  - {acc.username} (状态: {acc.status})")

        return True

    except Exception as e:
        print(f"❌ 错误: {e}")
        return False


def print_usage():
    """打印使用说明"""
    print("使用方法:")
    print("  python3 add_account.py <用户名> <密码> <邮箱> <邮箱密码>")
    print("\n示例:")
    print("  python3 add_account.py myuser mypass my@email.com emailpass")
    print("\n或者运行交互式设置:")
    print("  python3 setup_accounts.py")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("❌ 参数数量不正确\n")
        print_usage()
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    email = sys.argv[3]
    email_password = sys.argv[4]

    print("=" * 80)
    print("Twitter/X 账号添加工具")
    print("=" * 80)
    print()

    success = asyncio.run(add_account(username, password, email, email_password))

    if success:
        print("\n🎉 账号设置完成！")
        print("\n你现在可以运行:")
        print("  python3 xr_scraper.py       # 立即抓取")
        print("  python3 scheduler.py        # 启动定时任务")
        sys.exit(0)
    else:
        print("\n❌ 账号设置失败")
        sys.exit(1)
