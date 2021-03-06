"""Номер успешной отправки 37773940 """


def upload_photo(servers):
    """
    Upload photo
    :param servers: data centers
    """
    servers[0] -= 1
    servers[1] -= 1


def data_centers(servers):
    """
    Manages the selection of data centers
    :param servers: data centers
    :return: maximum number of photos
    """
    photos = 0
    if len(servers) <= 1:
        return 0
    while servers[0] != 0 and servers[1] != 0:
        upload_photo(servers)
        photos += 1
        servers.sort(reverse=True)
    return photos


if __name__ == "__main__":
    n = int(input())
    arr = [int(a) for a in input().split(' ')]
    print(data_centers(arr))
