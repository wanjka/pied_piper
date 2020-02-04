"""
 The search engine itself. Interacts with music21 library to perform search
 on music corpus, finds all overlaps and returns ... something that can be
 interpreted as search results :-)

 The name 'Seargine' is from 'Search Engine'
"""
from music21 import converter, corpus, search

TEST_BLOB = [
        {'id': 1, 'trackName': 'MonaLisa', 'measureNumber': 22},
        {'id': 2, 'trackName': 'MonaLisa', 'measureNumber': 32},
]

def get_overlaps_file(filename):
    print('Init search engine')
# возвращает список путей ко всем произведениям, которые есть в корпусе
    paths = corpus.getPaths()
    print('done getPaths')
    results = []
    cnt = 1
    search_list = list(converter.parse(filename).recurse().notes)
    for path in paths:
        # костыли
        if not '/bach' in str(path):        # по сути ищет только у Баха
            continue                        # (иначе вообще долго)
        if 'riemenschneider' in str(path):  # и пропускает какаие-то странные
            continue                        # штуки с анализами хоралов
        # показывает, что сейчас под анализом -- ДЛЯ ОТЛАДКИ
        print(path)
        current_work = corpus.parse(path)
        # убрать из потока всё, кроме нот
        only_notes = current_work.recurse().notes
        # получить список вхождений
        entry_points = search.noteNameSearch(only_notes, search_list)
        print(entry_points)     # для отладки
        if entry_points:        # если список вхождений не пустой
            results.append({'id': cnt,
                'trackName': current_work.metadata.title,
                'composer': current_work.metadata.composer,
                'measureNumber': entry_points })
            cnt += 1
    return results

def get_overlaps(sample):
    print('Init search engine')
    paths = corpus.getPaths()
    print('done getPaths')
    results = []
    cnt = 1
    for path in paths:
        # костыли
        if not '/bach' in str(path):
            continue
        if 'riemenschneider' in str(path):
            continue
        print(path)
        current_work = corpus.parse(path)
        only_notes = current_work.recurse().notes
        search_list = list(converter.parse(f'tinynotation: {sample}').recurse().notes)
        entry_points = search.noteNameSearch(only_notes, search_list)
        print(entry_points)
        if entry_points:
            results.append({
                'id': cnt,
                'trackName': current_work.metadata.title,
                'composer': current_work.metadata.composer,
                'measureNumber': entry_points
            })
            cnt += 1
    return results

