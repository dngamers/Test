#!/usr/bin/env python3
"""
真实场景演示 - 模拟实际抓取结果
使用近期真实的 XR 话题和合理的数据
"""

from datetime import datetime, timedelta
import random


def generate_realistic_posts():
    """生成真实场景的演示数据"""

    # 基于 2026 年 1 月的真实 XR 趋势
    realistic_posts = [
        {
            'id': '1881234567890123456',
            'author': 'MetaQuestVR',
            'author_name': 'Meta Quest',
            'text': 'Meta Quest 3S just dropped to $299 for a limited time! This is the perfect entry point into XR. Featuring inside-out tracking, 4K+ display, and access to our entire library of 500+ apps. Link in bio 🎮 #MetaQuest #VR #XR',
            'created_at': datetime.now() - timedelta(hours=6),
            'views': 1847293,
            'likes': 34521,
            'retweets': 8934,
            'replies': 2847,
            'url': 'https://twitter.com/MetaQuestVR/status/1881234567890123456'
        },
        {
            'id': '1881234567890123457',
            'author': 'ID_Xbox',
            'author_name': 'Xbox',
            'text': 'Cloud gaming meets mixed reality. Xbox Cloud Gaming is now optimized for Vision Pro and Quest 3. Play your favorite titles on a virtual 200" screen anywhere. The future of gaming is here. 🎮☁️ #Xbox #CloudGaming #XR',
            'created_at': datetime.now() - timedelta(hours=9),
            'views': 2134892,
            'likes': 41283,
            'retweets': 12847,
            'replies': 3921,
            'url': 'https://twitter.com/ID_Xbox/status/1881234567890123457'
        },
        {
            'id': '1881234567890123458',
            'author': 'MKBHD',
            'author_name': 'Marques Brownlee',
            'text': 'Just spent a week with Vision Pro 2.0 and WOW. The eye tracking improvements are game-changing. Full review dropping tomorrow but short version: spatial computing is finally ready for mainstream. Thread 🧵👇 #VisionPro #SpatialComputing #AR',
            'created_at': datetime.now() - timedelta(hours=4),
            'views': 3847291,
            'likes': 67842,
            'retweets': 18923,
            'replies': 5284,
            'url': 'https://twitter.com/MKBHD/status/1881234567890123458'
        },
        {
            'id': '1881234567890123459',
            'author': 'unity',
            'author_name': 'Unity',
            'text': 'Unity 2026.1 brings native OpenXR support with zero-config deployment across Quest, Pico, Vision Pro & more. Plus NEW: Real-time hand tracking API, improved passthrough rendering, and 40% better performance. Download now 🚀 unity.com/xr #GameDev #Unity #XRDev',
            'created_at': datetime.now() - timedelta(hours=14),
            'views': 892347,
            'likes': 23847,
            'retweets': 6284,
            'replies': 1847,
            'url': 'https://twitter.com/unity/status/1881234567890123459'
        },
        {
            'id': '1881234567890123460',
            'author': 'SonyPlayStation',
            'author_name': 'PlayStation',
            'text': 'PlayStation VR2 + Horizon Call of the Mountain bundle now $449. Experience the future of gaming with 4K HDR, haptic feedback, and eye tracking. Limited time offer 🎮 #PSVR2 #PlayStation #VR',
            'created_at': datetime.now() - timedelta(hours=11),
            'views': 1547283,
            'likes': 28934,
            'retweets': 7483,
            'replies': 2184,
            'url': 'https://twitter.com/SonyPlayStation/status/1881234567890123460'
        },
        {
            'id': '1881234567890123461',
            'author': 'timsweeney',
            'author_name': 'Tim Sweeney',
            'text': 'Unreal Engine 5.5 brings photorealistic rendering to XR. Real-time ray tracing, Nanite for VR, and Lumen global illumination - all running at 90fps on Quest 3. The metaverse is being built right now. Check out the demo 👀 #UnrealEngine #VR #Metaverse',
            'created_at': datetime.now() - timedelta(hours=7),
            'views': 1234567,
            'likes': 31284,
            'retweets': 8472,
            'replies': 2638,
            'url': 'https://twitter.com/timsweeney/status/1881234567890123461'
        },
        {
            'id': '1881234567890123462',
            'author': 'valvesoftware',
            'author_name': 'Valve',
            'text': 'Steam VR Winter Sale: Up to 80% off on top XR titles. Half-Life: Alyx, Beat Saber, Boneworks and 500+ more games. Plus Valve Index now $799 (was $999). Sale ends Sunday! 🎮 #SteamVR #VR #Gaming',
            'created_at': datetime.now() - timedelta(hours=18),
            'views': 987654,
            'likes': 19847,
            'retweets': 5284,
            'replies': 1423,
            'url': 'https://twitter.com/valvesoftware/status/1881234567890123462'
        },
        {
            'id': '1881234567890123463',
            'author': 'UploadVR',
            'author_name': 'UploadVR',
            'text': 'BREAKING: New leak shows Meta working on Quest 4 with microOLED displays, inside-out body tracking, and neural wristband controls. Expected Q4 2026. This could be the iPhone moment for XR 🚀 Full article: uploadvr.com/quest-4-leak #MetaQuest #VR',
            'created_at': datetime.now() - timedelta(hours=3),
            'views': 1647382,
            'likes': 27483,
            'retweets': 9284,
            'replies': 3147,
            'url': 'https://twitter.com/UploadVR/status/1881234567890123463'
        }
    ]

    # 添加一些随机变化使数据更真实
    for post in realistic_posts:
        # 添加小的随机波动
        post['views'] += random.randint(-5000, 5000)
        post['likes'] += random.randint(-500, 500)
        post['retweets'] += random.randint(-100, 100)
        post['replies'] += random.randint(-50, 50)

        # 计算互动分数
        post['engagement_score'] = (
            post['likes'] * 3 +
            post['retweets'] * 5 +
            post['replies'] * 2 +
            post['views'] * 0.001
        )

    # 按互动分数排序
    realistic_posts.sort(key=lambda x: x['engagement_score'], reverse=True)

    return realistic_posts[:3]


def format_output(posts):
    """格式化输出"""
    output = []
    output.append("=" * 80)
    output.append("📊 X 平台 XR 热门帖子 TOP 3 - 真实场景演示")
    output.append("⏰ 抓取时间: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    output.append("=" * 80)
    output.append("")
    output.append("💡 这是基于真实 XR 话题的演示数据")
    output.append("   实际运行时，会抓取 Twitter 上的真实最新帖子")
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
        output.append(f"   📊 互动分数: {post['engagement_score']:,.0f}")
        output.append("")
        output.append(f"🔗 链接: {post['url']}")
        output.append("")
        output.append("-" * 80)
        output.append("")

    return "\n".join(output)


def main():
    """主函数"""
    print("\n🎬 XR 热门帖子抓取器 - 真实场景演示\n")
    print("模拟实际运行效果，使用基于真实 XR 趋势的数据...\n")

    # 生成数据
    posts = generate_realistic_posts()

    # 格式化输出
    output = format_output(posts)

    # 打印到控制台
    print(output)

    # 保存到文件
    import os
    os.makedirs('output', exist_ok=True)
    filename = f"output/realistic_demo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"\n✓ 演示结果已保存到: {filename}\n")
    print("=" * 80)
    print("📝 说明:")
    print("=" * 80)
    print("\n这个演示展示了程序实际运行时的效果：")
    print("  • 搜索 XR/VR/AR 相关热门话题")
    print("  • 按互动度（点赞×3 + 转发×5 + 回复×2 + 浏览×0.001）排序")
    print("  • 显示完整数据和链接")
    print("  • 自动保存结果")
    print("\n在能访问 Twitter 的环境中运行 xr_scraper.py 将获取真实数据！")
    print("")


if __name__ == "__main__":
    main()
