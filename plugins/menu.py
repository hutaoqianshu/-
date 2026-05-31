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


async def get_image_url():
    """获取图片URL"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://t.alcy.cc/', timeout=10, allow_redirects=True) as resp:
                return str(resp.url)
    except Exception:
        pass
    return None


@handler(r'^/?菜单$', name='功能菜单', desc='显示功能菜单', priority=10)
async def show_menu(event, match):
    """显示功能菜单"""
    saying = await get_saying()
    image_url = await get_image_url()
    
    if image_url:
        message = f"[CQ:image,file={image_url}]\n\n{saying}"
    else:
        message = saying
    
    await event.reply(message)
    
    buttons = [
        [
            {"text": "🎮 王者功能", "data": "王者功能", "type": 2},
            {"text": "🎬 视频菜单", "data": "视频菜单", "type": 2},
        ],
        [
            {"text": "📚 文案菜单", "data": "文案菜单", "type": 2},
            {"text": "🛠️ 实用工具", "data": "实用工具", "type": 2},
        ],
        [
            {"text": "🎮 娱乐菜单", "data": "娱乐菜单", "type": 2},
            {"text": "📅 签到功能", "data": "签到功能", "type": 2},
        ],
        [
            {"text": "🎵 音乐系统", "data": "音乐系统", "type": 2},
            {"text": "📽️ 视频解析", "data": "视频解析", "type": 2},
        ],
        [
            {"text": "📋 免@授权", "data": "免@授权", "type": 2},
            {"text": "👥 邀请加群", "data": "邀请加群", "type": 2},
        ],
    ]
    
    await event.reply("请选择你需要的功能：", buttons=buttons)


@handler(r'^王者功能$', name='王者功能', desc='王者功能')
async def handle_king_menu(event, match):
    """王者功能"""
    await event.reply("王者功能测试")


@handler(r'^视频菜单$', name='视频菜单', desc='视频菜单')
async def handle_video_menu(event, match):
    """视频功能"""
    await event.reply("视频功能测试")


@handler(r'^文案菜单$', name='文案菜单', desc='文案菜单')
async def handle_copy_menu(event, match):
    """文案菜单"""
    await event.reply("文案菜单测试")


@handler(r'^实用工具$', name='实用工具', desc='实用工具')
async def handle_tools_menu(event, match):
    """实用工具"""
    await event.reply("实用工具测试")


@handler(r'^娱乐菜单$', name='娱乐菜单', desc='娱乐菜单')
async def handle_entertainment_menu(event, match):
    """娱乐菜单"""
    await event.reply("娱乐菜单测试")


@handler(r'^签到功能$', name='签到功能', desc='签到功能')
async def handle_checkin(event, match):
    """签到功能"""
    await event.reply("签到功能测试")


@handler(r'^音乐系统$', name='音乐系统', desc='音乐系统')
async def handle_music_system(event, match):
    """音乐系统"""
    await event.reply("音乐系统测试")


@handler(r'^视频解析$', name='视频解析', desc='视频解析')
async def handle_video_parse(event, match):
    """视频解析"""
    await event.reply("视频解析测试")


@handler(r'^免@授权$', name='免@授权', desc='免@授权')
async def handle_auth(event, match):
    """免@授权"""
    await event.reply("免@授权测试")


@handler(r'^邀请加群$', name='邀请加群', desc='邀请加群')
async def handle_invite(event, match):
    """邀请加群"""
    await event.reply("邀请加群测试")
