from draft_content import read_draft_content_src
from simple_srt import tracks_to_srt_string
import os

if __name__ == '__main__':
    draft = os.getenv("LOCALAPPDATA") + '\\JianyingPro\\User Data\\Projects\\com.lveditor.draft\\'
    draft_content_directory_default = draft + os.listdir(draft)[-2]+'\\draft_content.json'
    print('最新创建的剪映草稿文件是'+ draft_content_directory_default)

    draft_content_directory = input("请输入 draft_content.json 的地址，或回车使用上面的文件")
    if not draft_content_directory:
        draft_content_directory = draft_content_directory_default
        
    tracks, name = read_draft_content_src(draft_content_directory)

    srtname = './' + os.path.splitext(name)[0] + '.srt'
    with open(srtname, 'w', encoding='utf-8') as f:
        f.write(tracks_to_srt_string(tracks))
    
    input('请查收 ' + srtname)
