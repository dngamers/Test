#!/usr/bin/env python3
"""
XR 热门帖子抓取器
自动从 X (Twitter) 上抓取 XR/VR/AR 相关的热门帖子
"""

import asyncio
import os
from datetime import datetime
from typing import List, Dict
from dotenv import load_dotenv
from twscrape import API, gather
from twscrape.logger import set_log_level

# 加载环境变量
load_dotenv()


class XRScraper:
    """XR 帖子抓取器类"""

    def __init__(self):
        self.api = API()
        self.keywords = os.getenv('XR_KEYWORDS', 'XR,VR,AR,virtual reality,augmented reality,mixed reality').split(',')
        self.top_count = int(os.getenv('TOP_POST_COUNT', '3'))

    async def initialize(self):
        """初始化 API 和账号"""
        # 设置日志级别
        set_log_level("INFO")

        # 检查是否已有账号
        accounts = await self.api.pool.accounts_info()
        if not accounts:
            print("⚠️  未检测到已登录的账号。")
            print("请运行: python setup_accounts.py 来添加账号")
            return False

        print(f"✓ 检测到 {len(accounts)} 个账号")
        return True

    def build_search_query(self) -> str:
        """构建搜索查询字符串"""
        # 使用 OR 连接所有关键词
        keywords_clean = [kw.strip() for kw in self.keywords]
        # 添加英文查询以提高准确性，排除转发
        query = f"({' OR '.join(keywords_clean)}) -filter:retweets lang:en"
        return query

    async def fetch_top_posts(self) -> List[Dict]:
        """抓取热门 XR 帖子"""
        query = self.build_search_query()
        print(f"\n🔍 搜索查询: {query}\n")

        # 使用 "Top" 产品参数来获取热门推文
        # 抓取更多帖子以便筛选出真正热门的
        tweets = await gather(
            self.api.search(query, limit=50, kv={"product": "Top"})
        )

        if not tweets:
            print("未找到任何帖子")
            return []

        print(f"✓ 找到 {len(tweets)} 条帖子")

        # 提取帖子信息并按互动度排序
        posts_data = []
        for tweet in tweets:
            # 计算总互动度 (浏览量权重较小)
            engagement_score = (
                tweet.likeCount * 3 +  # 点赞权重最高
                tweet.retweetCount * 5 +  # 转发权重更高
                tweet.replyCount * 2 +  # 回复
                (tweet.viewCount or 0) * 0.001  # 浏览量权重很小，防止低质量高浏览量
            )

            post_info = {
                'id': tweet.id,
                'text': tweet.rawContent,
                'author': tweet.user.username,
                'author_name': tweet.user.displayname,
                'url': f"https://twitter.com/{tweet.user.username}/status/{tweet.id}",
                'created_at': tweet.date,
                'views': tweet.viewCount or 0,
                'likes': tweet.likeCount,
                'retweets': tweet.retweetCount,
                'replies': tweet.replyCount,
                'engagement_score': engagement_score
            }
            posts_data.append(post_info)

        # 按互动度排序
        posts_data.sort(key=lambda x: x['engagement_score'], reverse=True)

        # 返回前 N 个
        return posts_data[:self.top_count]

    def format_post_output(self, posts: List[Dict]) -> str:
        """格式化输出帖子信息"""
        if not posts:
            return "今日未找到热门 XR 帖子"

        output = []
        output.append("=" * 80)
        output.append(f"📊 X 平台 XR 热门帖子 TOP {len(posts)}")
        output.append(f"⏰ 抓取时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        output.append("=" * 80)
        output.append("")

        for idx, post in enumerate(posts, 1):
            output.append(f"🏆 第 {idx} 名")
            output.append(f"👤 作者: {post['author_name']} (@{post['author']})")
            output.append(f"📅 发布时间: {post['created_at'].strftime('%Y-%m-%d %H:%M:%S')}")
            output.append(f"")
            output.append(f"📝 内容:")
            # 限制内容长度，避免过长
            content = post['text'][:500]
            if len(post['text']) > 500:
                content += "..."
            output.append(f"   {content}")
            output.append(f"")
            output.append(f"📈 数据统计:")
            output.append(f"   👁️  浏览量: {post['views']:,}")
            output.append(f"   ❤️  点赞数: {post['likes']:,}")
            output.append(f"   🔄 转发数: {post['retweets']:,}")
            output.append(f"   💬 回复数: {post['replies']:,}")
            output.append(f"")
            output.append(f"🔗 链接: {post['url']}")
            output.append("")
            output.append("-" * 80)
            output.append("")

        return "\n".join(output)

    async def save_to_file(self, content: str):
        """保存到文件"""
        # 创建输出目录
        os.makedirs('output', exist_ok=True)

        # 使用日期作为文件名
        filename = f"output/xr_top_posts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"\n✓ 结果已保存到: {filename}")

    async def run(self):
        """运行抓取任务"""
        print("🚀 XR 热门帖子抓取器启动")
        print("=" * 80)

        # 初始化
        if not await self.initialize():
            return

        # 抓取帖子
        print(f"\n📱 开始抓取 XR 热门帖子...")
        posts = await self.fetch_top_posts()

        # 格式化输出
        output = self.format_post_output(posts)

        # 打印到控制台
        print("\n" + output)

        # 保存到文件
        await self.save_to_file(output)

        print("\n✅ 抓取完成!")


async def main():
    """主函数"""
    scraper = XRScraper()
    await scraper.run()


if __name__ == "__main__":
    asyncio.run(main())
