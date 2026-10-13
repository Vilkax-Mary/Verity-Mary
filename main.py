import os
import discord
from discord import app_commands
from discord.ext import commands

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    try:
        synced = await client.tree.sync()
        print(f"تم تسجيل {len(synced)} أمر بنجاح!")
    except Exception as e:
        print(e)
    print(f"البوت خدام دابا باسم: {client.user}")

# أمر /start لتشغيل البوت وإدخاله لروَم الصوت كصنم دائم
@client.tree.command(name="start", description="أمر لتشغيل البوت وإدخاله لروَم الصوت كصنم دائم")
async def start_bot(interaction: discord.Interaction):
    if interaction.user.voice and interaction.user.voice.channel:
        voice_channel = interaction.user.voice.channel
        if interaction.guild.voice_client is not None:
            await interaction.guild.voice_client.move_to(voice_channel)
            await interaction.response.send_message(f"✅ تم نقل البوت بنجاح إلى الروم الصوتي: **{voice_channel.name}** ويثبت هنا!", ephemeral=True)
        else:
            await voice_channel.connect()
            await interaction.response.send_message(f"🚀 تم تفعيل البوت بنجاح! دخل لـ **{voice_channel.name}** وغادي يبقى هنا ديما كصنم.", ephemeral=True)
    else:
        await interaction.response.send_message("❌ خصك تكون داخل لشي روم صوتي أولاً عاد دير الأمر `/start`!", ephemeral=True)

# ميزة إضافية: أمر /clear لمسح الرسائل بسرعة
@client.tree.command(name="clear", description="مسح عدد محدد من الرسائل في الشات")
@app_commands.describe(amount="عدد الرسائل المراد مسحها")
async def clear(interaction: discord.Interaction, amount: int):
    if not interaction.user.guild_permissions.manage_messages:
        await interaction.response.send_message("❌ ما عندكش الصلاحية باش تستعمل هاد الأمر!", ephemeral=True)
        return
    
    await interaction.channel.purge(limit=amount)
    await interaction.response.send_message(f"🧹 تم بنجاح مسح **{amount}** رسالة!", ephemeral=True)

TOKEN = "التوكن_ديالك_هنا_بين_علامات_تنصيص"
client.run(TOKEN)
