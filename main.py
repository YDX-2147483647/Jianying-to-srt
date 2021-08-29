from os import getenv
from os.path import join, getctime
import glob

from draft_content import read_draft_content_src
from simple_srt import tracks_to_srt_string
from draft_meta_info import get_draft_name_from_content_path

if __name__ == '__main__':
    drafts_parent = join(getenv("LOCALAPPDATA"), './JianyingPro/User Data/Projects/com.lveditor.draft/')
    drafts_contents = glob.glob(drafts_parent + './*/draft_content.json')
    latest_draft_content = max(drafts_contents, key=getctime)
    print('最新创建的剪映草稿文件如下。')
    print(latest_draft_content)

    draft_content = input("请输入 draft_content.json 的地址，留空则使用上面的文件。>>>")
    if not draft_content:
        draft_content = latest_draft_content

    tracks, _ = read_draft_content_src(draft_content)
    name = get_draft_name_from_content_path(draft_content)

    subtitle_filename = f'./{name}.srt'
    with open(subtitle_filename, 'w', encoding='utf-8') as f:
        f.write(tracks_to_srt_string(tracks))

    print(f'请查收 {subtitle_filename}。')
    input('请按 Enter 继续. . .')
