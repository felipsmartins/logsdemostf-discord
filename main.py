import urllib.request as net
import http.client
import json

# TODO: some const values below should come from command line args or config file
DISCORD_CHANNEL_WEBHOOK = ''
URL_LOGS_API = 'https://logs.tf/api/v1/log'
URL_DEMOS_API = 'https://api.demos.tf'
URL_DEMOS = 'https://demos.tf'
MAX_REQUESTS_DEMOS_API = 100
UPLOADER_ID = 37267  # origin upload server ID
DEFAULT_MATCH_MODE = '6v6'


def search_demos(max_demos=3, match_mode=DEFAULT_MATCH_MODE):
    # type: (int, str) -> list
    found = []  # demos found until now
    page = 0

    def finished():
        return len(found) >= max_demos

    while not finished():
        if page == MAX_REQUESTS_DEMOS_API:
            break

        page += 1
        url = f'{URL_DEMOS_API}/demos?page={page}&type={match_mode}'
        res = net.urlopen(url)  # type: http.client.HTTPResponse
        demos = json.loads(res.read())

        for demo in demos:
            if demo['uploader'] == UPLOADER_ID:
                found.append(demo)

            if finished():
                break

    return found


if __name__ == '__main__':
    print('under development! ;)')
