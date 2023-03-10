# Код спизжен из модуля print, автора KeyZenD
# Govnocode by @kompot_69
from .. import loader, utils
@loader.tds
class FixLayoutMod(loader.Module):
	"""Фиксит раскладку"""
	strings = {"name": "Fix Layout"}
	@loader.owner
	async def flcmd(self, message):
		""".fl <text or reply> en>ru"""
		layout = dict(zip(map(ord, "qwertyuiop[]asdfghjkl;'zxcvbnm,./`" 'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'), "йцукенгшщзхъфывапролджэячсмитьбю.ё" 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'))
		text = utils.get_args_raw(message)
		if not text:
			reply = await message.get_reply_message()
			if not reply or not reply.message:
				await message.edit("<b>Текста нет!</b>")
				return
			text = reply.message
		text = text.translate(layout)
		await message.edit(text)
	async def flrcmd(self, message):
		""".flr <text or reply> ru>en"""
		layout = dict(zip(map(ord, "йцукенгшщзхъфывапролджэячсмитьбю.ё" 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'), "qwertyuiop[]asdfghjkl;'zxcvbnm,./`" 'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'))
		text = utils.get_args_raw(message)
		if not text:
			reply = await message.get_reply_message()
			if not reply or not reply.message:
				await message.edit("<b>Текста нет!</b>")
				return
			text = reply.message
		text = text.translate(layout)
		await message.edit(text)
