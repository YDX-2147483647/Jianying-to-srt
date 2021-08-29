import json
from os.path import join, dirname


def get_meta_info_path(content_path: str) -> str:
    """
    获取 meta_info.json 的路径
    :param content_path: content.json 的路径
    :return: draft_meta_info.json 的路径
    """
    return join(dirname(content_path), 'draft_meta_info.json')


def get_draft_name(directory: str) -> str:
    """
    获取项目名称
    :param directory: meta_info.json 的路径
    :return: 项目名称
    """
    with open(directory, 'r', encoding='utf-8') as f:
        meta_info = json.loads(f.read())
    return meta_info['draft_name']


def get_draft_name_from_content_path(content_path: str) -> str:
    return get_draft_name(get_meta_info_path(content_path))
