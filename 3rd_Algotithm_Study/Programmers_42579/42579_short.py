def solution(genres, plays):
    # key = 장르, vlaue = 해당 장르 플레이 수로 hash table 구성한다.
    genres_hash = {genre:sum([plays[i] for i in range(len(plays)) if genres[i] == genre]) for genre in set(genres)}

    # 해당 hash table을 플레이가 많은 순으로 정렬해서 리스트로 변환한다.
    sorted_genres = sorted(genres_hash.items(), key=lambda x: -x[1])

    # 플레이가 많이 된 순으로 노래의 번호를 저장하는 이중 리스트를 구성한다. 이때 각 요소는 장르별로 노래의 번호를 리스트로 묶은 것이다.
    song_by_sorted_genres = [[i for i in range(len(plays)) if genres[i] == genre[0]] for genre in sorted_genres]

    # 위의 이중 리스트에서 각 요소에 해당되는 리스트를 플레이 순으로 정렬한다.(플레이 수가 같다면 노래의 고유 번호로 정렬)
    sorted_song =  [sorted(genre_play, key=lambda i: (-plays[i], i)) for genre_play in song_by_sorted_genres]

    # 위의 이중 리스트에서 각 요소의 리스트에서 노래 번호를 2개씩 가지고 와서 리스트로 반환한다.
    # 만약 해당 장르의 곡이 하나만 존재하면 노래 번호를 하나만 가져온다.
    return [song[index] for song in sorted_song for index in range(min(2, len(song)))]
