import json


def draft_content_to_tracks(draft_content: json) -> list:
    texts = {t['id']: t['content']
             for t in draft_content['materials']['texts']
             if t['type'] == 'subtitle'}

    """[
        'start': (μs),
        'end': (μs),
        'content': (...)
    }]"""
    tracks = []
    for t in draft_content['tracks']:
        for s in t['segments']:
            if s['material_id'] in texts.keys():
                timerange = s['target_timerange']
                tracks.append({
                    'start': timerange['start'],
                    'end': timerange['start'] + timerange['duration'],
                    'content': texts[s['material_id']]
                })

    return tracks


def get_material_name(draft_content: json) -> str:
    return draft_content['materials']['videos'][0]['material_name']


def read_draft_content_src(directory: str) -> (list, str):
    with open(directory, 'r', encoding='utf-8') as f:
        draft_content = json.loads(f.read())
    tracks = draft_content_to_tracks(draft_content)
    name = get_material_name(draft_content)
    return tracks, name
