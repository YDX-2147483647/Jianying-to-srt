# 转换剪映字幕

> 2021年4月30日。

[剪映](https://lv.ulikecam.com/)是一款剪辑软件，据说它的（中文）字幕识别效果特别好，然而无法导出导出字幕文件。还好其轨道是用 JSON 存储的，可由此制作 *.srt 字幕文件。

您首先需要找到这个`draft_content.json`文件。当您打开剪映的一个草稿时，右侧的“草稿参数”栏会显示“保存位置”（此外还有“作品名称”“色彩空间”），`draft_content.json`就在这个文件夹中（该文件夹中可能还有`draft_cover.jpg`、`draft_meta_info.json`、`draft_settings`）。
