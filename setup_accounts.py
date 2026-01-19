#!/usr/bin/env python3
"""
账号设置脚本
用于添加和管理 Twitter/X 账号
"""

import asyncio
from twscrape import API
from twscrape.logger import set_log_level


async def setup_accounts():
    """设置账号"""
    api = API()
    set_log_level("INFO")

    print("=" * 80)
    print("Twitter/X 账号设置")
    print("=" * 80)
    print()
    print("说明: 需要添加至少一个 Twitter/X 账号来进行数据抓取")
    print("注意: 账号信息将加密保存在本地 accounts.db 文件中")
    print()

    # 检查现有账号
    existing_accounts = await api.pool.accounts_info()
    if existing_accounts:
        print(f"✓ 当前已有 {len(existing_accounts)} 个账号:")
        for acc in existing_accounts:
            print(f"  - {acc.username} (状态: {acc.status})")
        print()

        choice = input("是否要添加更多账号? (y/n): ").lower()
        if choice != 'y':
            print("\n设置已取消")
            return

    # 添加账号
    print("\n请输入 Twitter/X 账号信息:")
    print("提示: 可以添加多个账号以提高抓取速度和稳定性")
    print()

    while True:
        username = input("用户名: ").strip()
        password = input("密码: ").strip()
        email = input("邮箱: ").strip()
        email_password = input("邮箱密码: ").strip()

        if not all([username, password, email, email_password]):
            print("❌ 所有字段都是必填的!")
            continue

        try:
            # 添加账号
            await api.pool.add_account(username, password, email, email_password)
            print(f"✓ 账号 {username} 添加成功!")

            # 尝试登录
            print(f"⏳ 正在登录账号 {username}...")
            await api.pool.login(username)
            print(f"✓ 账号 {username} 登录成功!")

        except Exception as e:
            print(f"❌ 添加账号失败: {e}")

        # 询问是否继续添加
        more = input("\n是否继续添加账号? (y/n): ").lower()
        if more != 'y':
            break

    # 显示最终账号列表
    print("\n" + "=" * 80)
    print("账号设置完成")
    print("=" * 80)

    final_accounts = await api.pool.accounts_info()
    print(f"\n总共 {len(final_accounts)} 个账号:")
    for acc in final_accounts:
        print(f"  ✓ {acc.username} (状态: {acc.status})")

    print("\n你现在可以运行: python xr_scraper.py 来抓取帖子")


if __name__ == "__main__":
    asyncio.run(setup_accounts())
