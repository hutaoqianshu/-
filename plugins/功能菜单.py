import aiohttp
from core.plugin.decorators import handler

__plugin_meta__ = {
    'name': '功能菜单',
    'author': 'ElainaBot',
    'description': '提供功能菜单命令',
    'version': '1.0.0',
}


async def get_saying():
    """获取每日一言"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://uapis.cn/api/v1/saying', timeout=10) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    return data.get('text', '今天也要开心哦！')
    except Exception:
        pass
    return '今天也要开心哦！'


async def download_image(url):
    """下载图片为字节流"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as resp:
                if resp.status == 200:
                    return await resp.read()
    except Exception:
        pass
    return None


@handler(r'^/?菜单$', name='功能菜单', desc='显示功能菜单', priority=10)
async def show_menu(event, match):
    """显示功能菜单"""
    saying = await get_saying()
    
    # 先下载图片再发送
    image_bytes = await download_image("https://imgapi.xl0408.top/index.php")
    if image_bytes:
        await event.reply_image(image_bytes, "")
    else:
        await event.reply(saying)
        return
    
    # 再发送每日一言和按钮
    buttons = [
        [
            {"text": "🔍 查询功能", "data": "查询功能", "type": 2},
            {"text": "🎬 视频菜单", "data": "视频菜单", "type": 2},
            {"text": "📝 文案功能", "data": "文案功能", "type": 2},
        ],
        [
            {"text": "❓ 常见问题", "data": "常见问题", "type": 2},
            {"text": "📅 签到功能", "data": "签到功能", "type": 2},
            {"text": "📷 图片菜单", "data": "图片菜单", "type": 2},
        ],
    ]
    
    await event.reply(saying, buttons=buttons)


@handler(r'^查询功能$', name='查询功能', desc='查询功能')
async def query_test(event, match):
    """查询功能"""
    await event.reply("查询功能测试")


@handler(r'^视频菜单$', name='视频菜单', desc='视频菜单')
async def video_test(event, match):
    """视频功能"""
    await event.reply("视频功能测试")


@handler(r'^文案功能$', name='文案功能', desc='文案功能')
async def copy_test(event, match):
    """文案功能"""
    await event.reply("文案功能测试")


@handler(r'^常见问题$', name='常见问题', desc='常见问题')
async def faq_test(event, match):
    """常见问题"""
    await event.reply("常见问题测试")


@handler(r'^签到功能$', name='签到功能', desc='签到功能')
async def checkin_test(event, match):
    """签到功能"""
    await event.reply("签到功能测试")


@handler(r'^图片菜单$', name='图片菜单', desc='图片菜单')
async def image_test(event, match):
    """图片菜单"""
    await event.reply("图片菜单测试")
