from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
# from astrbot.api.all import *

@register("Development", "daiHao4312", "一个简单的功能拓展插件", "1.0.0")
class DevelopmentPlugin(Star):
    def __init__(self, context: Context, config: dict):
        self.config = config
        super().__init__(context)
    
    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("anime")  # 获取随机动漫图片
    async def anime(self, event: AstrMessageEvent):
        yield event.image_result(self.config.image_api)  # 发送图片
