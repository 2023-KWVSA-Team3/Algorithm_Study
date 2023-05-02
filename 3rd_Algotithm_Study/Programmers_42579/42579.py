from heapq import nlargest


def solution(genres, plays):
    # key = 장르,  value = 해당 장르의 재생 수
    genres_hash = {}
    for genre, play in zip(genres, plays):
        genres_hash[genre] = genres_hash.get(genre, 0) + play

    # 장르별 재생수가 높은 순으로 정렬한다. 이때 각 요소가 [장르, 재생수] 인 이중 리스트가 된다.
    sorted_genres = sorted(genres_hash.items(), key=lambda x: x[1], reverse=True)

    best_album = []

    # 재생수가 높은 장르 순으로 2개의 곡씩 best_album에 추가한다.
    for genre_and_play in sorted_genres:
        genre = genre_and_play[0]
        # 해당 장르의 곡 번호들을 리스트로 구현한다.
        song_list = list(filter(lambda i: genre == genres[i], range(len(plays))))

        # 해당 장르의 곡 번호와 재생수를 리스트로 구현한다. 이때 각 요소는 (곡 번호, 재생 수) 이다.
        song_list = [(i, plays[i]) for i in song_list]

        # 해당 장르 베스트 두곡의 곡 번호와 재생수를 가지고 온다. 이때 해당 장르에 한곡만 존재하면, 한곡만 가지고 온다.
        best_two_songs = nlargest(2, song_list, key=lambda x: (x[1], -x[0]))
        # 베스트 두 곡의 곡 번호만 가지고 온다.
        best_two_songs = [song[0] for song in best_two_songs]

        # 베스트 앨범에 베스트 곡 번호를 순서대로 추가한다.
        best_album.extend(best_two_songs)

    return best_album
