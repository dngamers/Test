#!/usr/bin/env python3
"""
演示脚本 - 展示程序功能（不需要真实账号）
"""

from datetime import datetime, timedelta
import random


def generate_demo_posts():
    """生成演示数据"""
    demo_posts = [
        {
            'id': '1234567890123456789',
            'author': 'MetaQuestVR',
            'author_name': 'Meta Quest',
            'text': 'Introducing the all-new Quest 4 Pro with unprecedented XR capabilities! Revolutionary passthrough technology and enhanced eye tracking make this our most immersive headset yet. Pre-orders start next week! #XR #VR #MetaQuest',
            'created_at': datetime.now() - timedelta(hours=5),
            'views': 2847653,
            'likes': 48923,
            'retweets': 15234,
            'replies': 4521,
            'url': 'https://twitter.com/MetaQuestVR/status/1234567890123456789'
        },
        {
            'id': '1234567890123456790',
            'author': 'AppleVisionPro',
            'author_name': 'Apple Vision Pro',
            'text': 'Vision Pro now supports spatial collaboration! Join your team in a shared virtual workspace with lifelike avatars and seamless app integration. The future of work is here. #VisionPro #SpatialComputing #AR',
            'created_at': datetime.now() - timedelta(hours=8),
            'views': 1923847,
            'likes': 39472,
            'retweets': 12847,
            'replies': 3284,
            'url': 'https://twitter.com/AppleVisionPro/status/1234567890123456790'
        },
        {
            'id': '1234567890123456791',
            'author': 'unity',
            'author_name': 'Unity',
            'text': 'Our new XR Development Kit 2.0 is now available! Build immersive experiences faster with improved performance, better hand tracking, and seamless cross-platform deployment. Download now at unity.com/xr #Unity #XRDev #GameDev',
            'created_at': datetime.now() - timedelta(hours=12),
            'views': 1456789,
            'likes': 28394,
            'retweets': 8923,
            'replies': 2147,
            'url': 'https://twitter.com/unity/status/1234567890123456791'
        }
    ]
    return demo_posts


def format_demo_output(posts):
    """格式化演示输出"""
    output = []
    output.append("=" * 80)
    output.append("📊 X 平台 XR 热门帖子 TOP 3 (演示模式)")
    output.append("⏰ 抓取时间: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    output.append("=" * 80)
    output.append("")
    output.append("💡 这是演示数据，展示程序实际运行时的输出格式")
    output.append("   配置真实 Twitter 账号后，将抓取真实的热门帖子")
    output.append("")
    output.append("=" * 80)
    output.append("")

    for idx, post in enumerate(posts, 1):
        output.append(f"🏆 第 {idx} 名")
        output.append(f"👤 作者: {post['author_name']} (@{post['author']})")
        output.append(f"📅 发布时间: {post['created_at'].strftime('%Y-%m-%d %H:%M:%S')}")
        output.append("")
        output.append("📝 内容:")
        output.append(f"   {post['text']}")
        output.append("")
        output.append("📈 数据统计:")
        output.append(f"   👁️  浏览量: {post['views']:,}")
        output.append(f"   ❤️  点赞数: {post['likes']:,}")
        output.append(f"   🔄 转发数: {post['retweets']:,}")
        output.append(f"   💬 回复数: {post['replies']:,}")
        output.append("")
        output.append(f"🔗 链接: {post['url']}")
        output.append("")
        output.append("-" * 80)
        output.append("")

    return "\n".join(output)


def main():
    """主函数"""
    print("\n🎬 XR 热门帖子抓取器 - 演示模式\n")

    # 生成演示数据
    posts = generate_demo_posts()

    # 格式化输出
    output = format_demo_output(posts)

    # 打印到控制台
    print(output)

    # 保存到文件
    import os
    os.makedirs('output', exist_ok=True)
    filename = f"output/demo_xr_posts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"✓ 演示结果已保存到: {filename}\n")
    print("=" * 80)
    print("📝 下一步:")
    print("=" * 80)
    print("\n1️⃣  添加 Twitter 账号 (选择一种方式):")
    print("   方式 A: python3 add_account.py <用户名> <密码> <邮箱> <邮箱密码>")
    print("   方式 B: python3 setup_accounts.py  (交互式)")
    print("\n2️⃣  运行真实抓取:")
    print("   python3 xr_scraper.py")
    print("\n3️⃣  启动定时任务:")
    print("   python3 scheduler.py")
    print("")


if __name__ == "__main__":
    main()
