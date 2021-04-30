from draft_content import read_draft_content_src
from simple_srt import tracks_to_srt_string

if __name__ == '__main__':
    print(r'''剪映的草稿文件位于 C:\Users\bjalp\AppData\Local\JianyingPro\User Data\Projects 。''')

    draft_content_directory = input("请输入 draft_content.json 的地址>>")
    if not draft_content_directory:
        draft_content_directory = r'C:\Users\bjalp\AppData\Local\JianyingPro\User Data\Projects\com.lveditor.draft\85E36163-D02E-4ed0-8253-CFC4F9E4D720\draft_content.json'

    tracks = read_draft_content_src(draft_content_directory)

    with open('./subtitles.srt', 'w', encoding='utf-8') as f:
        f.write(tracks_to_srt_string(tracks))
    
    input('请查收 subtitles.srt。')
